#!/usr/bin/env python3
"""
Standalone CLI tool for batch Pikafish analysis.

Analyzes one or more xiangqi positions using the Pikafish engine and
outputs results as human-readable text or JSON.

Requires: Python 3.8+, Pikafish binary in the engine/ folder.
No external dependencies.

Usage:
    python3 analyze.py --fen "rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w" --depth 20
    python3 analyze.py --file positions.txt --output results.json
    python3 analyze.py --file positions.txt --depth 18 --multipv 5
"""

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path


# ---------------------------------------------------------------------------
# Engine communication
# ---------------------------------------------------------------------------

class PikafishCLI:
    """Minimal Pikafish wrapper for CLI batch usage."""

    def __init__(self, engine_path: str, threads: int = 1, hash_mb: int = 128):
        self.engine_path = engine_path
        self.threads = threads
        self.hash_mb = hash_mb
        self.process = None

    def start(self):
        self.process = subprocess.Popen(
            [self.engine_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
        )
        self._send("uci")
        self._read_until("uciok")
        self._send(f"setoption name Threads value {self.threads}")
        self._send(f"setoption name Hash value {self.hash_mb}")
        self._send("isready")
        self._read_until("readyok")

    def stop(self):
        if self.process and self.process.poll() is None:
            try:
                self._send("quit")
                self.process.wait(timeout=5)
            except Exception:
                self.process.kill()

    def _send(self, cmd: str):
        if self.process and self.process.stdin:
            self.process.stdin.write(cmd + "\n")
            self.process.stdin.flush()

    def _readline(self) -> str:
        if not self.process or not self.process.stdout:
            raise RuntimeError("Engine not running")
        line = self.process.stdout.readline()
        if not line:
            raise RuntimeError("Engine closed unexpectedly")
        return line.strip()

    def _read_until(self, token: str, timeout: float = 30) -> list:
        lines = []
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            line = self._readline()
            lines.append(line)
            if line.startswith(token):
                return lines
        raise TimeoutError(f"Timed out waiting for '{token}'")

    def analyze(self, fen: str, depth: int = 20, multipv: int = 3) -> dict:
        """Analyze a position and return structured results."""
        self._send(f"setoption name MultiPV value {multipv}")
        self._send("ucinewgame")
        self._send("isready")
        self._read_until("readyok")
        self._send(f"position fen {fen}")
        self._send(f"go depth {depth}")
        lines = self._read_until("bestmove", timeout=120)
        return self._parse(lines, fen, depth, multipv)

    @staticmethod
    def _parse(lines: list, fen: str, depth: int, multipv: int) -> dict:
        pvs = {}
        for line in lines:
            if not line.startswith("info "):
                continue
            tokens = line.split()
            info = {}
            i = 1
            while i < len(tokens):
                key = tokens[i]
                if key == "depth":
                    info["depth"] = int(tokens[i + 1]); i += 2
                elif key == "multipv":
                    info["multipv"] = int(tokens[i + 1]); i += 2
                elif key == "score":
                    info["score_type"] = tokens[i + 1]
                    info["score_val"] = int(tokens[i + 2]); i += 3
                elif key == "nodes":
                    info["nodes"] = int(tokens[i + 1]); i += 2
                elif key == "nps":
                    info["nps"] = int(tokens[i + 1]); i += 2
                elif key == "time":
                    info["time"] = int(tokens[i + 1]); i += 2
                elif key == "pv":
                    info["pv"] = " ".join(tokens[i + 1:]); break
                else:
                    i += 1
            pv_idx = info.get("multipv", 1)
            d = info.get("depth", 0)
            if pv_idx not in pvs or d >= pvs[pv_idx].get("depth", 0):
                pvs[pv_idx] = info

        analysis = []
        for idx in sorted(pvs.keys()):
            e = pvs[idx]
            score_cp = e.get("score_val") if e.get("score_type") == "cp" else None
            score_mate = e.get("score_val") if e.get("score_type") == "mate" else None
            analysis.append({
                "pv_index": idx,
                "depth": e.get("depth"),
                "score_cp": score_cp,
                "score_mate": score_mate,
                "pv": e.get("pv", ""),
            })

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
            "bestmove": bestmove,
            "analysis": analysis,
        }


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def format_score(entry: dict) -> str:
    """Human-readable score string."""
    if entry.get("score_mate") is not None:
        m = entry["score_mate"]
        return f"Mate in {m}" if m > 0 else f"Mated in {abs(m)}"
    cp = entry.get("score_cp", 0) or 0
    return f"{cp / 100:+.2f}"


