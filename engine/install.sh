#!/usr/bin/env bash
# ============================================================================
# Pikafish Installer
#
# Downloads the latest Pikafish release binary from GitHub, places it in
# this directory, and verifies it responds to UCI commands.
#
# Usage:
#   bash install.sh            # auto-detect OS and install
#   bash install.sh --help     # show usage info
# ============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="official-pikafish/Pikafish"
API_URL="https://api.github.com/repos/${REPO}/releases/latest"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

info()  { printf "\033[1;34m[INFO]\033[0m  %s\n" "$*"; }
ok()    { printf "\033[1;32m[OK]\033[0m    %s\n" "$*"; }
warn()  { printf "\033[1;33m[WARN]\033[0m  %s\n" "$*"; }
fail()  { printf "\033[1;31m[FAIL]\033[0m  %s\n" "$*"; exit 1; }

usage() {
    cat <<'USAGE'
Pikafish Installer

Downloads the latest Pikafish binary from GitHub and sets it up for use
with server.py and analyze.py.

Usage:
    bash install.sh [OPTIONS]

Options:
    --help          Show this help message
    --force         Overwrite existing binary if present
    --arch ARCH     Override architecture detection (aarch64 | x86_64)

Supported platforms:
    macOS  (Apple Silicon / Intel)
    Linux  (x86_64 / aarch64)

After installation the binary will be located at:
    <script_dir>/pikafish-<platform>

You can test it manually:
    echo -e "uci\nquit" | ./pikafish*

USAGE
    exit 0
}

# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

FORCE=0
ARCH_OVERRIDE=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --help|-h)   usage ;;
        --force)     FORCE=1; shift ;;
        --arch)      ARCH_OVERRIDE="$2"; shift 2 ;;
        *)           warn "Unknown option: $1"; shift ;;
    esac
done

# ---------------------------------------------------------------------------
# Detect platform
# ---------------------------------------------------------------------------

detect_platform() {
    local os arch

    case "$(uname -s)" in
        Darwin) os="apple-darwin" ;;
        Linux)  os="linux" ;;
        *)      fail "Unsupported OS: $(uname -s). Only macOS and Linux are supported." ;;
    esac

    if [[ -n "$ARCH_OVERRIDE" ]]; then
        arch="$ARCH_OVERRIDE"
    else
        case "$(uname -m)" in
            arm64|aarch64) arch="aarch64" ;;
            x86_64)        arch="x86_64" ;;
            *)             fail "Unsupported architecture: $(uname -m)" ;;
        esac
    fi

    echo "${arch}-${os}"
}

PLATFORM="$(detect_platform)"
info "Detected platform: ${PLATFORM}"

# ---------------------------------------------------------------------------
# Check for existing binary
# ---------------------------------------------------------------------------

EXISTING=$(find "$SCRIPT_DIR" -maxdepth 1 -name "pikafish*" -o -name "Pikafish*" 2>/dev/null | head -1 || true)
# Filter out our own scripts
for f in $EXISTING; do
    case "$f" in
        *.py|*.sh|*.txt|*.md|*.json) EXISTING="" ;;
    esac
done

if [[ -n "$EXISTING" && "$FORCE" -eq 0 ]]; then
    ok "Pikafish binary already exists: $EXISTING"
    info "Use --force to re-download."
    exit 0
fi

# ---------------------------------------------------------------------------
# Fetch latest release info from GitHub API
# ---------------------------------------------------------------------------

info "Fetching latest release info from GitHub..."

if command -v curl &>/dev/null; then
    RELEASE_JSON=$(curl -sL "$API_URL")
elif command -v wget &>/dev/null; then
    RELEASE_JSON=$(wget -qO- "$API_URL")
else
    fail "Neither curl nor wget found. Please install one of them."
fi

