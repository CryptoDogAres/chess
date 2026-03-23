# OBS Studio 场景配置指南 / OBS Scene Setup Guide

本目录包含为中国象棋内容创作预配置的 OBS Studio 场景和配置文件。

## 快速开始 / Quick Start

1. 运行设置脚本:
   ```bash
   chmod +x obs-config/setup.sh
   ./obs-config/setup.sh
   ```

2. 或手动按照以下步骤操作。

---

## 导入配置 / Importing Profiles

OBS 不支持直接导入 JSON 场景文件，但可以导入 Profile（配置文件）：

### 导入 Profile（推荐设置）

1. 打开 OBS Studio
2. 菜单栏 → **Profile** → **Import**
3. 选择本目录中的 `.ini` 文件所在文件夹
4. 两个 Profile 可用：
   - `landscape-profile.ini` — 横屏 1920x1080（分析视频、直播）
   - `vertical-profile.ini` — 竖屏 1080x1920（短视频）

### 手动创建 Profile

如果导入不生效，可手动设置：

1. **Profile** → **New** → 命名为 "象棋横屏" 或 "象棋竖屏"
2. **Settings** → **Video**:
   - 横屏: Base 1920x1080, Output 1920x1080
   - 竖屏: Base 1080x1920, Output 1080x1920
3. **Settings** → **Output**:
   - Output Mode: Advanced
   - Encoder: x264 (H.264)
   - Rate Control: CBR
   - Bitrate: 6000 Kbps
   - Keyframe Interval: 2
4. **Settings** → **Audio**:
   - Sample Rate: 48 kHz
   - Audio Bitrate: 160 Kbps (AAC)

---

## 推荐设置 / Recommended Settings

| 参数 | 值 |
|------|------|
| 分辨率 (横屏) | 1920x1080 |
| 分辨率 (竖屏) | 1080x1920 |
| 帧率 | 30 FPS |
| 编码器 | H.264 (x264) |
| 码率控制 | CBR |
| 视频码率 | 6000 Kbps |
| 音频采样率 | 48 kHz |
| 音频码率 | 160 Kbps AAC |
| 关键帧间隔 | 2 秒 |
| CPU 预设 | veryfast（直播）/ medium（录制） |

---

## 场景设置 / Scene Setup

请参考 `scenes.json` 中的详细配置。以下是四个场景的快速指南：

### 场景 1: 棋局分析 Board Analysis（横屏）

用途：录制棋局分析和讲解视频。

1. 新建场景，命名为 "棋局分析 Board Analysis"
2. 添加 **Window Capture** 源：
   - 选择浏览器窗口（打开 board-art.html 或 explain.html）
   - 尺寸: 1920x1080，全屏
3. 添加 **Audio Input Capture** 源：
   - 选择麦克风设备

### 场景 2: 残局挑战 Puzzle Challenge（横屏）

用途：互动残局挑战视频，带倒计时功能。

1. 新建场景，命名为 "残局挑战 Puzzle Challenge"
2. 添加 **Window Capture** 源（棋盘）:
   - 尺寸: 1440x1080，位置 (0, 0)
3. 添加 **Browser** 源（挑战覆层）:
   - URL: `file:///Users/changchunshi/codebase/chess/overlays/puzzle-challenge.html`
   - 宽: 480, 高: 1080, 位置 (1440, 0)
4. 添加 **Audio Input Capture** 源

### 场景 3: 直播对弈 Live Stream（横屏）

用途：在抖音/B站直播下棋。

1. 新建场景，命名为 "直播对弈 Live Stream"
2. 添加 **Window Capture** 源（棋盘）:
   - 尺寸: 1280x1080，位置 (0, 0)
3. 添加 **Browser** 源（直播边框）:
   - URL: `file:///Users/changchunshi/codebase/chess/overlays/stream-frame.html`
   - 宽: 1920, 高: 1080（全屏覆层）
4. 添加 **Browser** 源（评估条）:
   - URL: `file:///Users/changchunshi/codebase/chess/overlays/eval-bar.html`
   - 宽: 40, 高: 1080, 位置 (1280, 0)
5. 添加 **Browser** 源（棋手信息）:
   - URL: `file:///Users/changchunshi/codebase/chess/overlays/player-info.html`
   - 宽: 600, 高: 1080, 位置 (1320, 0)
6. 可选：添加 **Video Capture Device**（摄像头）:
   - 尺寸: 320x240，位置 (1580, 820)

### 场景 4: 竖屏短视频 Vertical Short（竖屏）

用途：录制抖音/YouTube Shorts 竖屏短视频。

1. 先切换 Profile 到竖屏（1080x1920）
2. 新建场景，命名为 "竖屏短视频 Vertical Short"
3. 添加 **Window Capture** 源（棋盘）:
   - 裁剪为 1080x1080 正方形
   - 位置: (0, 420) 居中
4. 添加 **Audio Input Capture** 源

---

## 添加 HTML 覆层为 Browser Source

所有覆层文件位于 `overlays/` 目录：

1. 在 OBS 场景中点击 "+" 添加源
2. 选择 **Browser**
3. 勾选 **Local file** 或输入文件 URL：
   ```
   file:///Users/changchunshi/codebase/chess/overlays/stream-frame.html
   file:///Users/changchunshi/codebase/chess/overlays/eval-bar.html
   file:///Users/changchunshi/codebase/chess/overlays/player-info.html
   file:///Users/changchunshi/codebase/chess/overlays/puzzle-challenge.html
   file:///Users/changchunshi/codebase/chess/overlays/move-ticker.html
   file:///Users/changchunshi/codebase/chess/overlays/subscriber-alert.html
   ```
4. 设置宽度和高度（参考 scenes.json 中的具体尺寸）
5. 确保勾选 **Refresh browser when scene becomes active**
6. 可选：添加 Custom CSS 来微调样式

### Browser Source 参数示例

部分覆层支持 URL 参数，可在 URL 后添加：
```
file:///path/to/overlay.html?param1=value1&param2=value2
```

---

## 文件说明

| 文件 | 用途 |
|------|------|
| `scenes.json` | 四个场景的详细配置（源、尺寸、位置） |
| `landscape-profile.ini` | 横屏 1080p Profile 配置 |
| `vertical-profile.ini` | 竖屏 1080x1920 Profile 配置 |
| `setup.sh` | 自动设置脚本 |

---

## 故障排除

- **Browser Source 显示空白**: 确保 HTML 文件路径正确，使用 `file:///` 协议
- **Window Capture 黑屏**: macOS 需要在系统设置中授权 OBS 屏幕录制权限
  - 系统设置 → 隐私与安全 → 屏幕录制 → 勾选 OBS
- **音频无声**: 检查 Audio Input Capture 是否选择了正确的麦克风设备
- **竖屏裁剪不正确**: 确保已切换到竖屏 Profile（1080x1920）