def print_human(result: dict, index: int = 0):
    """Print one analysis result in a readable format."""
    if index > 0:
        print()
    fen = result["fen"]
    # Extract comment from fen if present (for file-based analysis)
    comment = result.get("comment", "")
    header = f"Position: {fen}"
    if comment:
        header += f"  ({comment})"
    print(header)
    print("-" * min(len(header), 80))
    print(f"  Best move : {result['bestmove']}")
    print(f"  Depth     : {result['depth']}")
    print()
    for entry in result.get("analysis", []):
        score = format_score(entry)
        pv = entry.get("pv", "")
        # Show first 8 moves of PV for readability
        pv_short = " ".join(pv.split()[:8])
        if len(pv.split()) > 8:
            pv_short += " ..."
        print(f"  PV {entry['pv_index']}: [{score:>8s}]  {pv_short}")
    print()


# ---------------------------------------------------------------------------
# Position file parsing
# ---------------------------------------------------------------------------

def load_positions(filepath: str) -> list:
    """Load FEN positions from a file. Lines starting with # are skipped.
    Inline comments after # are preserved as metadata."""
    positions = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # Split FEN from optional inline comment
            if " # " in line:
                fen_part, comment = line.split(" # ", 1)
            elif "#" in line and not line.startswith("#"):
                # Handle FEN#comment (no spaces around #)
                fen_part, comment = line.split("#", 1)
            else:
                fen_part, comment = line, ""
            positions.append({"fen": fen_part.strip(), "comment": comment.strip()})
    return positions


# ---------------------------------------------------------------------------
# Binary detection (shared with server.py)
# ---------------------------------------------------------------------------

def find_engine_binary(engine_dir: Path):
    candidates = (
        list(engine_dir.glob("pikafish*"))
        + list(engine_dir.glob("Pikafish*"))
    )
    for c in candidates:
        if c.is_file() and c.suffix not in (".py", ".txt", ".md", ".sh", ".json", ".nnue", ".bin", ".7z", ".zip", ".tar", ".gz"):
            return c
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Batch position analysis using Pikafish"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fen", type=str, help="Single FEN string to analyze")
    group.add_argument("--file", type=str, help="File with FEN strings (one per line)")

    parser.add_argument("--depth", type=int, default=20, help="Search depth (default: 20)")
    parser.add_argument("--multipv", type=int, default=3, help="Number of principal variations (default: 3)")
    parser.add_argument("--output", type=str, default=None,
                        help="Output file for JSON results (omit for human-readable stdout)")
    parser.add_argument("--engine-path", type=str, default=None,
                        help="Path to Pikafish binary (auto-detected if omitted)")
    parser.add_argument("--threads", type=int, default=1, help="Engine threads (default: 1)")
    parser.add_argument("--hash", type=int, default=128, help="Hash table size in MB (default: 128)")

    args = parser.parse_args()

    engine_dir = Path(__file__).resolve().parent

    # Resolve engine path
    if args.engine_path:
        engine_path = Path(args.engine_path)
    else:
        engine_path = find_engine_binary(engine_dir)

    if engine_path is None or not engine_path.is_file():
        print("ERROR: Pikafish binary not found.", file=sys.stderr)
        print(f"  Run: bash {engine_dir / 'install.sh'}", file=sys.stderr)
        print(f"  Or download from https://github.com/official-pikafish/Pikafish/releases", file=sys.stderr)
        sys.exit(1)

    if not os.access(engine_path, os.X_OK):
        os.chmod(engine_path, 0o755)

    # Build position list
    if args.fen:
        positions = [{"fen": args.fen, "comment": ""}]
    else:
        filepath = args.file
        if not os.path.isabs(filepath):
            filepath = str(engine_dir / filepath)
        positions = load_positions(filepath)
        if not positions:
            print(f"No positions found in {filepath}", file=sys.stderr)
            sys.exit(1)

    # Start engine
    engine = PikafishCLI(str(engine_path), threads=args.threads, hash_mb=args.hash)
    try:
        engine.start()
    except Exception as exc:
        print(f"ERROR: Failed to start engine: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Pikafish ready. Analyzing {len(positions)} position(s) at depth {args.depth} ...\n",
          file=sys.stderr)

    results = []
    try:
        for i, pos in enumerate(positions):
            t0 = time.monotonic()
            result = engine.analyze(pos["fen"], depth=args.depth, multipv=args.multipv)
            elapsed = time.monotonic() - t0
            result["comment"] = pos.get("comment", "")
            result["time_s"] = round(elapsed, 2)
            results.append(result)

            # Progress on stderr
            score_str = ""
            if result["analysis"]:
                score_str = format_score(result["analysis"][0])
            print(f"  [{i + 1}/{len(positions)}] {result['bestmove'] or '?':6s}  "
                  f"{score_str:>8s}  ({elapsed:.1f}s)  {pos.get('comment', '')[:50]}",
                  file=sys.stderr)

            # Print human-readable to stdout if not writing JSON
            if not args.output:
                print_human(result, index=i)
    finally:
        engine.stop()

    # Write JSON output if requested
    if args.output:
        output_path = args.output
        if not os.path.isabs(output_path):
            output_path = str(engine_dir / output_path)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\nResults written to {output_path}", file=sys.stderr)

    print(f"\nDone. {len(results)} position(s) analyzed.", file=sys.stderr)


if __name__ == "__main__":
    main()