# Extract tag name
TAG_NAME=$(echo "$RELEASE_JSON" | python3 -c "
import sys, json
data = json.load(sys.stdin)
print(data.get('tag_name', ''))
" 2>/dev/null || true)

if [[ -z "$TAG_NAME" ]]; then
    fail "Could not determine latest release tag. GitHub API response may have changed or rate-limited."
fi

info "Latest release: ${TAG_NAME}"

# ---------------------------------------------------------------------------
# Find the download URL for our platform
# ---------------------------------------------------------------------------

DOWNLOAD_URL=$(echo "$RELEASE_JSON" | python3 -c "
import sys, json
data = json.load(sys.stdin)
platform = '${PLATFORM}'
for asset in data.get('assets', []):
    name = asset['name'].lower()
    # Match platform string in asset name
    if platform.replace('-', '') in name.replace('-', '').replace('_', ''):
        print(asset['browser_download_url'])
        break
    # Fallback: check individual components
    parts = platform.split('-')
    if all(p in name for p in parts):
        print(asset['browser_download_url'])
        break
" 2>/dev/null || true)

if [[ -z "$DOWNLOAD_URL" ]]; then
    warn "Could not find a pre-built binary for platform: ${PLATFORM}"
    info "Available assets:"
    echo "$RELEASE_JSON" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for asset in data.get('assets', []):
    print('  -', asset['name'], ':', asset['browser_download_url'])
" 2>/dev/null || true
    echo ""
    info "Please download manually from:"
    info "  https://github.com/${REPO}/releases/tag/${TAG_NAME}"
    info "Then place the binary in: ${SCRIPT_DIR}"
    exit 1
fi

# Derive output filename
BINARY_NAME=$(basename "$DOWNLOAD_URL")
OUTPUT_PATH="${SCRIPT_DIR}/${BINARY_NAME}"

info "Downloading: ${BINARY_NAME}"
info "URL: ${DOWNLOAD_URL}"

# ---------------------------------------------------------------------------
# Download
# ---------------------------------------------------------------------------

if command -v curl &>/dev/null; then
    curl -L --progress-bar -o "$OUTPUT_PATH" "$DOWNLOAD_URL"
elif command -v wget &>/dev/null; then
    wget --show-progress -O "$OUTPUT_PATH" "$DOWNLOAD_URL"
fi

if [[ ! -f "$OUTPUT_PATH" ]]; then
    fail "Download failed. File not found at ${OUTPUT_PATH}"
fi

# Handle compressed archives
case "$BINARY_NAME" in
    *.tar.gz|*.tgz)
        info "Extracting tar.gz archive..."
        tar -xzf "$OUTPUT_PATH" -C "$SCRIPT_DIR"
        rm -f "$OUTPUT_PATH"
        # Find the extracted binary
        OUTPUT_PATH=$(find "$SCRIPT_DIR" -maxdepth 2 -type f \( -name "pikafish*" -o -name "Pikafish*" \) ! -name "*.py" ! -name "*.sh" ! -name "*.txt" ! -name "*.md" ! -name "*.json" | head -1)
        ;;
    *.zip)
        info "Extracting zip archive..."
        unzip -o "$OUTPUT_PATH" -d "$SCRIPT_DIR"
        rm -f "$OUTPUT_PATH"
        OUTPUT_PATH=$(find "$SCRIPT_DIR" -maxdepth 2 -type f \( -name "pikafish*" -o -name "Pikafish*" \) ! -name "*.py" ! -name "*.sh" ! -name "*.txt" ! -name "*.md" ! -name "*.json" | head -1)
        ;;
esac

if [[ -z "$OUTPUT_PATH" || ! -f "$OUTPUT_PATH" ]]; then
    fail "Could not locate binary after extraction."
fi

# ---------------------------------------------------------------------------
# Make executable & test
# ---------------------------------------------------------------------------

chmod +x "$OUTPUT_PATH"
info "Binary: ${OUTPUT_PATH}"
info "Testing UCI handshake..."

UCI_RESPONSE=$(echo -e "uci\nquit" | "$OUTPUT_PATH" 2>/dev/null | head -20 || true)

if echo "$UCI_RESPONSE" | grep -q "uciok"; then
    ok "Pikafish is working!"
    echo ""
    echo "$UCI_RESPONSE" | head -5
    echo ""
    ok "Installation complete. Binary: ${OUTPUT_PATH}"
    echo ""
    info "Next steps:"
    info "  Start server:  python3 ${SCRIPT_DIR}/server.py"
    info "  CLI analysis:  python3 ${SCRIPT_DIR}/analyze.py --fen \"rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w\" --depth 20"
else
    warn "UCI handshake did not return 'uciok'. The binary may not be compatible with your system."
    warn "Response was:"
    echo "$UCI_RESPONSE"
    echo ""
    info "You may need to download a different build from:"
    info "  https://github.com/${REPO}/releases/tag/${TAG_NAME}"
    exit 1
fi
