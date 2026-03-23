# 剪映/CapCut Editing Workflow for Xiangqi Short Videos

This guide covers the complete editing workflow for producing Xiangqi puzzle and
tactics short videos using CapCut (international) or 剪映 (Chinese version). The
workflow is optimized for Douyin and YouTube Shorts vertical video (9:16 aspect
ratio, under 60 seconds).

> **Which version should I use?** If you publish primarily on Douyin, use 剪映
> (Jianying). It integrates directly with Douyin for one-tap publishing and has
> Chinese-optimized auto-captions. If you publish on YouTube Shorts or TikTok,
> use CapCut. The interface is nearly identical; this guide provides menu paths
> for both.

---

## 1. Import Footage

Your raw material comes from OBS screen recordings of board-art.html (see the
OBS recording guide for capture settings).

**CapCut (English):**
1. Open CapCut and tap **New Project**.
2. Select your screen recording file from your device or import from a folder.
3. Tap **Add** to place it on the timeline.

**剪映 (中文):**
1. 打开剪映，点击 **开始创作**。
2. 从相册或文件夹中选择 OBS 录屏文件。
3. 点击 **添加** 将素材放入时间线。

**Tips:**
- Record in 1080x1920 (portrait) directly from OBS if possible. If you recorded
  in landscape (1920x1080), you will need to crop or reframe in step 2.
- Keep original files organized: one folder per puzzle episode, named
  `puzzle-001-raw.mp4`, `puzzle-002-raw.mp4`, etc.

---

## 2. Trim and Cut

Remove dead air, false starts, long pauses, and any off-topic segments. Puzzle
videos must be tight — every second counts on Douyin and Shorts.

**CapCut:** Select the clip on the timeline. Drag the white handles at the start
and end to trim. To split mid-clip, move the playhead to the desired frame and
tap **Split** (scissors icon in the toolbar).

**剪映:** 选中时间线上的片段，拖动两端白色手柄裁剪。若要在中间分割，将播放头
移到目标帧，点击工具栏中的 **分割**（剪刀图标）。

**What to cut:**
- Any pause longer than 1.5 seconds (puzzle videos should feel fast-paced).
- False starts where you restart a sentence.
- Setup time where pieces are being arranged — speed this up instead (see step
  7) or cut it entirely.
- End-of-recording dead space after the puzzle is solved.

**Target duration:** 30-45 seconds for Douyin, 30-58 seconds for YouTube Shorts.

---

## 3. Auto-Captions (自动字幕)

Captions are mandatory for short video. Most viewers watch without sound, and
Chinese character recognition is strong in both CapCut and 剪映.

**CapCut (English):**
1. Tap **Text** in the bottom toolbar.
2. Tap **Auto captions**.
3. Select language: **Mandarin Chinese** (or **Bilingual** if you narrate in
   both Chinese and English).
4. Tap **Generate**. Wait for processing.
5. Review every caption segment for accuracy.

**剪映 (中文):**
1. 点击底部工具栏的 **文字**。
2. 点击 **识别字幕** 或 **智能字幕**。
3. 选择语言：**中文**（或 **中英双语**）。
4. 点击 **开始识别**，等待处理完成。
5. 逐条检查字幕准确性。

**Caption styling:**
- Font: **Bold** (CapCut: select a bold font like "HeiTi Bold"; 剪映: 选择
  "黑体加粗" 或 "思源黑体 Bold")
- Color: **White** with **black outline** (stroke width 3-4px)
- Size: **48px minimum** (larger is better on mobile screens)
- Position: **Bottom 1/3** of the screen. Avoid the very bottom edge — Douyin
  and Shorts overlay UI elements there. Leave roughly 15% margin from the
  bottom.
- Background: Optional semi-transparent black background box behind text for
  extra readability.

**Common recognition errors to watch for:**
- Chess piece names: 车 (chē) vs 砗 (chē), 炮 (pào) vs 泡 (pào)
- Xiangqi terminology: 将军 (jiāngjūn, check) vs 将军 (jiāngjūn, general)
- Move notation: numbers and directional terms often get garbled

Review every segment. Tap on a caption block to edit text directly.

---

## 4. Bold Text Overlays

Text overlays are the visual hooks that keep viewers watching. Add them at key
moments throughout the video.

**CapCut:** Tap **Text** > **Add text**. Type your overlay text. Adjust font,
size, color, and position. Drag the text block on the timeline to control when
it appears and for how long.

**剪映:** 点击 **文字** > **新建文本**。输入文字内容，调整字体、大小、颜色和
位置。在时间线上拖动文字块控制出现时间和持续时间。

