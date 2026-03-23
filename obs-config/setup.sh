#!/usr/bin/env bash
#
# OBS Studio Scene Setup Script for Chinese Chess Content Creation
# Usage: ./obs-config/setup.sh
#

set -euo pipefail

# --- Configuration ---
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OBS_CONFIG_DIR="$HOME/Library/Application Support/obs-studio"
OBS_APP="/Applications/OBS.app"
OVERLAY_DIR="$PROJECT_DIR/overlays"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo ""
echo -e "${CYAN}╔══════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║  中国象棋 OBS Studio 场景配置                    ║${NC}"
echo -e "${CYAN}║  Chinese Chess OBS Scene Setup                   ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════╝${NC}"
echo ""

# --- Step 1: Check OBS installation ---
echo -e "${YELLOW}[1/5] 检查 OBS Studio 安装...${NC}"
if [ -d "$OBS_APP" ]; then
    echo -e "${GREEN}  ✓ OBS Studio found at $OBS_APP${NC}"
else
    echo -e "${RED}  ✗ OBS Studio not found at $OBS_APP${NC}"
    echo "  Please install OBS Studio first: https://obsproject.com/download"
    exit 1
fi

# --- Step 2: Create OBS config directories ---
echo -e "${YELLOW}[2/5] 创建 OBS 配置目录...${NC}"

mkdir -p "$OBS_CONFIG_DIR/basic/profiles/chess-landscape"
mkdir -p "$OBS_CONFIG_DIR/basic/profiles/chess-vertical"
mkdir -p "$OBS_CONFIG_DIR/basic/scenes"
echo -e "${GREEN}  ✓ OBS config directories created${NC}"

# --- Step 3: Copy profile configs ---
echo -e "${YELLOW}[3/5] 复制 Profile 配置文件...${NC}"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

cp "$SCRIPT_DIR/landscape-profile.ini" "$OBS_CONFIG_DIR/basic/profiles/chess-landscape/basic.ini"
echo -e "${GREEN}  ✓ Landscape profile (1920x1080) → chess-landscape${NC}"

cp "$SCRIPT_DIR/vertical-profile.ini" "$OBS_CONFIG_DIR/basic/profiles/chess-vertical/basic.ini"
echo -e "${GREEN}  ✓ Vertical profile (1080x1920) → chess-vertical${NC}"

# --- Step 4: Verify overlay files ---
echo -e "${YELLOW}[4/5] 验证覆层文件...${NC}"

OVERLAYS=(
    "stream-frame.html"
    "eval-bar.html"
    "player-info.html"
    "puzzle-challenge.html"
    "move-ticker.html"
    "subscriber-alert.html"
)

ALL_FOUND=true
for overlay in "${OVERLAYS[@]}"; do
    if [ -f "$OVERLAY_DIR/$overlay" ]; then
        echo -e "${GREEN}  ✓ $overlay${NC}"
    else
        echo -e "${RED}  ✗ $overlay (missing)${NC}"
        ALL_FOUND=false
    fi
done

if [ "$ALL_FOUND" = false ]; then
    echo -e "${YELLOW}  ⚠ Some overlay files are missing. Scenes using them may not display correctly.${NC}"
fi

# --- Step 5: Print manual scene setup instructions ---
echo -e "${YELLOW}[5/5] 场景设置指南...${NC}"
echo ""
echo -e "${CYAN}══════════════════════════════════════════════════${NC}"
echo -e "${CYAN}  OBS 场景需要在 GUI 中手动创建。请按以下步骤操作：${NC}"
echo -e "${CYAN}══════════════════════════════════════════════════${NC}"
echo ""

echo -e "${GREEN}--- Profile 选择 ---${NC}"
echo "  1. 打开 OBS → Profile → 选择 'chess-landscape' 或 'chess-vertical'"
echo ""

echo -e "${GREEN}--- 场景 1: 棋局分析 Board Analysis ---${NC}"
echo "  Profile: chess-landscape (1920x1080)"
echo "  1. Scenes 面板 → '+' → 命名: 棋局分析 Board Analysis"
echo "  2. Sources → '+' → Window Capture → 选择 board-art.html 或 explain.html 浏览器窗口"
echo "     - 尺寸: 1920x1080 (全屏)"
echo "  3. Sources → '+' → Audio Input Capture → 选择麦克风"
echo ""

echo -e "${GREEN}--- 场景 2: 残局挑战 Puzzle Challenge ---${NC}"
echo "  Profile: chess-landscape (1920x1080)"
echo "  1. Scenes → '+' → 命名: 残局挑战 Puzzle Challenge"
echo "  2. Sources → '+' → Window Capture → 选择棋盘浏览器窗口"
echo "     - 右键 → Transform → Edit Transform"
echo "     - Size: 1440x1080, Position: 0,0"
echo "  3. Sources → '+' → Browser"
echo "     - URL: file://$OVERLAY_DIR/puzzle-challenge.html"
echo "     - Width: 480, Height: 1080"
echo "     - 右键 → Transform → Position: 1440,0"
echo "  4. Sources → '+' → Audio Input Capture → 选择麦克风"
echo ""

echo -e "${GREEN}--- 场景 3: 直播对弈 Live Stream ---${NC}"
echo "  Profile: chess-landscape (1920x1080)"
echo "  1. Scenes → '+' → 命名: 直播对弈 Live Stream"
echo "  2. Sources → '+' → Window Capture → 棋盘"
echo "     - Size: 1280x1080, Position: 0,0"
echo "  3. Sources → '+' → Browser (直播边框)"
echo "     - URL: file://$OVERLAY_DIR/stream-frame.html"
echo "     - Width: 1920, Height: 1080, Position: 0,0"
echo "  4. Sources → '+' → Browser (评估条)"
echo "     - URL: file://$OVERLAY_DIR/eval-bar.html"
echo "     - Width: 40, Height: 1080, Position: 1280,0"
echo "  5. Sources → '+' → Browser (棋手信息)"
echo "     - URL: file://$OVERLAY_DIR/player-info.html"
echo "     - Width: 600, Height: 1080, Position: 1320,0"
echo "  6. (可选) Sources → '+' → Video Capture Device (摄像头)"
echo "     - Size: 320x240, Position: 1580,820"
echo "  7. Sources → '+' → Audio Input Capture → 选择麦克风"
echo ""

echo -e "${GREEN}--- 场景 4: 竖屏短视频 Vertical Short ---${NC}"
echo "  Profile: chess-vertical (1080x1920)"
echo "  ⚠ 先切换 Profile: Profile → chess-vertical"
echo "  1. Scenes → '+' → 命名: 竖屏短视频 Vertical Short"
echo "  2. Sources → '+' → Window Capture → 棋盘浏览器窗口"
echo "     - 右键 → Transform → Edit Transform"
echo "     - Crop: 裁剪为 1080x1080 正方形"
echo "     - Position: 0,420 (垂直居中)"
echo "  3. Sources → '+' → Audio Input Capture → 选择麦克风"
echo ""

echo -e "${CYAN}══════════════════════════════════════════════════${NC}"
echo -e "${CYAN}  配置完成! 详细说明请查看:${NC}"
echo -e "${CYAN}  $SCRIPT_DIR/README.md${NC}"
echo -e "${CYAN}  $SCRIPT_DIR/scenes.json${NC}"
echo -e "${CYAN}══════════════════════════════════════════════════${NC}"
echo ""

# --- Open OBS ---
read -p "是否现在打开 OBS Studio? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "正在启动 OBS Studio..."
    open "$OBS_APP"
fi

echo ""
echo -e "${GREEN}设置完成! Setup complete!${NC}"
