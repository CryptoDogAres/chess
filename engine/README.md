# Pikafish Engine Integration

A lightweight local bridge that wraps the [Pikafish](https://github.com/official-pikafish/Pikafish) xiangqi (Chinese chess) engine, exposing it as a REST API for use with the board tool and other analysis workflows.

## Quick Start

```bash
# 1. Install Pikafish (auto-downloads the latest release)
bash install.sh

# 2. Start the analysis server
python3 server.py

# 3. Query the API
curl -X POST http://localhost:8080/analyze \
  -H "Content-Type: application/json" \
  -d '{"fen": "rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w", "depth": 20}'
```

## Setup

### 1. Download Pikafish

**Option A — Automatic (recommended):**

```bash
cd /Users/changchunshi/codebase/chess/engine
bash install.sh
```

**Option B — Manual:**

1. Go to <https://github.com/official-pikafish/Pikafish/releases>
2. Download the binary for your platform:
   - macOS Apple Silicon: `pikafish-aarch64-apple-darwin`
   - macOS Intel: `pikafish-x86_64-apple-darwin`
   - Linux x86_64: `pikafish-x86_64-linux`
3. Place the binary in this `engine/` folder
4. Make it executable: `chmod +x pikafish*`

### 2. Verify Installation

```bash
echo -e "uci\nquit" | ./pikafish*
```

You should see UCI engine identification lines and `uciok`.

### 3. Start the Analysis Server

```bash
python3 server.py
```

**Command-line options:**

| Flag             | Default   | Description                        |
|------------------|-----------|------------------------------------|
| `--port`         | `8080`    | HTTP server port                   |
| `--engine-path`  | auto      | Path to Pikafish binary            |
| `--threads`      | `1`       | Engine search threads              |
| `--hash`         | `128`     | Hash table size in MB              |

Example with custom settings:

```bash
python3 server.py --port 9090 --threads 4 --hash 512
```

## API Reference

### `POST /analyze`

Full position analysis with multiple principal variations.

**Request:**
```json
{
  "fen": "rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w",
  "depth": 20,
  "multipv": 3
}
```

**Response:**
```json
{
  "fen": "...",
  "depth": 20,
  "multipv": 3,
  "analysis": [
    {
      "pv_index": 1,
      "depth": 20,
      "score_cp": 35,
      "score_mate": null,
      "pv": "b2e2 h9g7 h0g2 ..."
    }
  ],
  "bestmove": "b2e2"
}
```

### `POST /bestmove`

Get the single best move for a position.

**Request:**
```json
{
  "fen": "rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w",
  "movetime": 2000
}
```

**Response:**
```json
{
  "fen": "...",
  "bestmove": "b2e2",
  "ponder": "h9g7"
}
```

### `GET /health`

Check engine status.

**Response:**
```json
{
  "status": "ok",
  "engine": "Pikafish",
  "threads": 1,
  "hash": 128
}
```

## CLI Batch Analysis

For offline batch analysis without running the server:

```bash
# Single position
python3 analyze.py --fen "rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w" --depth 20

# Batch from file
python3 analyze.py --file positions.txt --output results.json
```

## Using with the Board Tool

1. Start the server: `python3 server.py`
2. Open `board.html` in your browser
3. The board tool can call `http://localhost:8080/analyze` to get engine evaluation for the current position
4. CORS headers are enabled, so browser-based tools can query the API directly

## Pre-loaded Positions

The file `positions.txt` contains 20 famous xiangqi positions for testing and study, including:

- Starting position
- Famous game critical moments (from games.html)
- Endgame puzzles from "Erta of Elegant Interest" (适情雅趣)
- Tactical puzzles from "Secret Inside an Orange" (桔中秘)
- Classic checkmate patterns (马后炮, 天地炮, 闷宫, 铁门栓)

## Requirements

- Python 3.8+
- No external dependencies (stdlib only)
- Pikafish binary (downloaded via `install.sh` or manually)