**Key overlays to add:**

| Moment | Overlay Text | Style |
|--------|-------------|-------|
| Wrong move shown | 错！ | Red, 72px, with shake animation |
| Correct answer | 对！ | Green, 72px, with bounce animation |
| Viewer pause | 暂停！想一想 | Yellow, 64px, centered |
| Episode number | 第42期 每日一题 | White, 48px, top-left corner |
| Series title | 象棋杀法训练 | White, 40px, below episode number |
| Difficulty rating | 难度：3/5 | Orange, 36px, top-right corner |

**Recommended text animations:**

- **CapCut:** Select the text layer, tap **Animation**, then choose from **In
  animations**. Recommended: **Typewriter** (打字机), **Bounce** (弹跳),
  **Fade In** (淡入), **Scale Up** (放大).
- **剪映:** 选中文字层，点击 **动画**，选择 **入场动画**。推荐：**打字机**、
  **弹跳**、**淡入**、**放大**。

**Duration:** Overlays should appear for 1.5-3 seconds. The "暂停！想一想" pause
overlay should last 3-5 seconds to give the viewer time to think.

---

## 5. Transitions

Keep transitions simple. Chess content should feel clean and focused.

**Recommended:**
- **Hard cut** (no transition) between puzzle positions — this is the default
  and almost always the best choice.
- **Quick fade** (0.2-0.3 seconds) when transitioning between the intro hook and
  the puzzle setup.
- **Cross dissolve** (0.3 seconds) only for the final reveal of the solution.

**Avoid:** Spinning transitions, page curls, 3D flips, glitch effects, or any
transition that draws attention to itself rather than the chess content.

**CapCut:** Tap the junction between two clips on the timeline. A small white
square appears. Tap it and select a transition. Adjust duration.

**剪映:** 点击时间线上两个片段之间的连接处，出现白色小方块，点击选择转场效果，
调整持续时间。

---

## 6. Background Music

Music is optional for puzzle videos. If you add it, keep it low and
unobtrusive.

**Recommended music types:**
- Chinese instrumental (guzheng, erhu, pipa) — fits the cultural context
- Lo-fi ambient — unobtrusive, modern feel
- No lyrics — vocal music competes with narration

**Volume level:** 10-15% of the main audio track. The voiceover must always be
clearly dominant.

**CapCut:** Tap **Audio** > **Music** > browse CapCut's built-in library. Search
for "Chinese" or "Traditional." After adding, select the music track on the
timeline and drag the volume slider to 10-15%.

**剪映:** 点击 **音频** > **音乐** > 浏览剪映内置曲库。搜索"中国风"或"古典"。
添加后选中音乐轨道，将音量滑块调至 10-15%。

**Important:** Both CapCut and 剪映 have royalty-free music libraries. Use these
to avoid copyright strikes. Do not use popular songs.

---

## 7. Speed Ramping

Speed ramping keeps the video dynamic. Speed up boring parts and maintain normal
speed (or even slow down) for critical analysis moments.

**What to speed up (2x-4x):**
- Piece setup and initial board arrangement
- Obvious recaptures or forced sequences
- Resetting the board between variations

**What to keep at normal speed (1x):**
- The key tactical move (the "aha" moment)
- Your explanation of why a move works
- The viewer pause segment

**CapCut:** Select the clip. Tap **Speed** in the bottom toolbar. Choose
**Normal** for constant speed change, or **Curve** for smooth speed ramping.
Under **Curve**, select a preset like **Montage** or **Hero**, or tap **Custom**
to create your own ramp.

**剪映:** 选中片段，点击底部的 **变速**。选择 **常规变速** 进行整体加减速，或
选择 **曲线变速** 进行平滑的速度曲线调整。在曲线变速中可选预设或 **自定义**
创建自己的变速曲线。

---

## 8. Export Settings

Correct export settings ensure your video looks sharp on every platform.

### Douyin Export

**CapCut / 剪映:**
1. Tap the **Export** button (top-right corner, arrow icon).
2. Resolution: **1080p** (1080x1920)
3. Frame rate: **30fps**
4. Quality: **High** or **Recommended** (剪映: 推荐)

- **CapCut:** Settings > Export > Resolution 1080p, Frame Rate 30.
- **剪映:** 导出页面 > 分辨率 1080p，帧率 30。

### YouTube Shorts Export

Same specifications as Douyin: 1080x1920, 30fps, high quality. YouTube Shorts
accepts the same vertical video format.

### Watermark Removal

Both CapCut and 剪映 may add a default ending watermark or logo.

