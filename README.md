# 棋道 ChessDAO — Xiangqi Creator Studio

The ultimate toolkit for building a Chinese Chess (象棋/Xiangqi) commentary channel across Douyin, Bilibili, and YouTube.

## What's Inside

### 16 HTML Tools (zero dependencies, open in browser)

| Tool | File | Description |
|------|------|-------------|
| **Landing Page** | `index.html` | Premium SaaS-style entry page with animated hero |
| **Dashboard** | `dashboard.html` | Founder's task tracker — 107 tasks across 13 plans |
| **Art Board** | `board-art.html` | Museum-quality board — 4 woods (紫檀/黄花梨/金丝楠/乌木), 3 piece materials (jade/rosewood/bronze), Gallery Mode |
| **3D Board** | `board3d.html` | CSS 3D board with camera controls, 4 visual themes |
| **Analysis Board** | `board.html` | Standard board with drag-drop, FEN input, annotations |
| **Play & Explain** | `explain.html` | Interactive YouTube-style presenter — board animates moves while commentary scrolls. "Copy for MiniMax" TTS export |
| **Position Analysis** | `analyze.html` | Pikafish-powered analysis — detects 14 tactical/positional patterns, explains WHY moves are good/bad |
| **Game Database** | `games.html` | 14 famous games with board replay, key moments, "Export for Commentary" |
| **Script Library** | `library.html` | Browse all 35 scripts with search, "Copy for MiniMax" one-click TTS export |
| **Content Calendar** | `calendar.html` | Multi-platform publishing scheduler with 5-7 video/week cadence tracking |
| **Script Generator** | `scripts.html` | 4 commentary templates (Xu Yinchuan method), CN+EN phrase library |
| **Analytics** | `analytics.html` | Multi-platform metrics — canvas charts, milestones, video performance log |
| **Branding Kit** | `branding.html` | Logo (4 styles), banners (YouTube/Bilibili/Douyin), 6 thumbnail templates — all downloadable as PNG |
| **SEO Tools** | `seo.html` | 105 keywords, title generator (3 platforms), title analyzer, hashtag manager |
| **Translator** | `translate.html` | 200-term CN↔EN xiangqi dictionary, SRT subtitle generator, move notation translator |
| **Report** | `report.html` | Full market research — competitors, revenue models, growth strategies |

> Every tool supports **中文 / EN / 双语** language toggle and has premium Chinese typography (LXGW WenKai, Noto Serif SC, Ma Shan Zheng).

### 6 OBS Streaming Overlays (`overlays/`)
Eval bar, player info, move ticker, puzzle countdown, subscriber alert, full stream frame.

### Pikafish Engine Integration (`engine/`)
REST API server wrapping the Pikafish xiangqi engine (Elo 3951).

### 105+ Famous Positions (`content/positions/`)
Classic endgames, tournament moments, tactical puzzles, opening theory.

### 35 Ready-to-Record Scripts (`content/`)
- 10 endgame puzzle scripts
- 5 famous game commentaries
- 12 beginner tutorial outlines
- 3 series pilot scripts
- 5 YouTube production packages

### Complete Production Guides (`content/platform-guides/`)
Douyin, Bilibili, YouTube setup guides, MiniMax voiceover workflow, editing guides, SEO optimization.

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/changchunshi/chess.git
cd chess

# 2. Install dependencies and Pikafish engine
./setup.sh

# 3. Start the engine server
cd engine && python3 server.py &

# 4. Open the dashboard
open index.html
```

## Setup Options

### Automatic (recommended)
```bash
./setup.sh
```

### Manual
```bash
# Install Pikafish engine
cd engine && bash install.sh

# Start engine server
python3 engine/server.py --port 8080 --threads 4 --hash 256

# Open any HTML file in your browser
open dashboard.html
```

### Python Project Manager (`manage.py`)
```bash
python3 manage.py setup     # Install Pikafish engine + verify all 16 tools
python3 manage.py serve     # Start engine server on localhost:8080
python3 manage.py analyze   # Batch analyze all 105+ positions
python3 manage.py status    # Show project progress (84/107 tasks)
python3 manage.py open      # Open landing page in browser
python3 manage.py open dashboard.html  # Open any specific tool
python3 manage.py export    # Export all plans as JSON
```

### npm Scripts (`package.json`)
```bash
npm start          # Open landing page
npm run dashboard  # Open founder's dashboard
npm run engine     # Start Pikafish server (port 8080, 4 threads)
npm run analyze    # Batch analyze preset positions
npm run setup      # Run full setup (engine + apps)
npm run status     # Show project progress
npm run serve      # Local HTTP server on port 3000
```

## Tech Stack

- **Board rendering**: Canvas API + CSS 3D transforms
- **Engine**: Pikafish 2026 (NNUE, Elo 3951)
- **Fonts**: LXGW WenKai, Noto Serif SC, Ma Shan Zheng
- **Voiceover**: MiniMax AI TTS (external)
- **Video editing**: OBS Studio, CapCut, Shotcut
- **Analytics**: localStorage-based tracking
- **Zero external JS dependencies** — all tools are self-contained HTML

## Project Structure

```
chess/
├── index.html              # Landing page
├── dashboard.html          # Task tracker
├── board-art.html          # Art board (premium)
├── board3d.html            # 3D board
├── board.html              # Standard board
├── explain.html            # Play & Explain presenter
├── analyze.html            # Position analysis
├── games.html              # Game database
├── library.html            # Script library viewer
├── calendar.html           # Content calendar
├── scripts.html            # Script generator
├── analytics.html          # Analytics tracker
├── branding.html           # Branding kit
├── seo.html                # SEO tools
├── translate.html          # Translator
├── report.html             # Research report
├── LAUNCH.md               # 14-day go-live checklist
├── setup.sh                # Auto-setup script
├── manage.py               # Python project manager
├── requirements.txt        # Python dependencies
├── package.json            # npm package info
├── engine/
│   ├── server.py           # Pikafish REST API
│   ├── analyze.py          # Batch analysis CLI
│   ├── install.sh          # Engine installer
│   └── positions.txt       # 20 preset positions
├── overlays/               # 6 OBS streaming overlays
├── obs-config/             # OBS scene configs
├── plans/                  # 13 plan tracking JSONs
└── content/
    ├── puzzles/            # 10 puzzle scripts
    ├── famous-games/       # 5 game commentary scripts
    ├── tutorials/          # 12 tutorial scripts + positions
    ├── series/             # 3 series pilot scripts
    ├── youtube/            # YouTube production package
    ├── positions/          # 85 famous positions
    ├── platform-guides/    # Platform & production guides
    ├── growth/             # Growth strategy guides
    ├── revenue/            # Monetization plans
    └── community/          # Community setup templates
```

## License

MIT

## Credits

- **Pikafish** — Open-source Xiangqi engine ([pikafish.com](https://pikafish.com))
- **LXGW WenKai** — Beautiful Chinese font ([GitHub](https://github.com/lxgw/LxgwWenKai))
- Built with [Claude Code](https://claude.ai/code)
