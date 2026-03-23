#!/usr/bin/env bash
# ============================================================================
# ChessDAO Setup Script
# Installs all dependencies and configures the project
# ============================================================================
set -euo pipefail

info()  { printf "\033[1;34m[棋]\033[0m  %s\n" "$*"; }
ok()    { printf "\033[1;32m[✓]\033[0m  %s\n" "$*"; }
warn()  { printf "\033[1;33m[!]\033[0m  %s\n" "$*"; }
fail()  { printf "\033[1;31m[✗]\033[0m  %s\n" "$*"; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo ""
echo "  棋道 ChessDAO — Xiangqi Creator Studio"
echo "  ========================================"
echo ""

# --- Python check ---
info "Checking Python..."
if command -v python3 &>/dev/null; then
    ok "Python $(python3 --version 2>&1 | cut -d' ' -f2) found"
else
    fail "Python 3 not found. Install from https://python.org"
    exit 1
fi

# --- Pikafish engine ---
info "Checking Pikafish engine..."
if [ -f engine/pikafish ] && [ -x engine/pikafish ]; then
    ok "Pikafish binary found"
else
    info "Installing Pikafish..."
    cd engine && bash install.sh && cd ..
fi

# Test engine
if [ -f engine/pikafish ]; then
    REPLY=$(echo -e "uci\nquit" | ./engine/pikafish 2>/dev/null | head -1)
    if echo "$REPLY" | grep -qi "pikafish"; then
        ok "Pikafish engine working"
    else
        warn "Pikafish binary exists but may not work on this platform"
    fi
fi

# --- OBS Studio ---
info "Checking OBS Studio..."
if [ -d "/Applications/OBS.app" ] || command -v obs &>/dev/null; then
    ok "OBS Studio installed"
else
    info "Installing OBS Studio..."
    if command -v brew &>/dev/null; then
        brew install --cask obs && ok "OBS installed"
    else
        warn "Install OBS manually from https://obsproject.com"
    fi
fi

# --- CapCut ---
info "Checking CapCut..."
if [ -d "/Applications/CapCut.app" ]; then
    ok "CapCut installed"
else
    info "Installing CapCut..."
    if command -v brew &>/dev/null; then
        brew install --cask capcut && ok "CapCut installed"
    else
        warn "Install CapCut manually from the App Store"
    fi
fi

# --- Shotcut (free video editor) ---
info "Checking Shotcut..."
if [ -d "/Applications/Shotcut.app" ]; then
    ok "Shotcut installed"
else
    info "Installing Shotcut..."
    if command -v brew &>/dev/null; then
        brew install --cask shotcut && ok "Shotcut installed"
    else
        warn "Install Shotcut manually from https://shotcut.org"
    fi
fi

# --- Verify HTML tools ---
info "Verifying HTML tools..."
TOOLS=(index.html dashboard.html board-art.html board3d.html board.html explain.html analyze.html games.html library.html calendar.html scripts.html analytics.html branding.html seo.html translate.html report.html)
MISSING=0
for tool in "${TOOLS[@]}"; do
    if [ ! -f "$tool" ]; then
        fail "Missing: $tool"
        MISSING=$((MISSING + 1))
    fi
done
if [ $MISSING -eq 0 ]; then
    ok "All ${#TOOLS[@]} HTML tools present"
else
    warn "$MISSING tools missing"
fi

# --- Verify overlays ---
info "Verifying OBS overlays..."
OVERLAYS=$(ls overlays/*.html 2>/dev/null | wc -l)
ok "$OVERLAYS OBS overlays found"

# --- Verify content ---
info "Verifying content scripts..."
SCRIPTS=$(find content -name "*.md" -o -name "*.txt" 2>/dev/null | wc -l)
ok "$SCRIPTS content files found"

# --- Verify positions ---
info "Verifying position library..."
POSITIONS=$(cat content/positions/*.txt engine/positions.txt 2>/dev/null | grep -c "^[a-zA-Z0-9]" || echo 0)
ok "$POSITIONS positions in library"

# --- Summary ---
echo ""
echo "  ========================================"
echo "  Setup Complete!"
echo "  ========================================"
echo ""
echo "  Next steps:"
echo "    1. Start engine:  cd engine && python3 server.py &"
echo "    2. Open studio:   open index.html"
echo "    3. Read launch:   cat LAUNCH.md"
echo ""