- **CapCut:** Go to **Settings** (gear icon) > toggle off **CapCut ending** or
  **Watermark**. On some versions, you can simply delete the auto-added ending
  clip from the timeline.
- **剪映:** 进入 **设置**（齿轮图标）> 关闭 **片尾水印** 或 **剪映片尾**。
  也可以直接在时间线末尾删除自动添加的片尾片段。

**File naming convention:** `puzzle-[number]-[platform]-final.mp4`
- Example: `puzzle-042-douyin-final.mp4`

---

## 9. Create a Reusable Template

Once you have edited one video to your satisfaction, save it as a template to
speed up future episodes.

**CapCut (English):**
1. With your completed project open, tap the three-dot menu (**...**) or
   **More** in the project screen.
2. Select **Save as template** (if available in your version).
3. Alternatively, duplicate the project: go back to the project list, long-press
   the project, and tap **Duplicate**. Rename it "Puzzle Template." For each new
   episode, duplicate this template project and swap out the footage.

**剪映 (中文):**
1. 打开已完成的项目，点击右上角的 **更多**（三个点）或返回项目列表。
2. 长按项目，选择 **复制项目**，重命名为"每日一题模板"。
3. 每次制作新一期时，复制模板项目，替换素材即可。

**What the template should contain:**
- Episode number text overlay (positioned, styled, animated — just change the
  number)
- Series title overlay (static across episodes)
- Difficulty rating overlay (change the number)
- "暂停！想一想" pause overlay (pre-timed, pre-animated)
- "错！" and "对！" overlays (pre-styled, ready to be repositioned on the
  timeline)
- Background music track (already set to 10-15% volume)
- Auto-caption style preset (font, color, size, position saved)
- Empty V1 track ready for new footage

Using the template, a new puzzle video should take 10-15 minutes to edit rather
than 30-45 minutes.

---

## Quick Reference: Complete Editing Checklist

Use this checklist for every puzzle video before export:

- [ ] Raw footage imported and trimmed (no dead air, under 60 seconds)
- [ ] Auto-captions generated and reviewed for accuracy
- [ ] Caption style: bold white, black outline, 48px+, bottom 1/3
- [ ] Episode number and series title overlays added
- [ ] "暂停！想一想" pause overlay at the right moment
- [ ] "错！" and "对！" overlays for wrong/correct moves
- [ ] Difficulty rating shown
- [ ] Repetitive sections sped up (2x-4x)
- [ ] Key moments at normal speed or slightly slowed
- [ ] Background music at 10-15% volume (if used)
- [ ] Transitions: simple cuts only, no fancy effects
- [ ] Exported at 1080x1920, 30fps, high quality
- [ ] CapCut/剪映 watermark disabled
- [ ] File named correctly: `puzzle-[number]-[platform]-final.mp4`

---

## Keyboard Shortcuts (Desktop Versions)

If you use CapCut or 剪映 on desktop, these shortcuts accelerate editing:

| Action | CapCut (Mac/PC) | 剪映 (Mac/PC) |
|--------|----------------|---------------|
| Split clip | Ctrl/Cmd + B | Ctrl/Cmd + B |
| Delete clip | Delete/Backspace | Delete/Backspace |
| Undo | Ctrl/Cmd + Z | Ctrl/Cmd + Z |
| Play/Pause | Space | Space |
| Zoom timeline in | Ctrl/Cmd + = | Ctrl/Cmd + = |
| Zoom timeline out | Ctrl/Cmd + - | Ctrl/Cmd + - |
| Add text | T | T |
| Export | Ctrl/Cmd + E | Ctrl/Cmd + E |

---

## Troubleshooting Common Issues

**Auto-captions are inaccurate for chess terms:**
Manually edit each caption. Build a personal dictionary of common terms you use
(将军, 绝杀, 闷宫, 双车错) so you can quickly spot and fix errors.

**Video looks blurry on Douyin:**
Ensure you export at 1080p, not 720p. Also check that the original OBS recording
was at 1080x1920 resolution. Douyin re-compresses uploads, so starting with
maximum quality is important.

**Text overlays are cut off on some phones:**
Keep all text within the "safe zone" — roughly 90% of the screen width and avoid
the top 10% and bottom 15% of the screen. Both CapCut and 剪映 show safe zone
guides when you enable them in settings.

**App crashes with long recordings:**
Split long recordings into shorter segments before importing. CapCut mobile
handles clips under 5 minutes best. For longer content, use the desktop version
or switch to Premiere Pro (see premiere-editing-guide.md).
