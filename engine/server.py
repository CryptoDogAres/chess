#!/usr/bin/env python3
"""
Pikafish UCI Engine HTTP Bridge

A lightweight HTTP server that wraps the Pikafish xiangqi engine,
exposing position analysis via a REST API.

Requires: Python 3.8+, Pikafish binary in the engine/ folder.
No external dependencies — uses only the Python standard library.

Usage:
    python3 server.py [--port 8080] [--engine-path ./pikafish] [--threads 1] [--hash 128]
"""

import argparse
import json
import os
import signal
import subprocess
import sys
import threading
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path


# ---------------------------------------------------------------------------
# Engine process wrapper
# ---------------------------------------------------------------------------

class PikafishEngine:
    """Manages a Pikafish subprocess communicating over UCI protocol."""

    def __init__(self, engine_path: str, threads: int = 1, hash_mb: int = 128):
        self.engine_path = engine_path
        self.threads = threads
        self.hash_mb = hash_mb
        self.process = None  # type: subprocess.Popen
        self.lock = threading.Lock()
        self._alive = False

    # -- lifecycle -----------------------------------------------------------

    def start(self):
        """Launch the engine subprocess and send initial UCI handshake."""
        self.process = subprocess.Popen(
            [self.engine_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
        )
        # UCI handshake
        self._send("uci")
        self._read_until("uciok", timeout=10)

        # Configure options
        self._send(f"setoption name Threads value {self.threads}")
        self._send(f"setoption name Hash value {self.hash_mb}")
        self._send("isready")
        self._read_until("readyok", timeout=10)

        self._alive = True

    def stop(self):
        """Gracefully shut down the engine."""
        if self.process and self.process.poll() is None:
            try:
                self._send("quit")
                self.process.wait(timeout=5)
            except Exception:
                self.process.kill()
        self._alive = False

    @property
    def is_alive(self) -> bool:
        return self._alive and self.process is not None and self.process.poll() is None

    # -- low-level I/O -------------------------------------------------------

    def _send(self, command: str):
        if self.process and self.process.stdin:
            self.process.stdin.write(command + "\n")
            self.process.stdin.flush()

    def _readline(self, timeout: float = 30) -> str:
        """Read one line from engine stdout with a timeout."""
        if not self.process or not self.process.stdout:
            raise RuntimeError("Engine process not running")
        # Use a simple blocking read; the engine is generally responsive.
        # For robustness we rely on the caller's timeout expectations.
        line = self.process.stdout.readline()
        if not line:
            raise RuntimeError("Engine process closed stdout unexpectedly")
        return line.strip()

    def _read_until(self, token: str, timeout: float = 30):
        """Read lines until one starts with *token*. Returns all lines read."""
        lines = []
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            line = self._readline(timeout)
            lines.append(line)
            if line.startswith(token):
                return lines
        raise TimeoutError(f"Timed out waiting for '{token}' from engine")

    # -- high-level commands --------------------------------------------------

    def analyze(self, fen: str, depth: int = 20, multipv: int = 1) -> dict:
        """Run a fixed-depth analysis and return structured results."""
        with self.lock:
            if multipv > 1:
                self._send(f"setoption name MultiPV value {multipv}")
            else:
                self._send("setoption name MultiPV value 1")

            self._send("ucinewgame")
            self._send("isready")
            self._read_until("readyok", timeout=10)

            self._send(f"position fen {fen}")
            self._send(f"go depth {depth}")

            lines = self._read_until("bestmove", timeout=120)

            return self._parse_analysis(lines, fen, depth, multipv)

    def bestmove(self, fen: str, movetime: int = 2000) -> dict:
        """Return the single best move for a position."""
        with self.lock:
            self._send("setoption name MultiPV value 1")
            self._send("ucinewgame")
            self._send("isready")
            self._read_until("readyok", timeout=10)

            self._send(f"position fen {fen}")
            self._send(f"go movetime {movetime}")

            lines = self._read_until("bestmove", timeout=max(30, movetime // 1000 + 10))

            bestmove_line = lines[-1]
            parts = bestmove_line.split()
            bm = parts[1] if len(parts) > 1 else None
            ponder = parts[3] if len(parts) > 3 and parts[2] == "ponder" else None

            return {"fen": fen, "bestmove": bm, "ponder": ponder}

    # -- parsing -------------------------------------------------------------

    @staticmethod
    def _parse_analysis(lines, fen, depth, multipv):
        """Parse UCI info lines into a structured analysis dict."""
        pvs = {}

        for line in lines:
            if not line.startswith("info "):
                continue
            tokens = line.split()
            info: dict = {}
            i = 1
            while i < len(tokens):
                key = tokens[i]
                if key == "depth":
                    info["depth"] = int(tokens[i + 1])
                    i += 2
                elif key == "seldepth":
                    info["seldepth"] = int(tokens[i + 1])
                    i += 2
                elif key == "multipv":
                    info["multipv"] = int(tokens[i + 1])
                    i += 2
                elif key == "score":
                    score_type = tokens[i + 1]
                    score_val = int(tokens[i + 2])
                    info["score_type"] = score_type
                    info["score_val"] = score_val
                    i += 3
                elif key == "nodes":
                    info["nodes"] = int(tokens[i + 1])
                    i += 2
                elif key == "nps":
                    info["nps"] = int(tokens[i + 1])
                    i += 2
                elif key == "time":
                    info["time"] = int(tokens[i + 1])
                    i += 2
                elif key == "pv":
                    info["pv"] = " ".join(tokens[i + 1 :])
                    break
                else:
                    i += 1

            pv_idx = info.get("multipv", 1)
            d = info.get("depth", 0)
            # Keep the deepest info for each PV line
            if pv_idx not in pvs or d >= pvs[pv_idx].get("depth", 0):
                pvs[pv_idx] = info

        analysis = []
        for idx in sorted(pvs.keys()):
            entry = pvs[idx]
            score_cp = entry.get("score_val") if entry.get("score_type") == "cp" else None
            score_mate = entry.get("score_val") if entry.get("score_type") == "mate" else None
            analysis.append({
                "pv_index": idx,
                "depth": entry.get("depth"),
                "score_cp": score_cp,
                "score_mate": score_mate,
                "nodes": entry.get("nodes"),
                "nps": entry.get("nps"),
                "time_ms": entry.get("time"),
                "pv": entry.get("pv", ""),
            })

        # Extract bestmove from last line
        bestmove = None
        for line in reversed(lines):
            if line.startswith("bestmove"):
                parts = line.split()
                bestmove = parts[1] if len(parts) > 1 else None
                break

        return {
            "fen": fen,
            "depth": depth,
            "multipv": multipv,
            "analysis": analysis,
            "bestmove": bestmove,
        }


# ---------------------------------------------------------------------------
# HTTP server
# ---------------------------------------------------------------------------

class EngineHandler(BaseHTTPRequestHandler):
    """HTTP request handler exposing Pikafish over REST."""

    engine: PikafishEngine  # set on the class before serving

    # Suppress default logging to stderr for each request
    def log_message(self, fmt, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {fmt % args}\n")

    # -- CORS helpers --------------------------------------------------------

    def _set_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def _json_response(self, data: dict, status: int = 200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self._set_cors_headers()
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _error_response(self, message: str, status: int = 400):
        self._json_response({"error": message}, status)

    def _read_json_body(self) -> dict:
        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            return {}
        raw = self.rfile.read(length)
        return json.loads(raw)

    # -- routing -------------------------------------------------------------

    def do_OPTIONS(self):
        self.send_response(204)
        self._set_cors_headers()
        self.end_headers()

    def do_GET(self):
        if self.path == "/health":
            self._handle_health()
        else:
            self._error_response("Not found. Available endpoints: GET /health, POST /analyze, POST /bestmove", 404)

    def do_POST(self):
        if self.path == "/analyze":
            self._handle_analyze()
        elif self.path == "/bestmove":
            self._handle_bestmove()
        else:
            self._error_response("Not found. Available endpoints: GET /health, POST /analyze, POST /bestmove", 404)

    # -- handlers ------------------------------------------------------------

    def _handle_health(self):
        alive = self.engine.is_alive
        self._json_response({
            "status": "ok" if alive else "engine_down",
            "engine": "Pikafish",
            "threads": self.engine.threads,
            "hash": self.engine.hash_mb,
        }, 200 if alive else 503)

    def _handle_analyze(self):
        try:
            body = self._read_json_body()
        except (json.JSONDecodeError, ValueError) as exc:
            self._error_response(f"Invalid JSON: {exc}")
            return

        fen = body.get("fen")
        if not fen:
            self._error_response("Missing required field: fen")
            return

        depth = int(body.get("depth", 20))
        multipv = int(body.get("multipv", 1))

        if depth < 1 or depth > 100:
            self._error_response("depth must be between 1 and 100")
            return
        if multipv < 1 or multipv > 10:
            self._error_response("multipv must be between 1 and 10")
            return

        try:
            result = self.engine.analyze(fen, depth=depth, multipv=multipv)
            self._json_response(result)
        except Exception as exc:
            self._error_response(f"Engine error: {exc}", 500)

    def _handle_bestmove(self):
        try:
            body = self._read_json_body()
        except (json.JSONDecodeError, ValueError) as exc:
            self._error_response(f"Invalid JSON: {exc}")
            return

        fen = body.get("fen")
        if not fen:
            self._error_response("Missing required field: fen")
            return

        movetime = int(body.get("movetime", 2000))
        if movetime < 100 or movetime > 60000:
            self._error_response("movetime must be between 100 and 60000 ms")
            return

        try:
            result = self.engine.bestmove(fen, movetime=movetime)
            self._json_response(result)
        except Exception as exc:
            self._error_response(f"Engine error: {exc}", 500)


# ---------------------------------------------------------------------------
# Binary detection
# ---------------------------------------------------------------------------

def find_engine_binary(engine_dir: Path):
    """Auto-detect a Pikafish binary in the given directory."""
    candidates = (
        list(engine_dir.glob("pikafish*"))
        + list(engine_dir.glob("Pikafish*"))
    )
    for candidate in candidates:
        if candidate.is_file() and candidate.suffix not in (".py", ".txt", ".md", ".sh", ".json", ".nnue", ".bin", ".7z", ".zip", ".tar", ".gz"):
            return candidate
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="HTTP bridge for the Pikafish xiangqi engine"
    )
    parser.add_argument("--port", type=int, default=8080, help="Server port (default: 8080)")
    parser.add_argument("--engine-path", type=str, default=None,
                        help="Path to Pikafish binary (auto-detected if omitted)")
    parser.add_argument("--threads", type=int, default=1, help="Engine threads (default: 1)")
    parser.add_argument("--hash", type=int, default=128, help="Hash table size in MB (default: 128)")
    args = parser.parse_args()

    engine_dir = Path(__file__).resolve().parent

    # Resolve engine binary
    if args.engine_path:
        engine_path = Path(args.engine_path)
    else:
        engine_path = find_engine_binary(engine_dir)

    if engine_path is None or not engine_path.is_file():
        print("ERROR: Pikafish binary not found.", file=sys.stderr)
        print("", file=sys.stderr)
        print("To fix this, do one of the following:", file=sys.stderr)
        print(f"  1. Run: bash {engine_dir / 'install.sh'}", file=sys.stderr)
        print(f"  2. Download from https://github.com/official-pikafish/Pikafish/releases", file=sys.stderr)
        print(f"     and place the binary in {engine_dir}", file=sys.stderr)
        print(f"  3. Specify the path: python3 server.py --engine-path /path/to/pikafish", file=sys.stderr)
        sys.exit(1)

    if not os.access(engine_path, os.X_OK):
        print(f"WARNING: {engine_path} is not executable. Attempting chmod +x ...", file=sys.stderr)
        os.chmod(engine_path, 0o755)

    # Start engine
    print(f"Starting Pikafish engine: {engine_path}")
    print(f"  Threads: {args.threads}  |  Hash: {args.hash} MB")

    engine = PikafishEngine(str(engine_path), threads=args.threads, hash_mb=args.hash)
    try:
        engine.start()
    except Exception as exc:
        print(f"ERROR: Failed to start engine: {exc}", file=sys.stderr)
        sys.exit(1)

    print("Engine ready.")

    # Attach engine to handler class
    EngineHandler.engine = engine

    # Start HTTP server
    server = HTTPServer(("0.0.0.0", args.port), EngineHandler)
    print(f"Listening on http://localhost:{args.port}")
    print("Endpoints: POST /analyze  |  POST /bestmove  |  GET /health")
    print("Press Ctrl+C to stop.\n")

    # Graceful shutdown on SIGINT / SIGTERM
    def shutdown(signum, frame):
        print("\nShutting down...")
        engine.stop()
        server.shutdown()

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    try:
        server.serve_forever()
    finally:
        engine.stop()
        print("Server stopped.")


if __name__ == "__main__":
    main()
