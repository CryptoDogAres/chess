# Premiere Pro Editing Workflow for Long-Form Xiangqi Analysis

This guide covers the complete Adobe Premiere Pro workflow for editing 10-30
minute Xiangqi game analysis videos. These videos are published primarily on
YouTube and Bilibili, where longer-form educational content performs well.

Long-form analysis videos require a more structured editing approach than short
puzzle clips. You will work with multiple video and audio tracks, engine
evaluation overlays, annotations, and chapter markers.

---

## 1. Project Setup

### Create a New Project

1. Open Premiere Pro. Select **New Project** (File > New > Project).
2. Name the project using the convention: `game-analysis-[date]-[players].prproj`
   - Example: `game-analysis-2026-03-15-wang-vs-zheng.prproj`
3. Set the project location to your working folder.

### Sequence Settings

1. Go to **File > New > Sequence** (or Ctrl/Cmd + N).
2. Under the **Settings** tab, configure manually:
   - **Editing Mode:** Custom
   - **Timebase:** 30 frames/second
   - **Frame Size:** 1920 horizontal x 1080 vertical
   - **Pixel Aspect Ratio:** Square Pixels (1.0)
   - **Fields:** No Fields (Progressive Scan)
   - **Preview File Format:** I-Frame Only MPEG
3. Name the sequence: `main-edit`
4. Click **OK**.

Alternatively, select the **Digital SLR > 1080p > DSLR 1080p30** preset and
adjust if needed.

### Folder Structure in the Project Panel

Organize your Project panel (bottom-left) with bins (folders):

```
project-root/
  Footage/        — OBS screen recordings, webcam footage
  Audio/          — Voiceover narration files, music tracks
  Graphics/       — Text overlays, lower thirds, eval bar assets
  SRT/            — Subtitle files from translate.html
  Exports/        — Final rendered files (set as export destination)
```

Right-click in the Project panel > **New Bin** to create each folder. Drag
imported files into the appropriate bins.

---

## 2. Multi-Track Timeline Layout

A well-organized timeline makes complex edits manageable. Use this track
layout consistently across all analysis videos.

### Video Tracks

| Track | Content | Notes |
|-------|---------|-------|
| V1 | Board screen recording | Main footage from OBS recording of board-art.html |
| V2 | Engine eval overlay | Eval bar captured from overlays/eval-bar.html |
| V3 | Text overlays and annotations | Move labels, arrows, highlights, chapter titles |
| V4 | Picture-in-picture (webcam) | Optional facecam, positioned in corner |

### Audio Tracks

| Track | Content | Notes |
|-------|---------|-------|
| A1 | Voiceover narration | Primary audio — should be loudest |
| A2 | Background music | Chinese instrumental or ambient, 10-15% volume |
| A3 | Sound effects (optional) | Move sounds, clock ticks, notification pings |

### Setting Up Tracks

1. Right-click in the timeline header (where track names are shown).
2. Select **Add Tracks**.
3. Add video and audio tracks as needed to reach the layout above.
4. Rename tracks by right-clicking the track name and selecting **Rename**.
5. Lock tracks you are not actively editing (click the lock icon) to prevent
   accidental changes.

---

## 3. Arrow and Highlight Annotations

Arrows and highlights on the board are essential for directing viewer attention
during analysis. There are two approaches.

### Approach A: Premiere's Built-In Shape Tools (Essential Graphics)

1. Select the **Rectangle Tool** (R) or **Pen Tool** (P) from the toolbar.
2. Draw directly on the Program Monitor (the preview window).
3. To create an arrow:
   - Use the **Pen Tool** to draw an arrow shape, or
   - Go to **Graphics > Essential Graphics** panel, click **New Layer > From
     File**, and import a pre-made arrow PNG with transparency.
4. In the **Essential Graphics** panel (Window > Essential Graphics), adjust:
   - **Fill color:** Green (#00CC00) for good moves, Red (#CC0000) for bad moves
   - **Stroke:** 4px for visibility
   - **Opacity:** 85-90%
5. Position the arrow on the board pointing from the piece's starting square to
   its destination square.

**Animating the arrow (draw-in effect):**
1. Select the arrow graphic on V3.
2. Open **Effect Controls** (Window > Effect Controls).
3. At the start of the clip, set a keyframe for **Scale** at 0% and **Position**
   at the arrow's origin point.
4. Move the playhead forward 0.5 seconds (15 frames at 30fps).
5. Set **Scale** to 100% and **Position** to the final position.
6. Right-click the first keyframe and select **Temporal Interpolation > Ease
   Out** for a smooth draw-in.

**Color coding convention:**
- Green arrows: good moves, recommended moves, key tactical shots
- Red arrows: bad moves, blunders, moves to avoid
- Yellow arrows: interesting alternatives, sideline variations
- Blue highlights (squares): key squares to control

### Approach B: Record from board-art.html

If you use board-art.html's built-in annotation feature (right-click to draw
arrows and highlights on the board), you can simply record these annotations
as part of your OBS screen recording. This is faster than creating annotations
in Premiere but offers less control over animation and timing.

**Recommendation:** Use Approach B for most arrows during recording, and add
Premiere arrows (Approach A) only for emphasis moments or when you need animated
draw-in effects.

---

## 4. Engine Eval Overlay

The engine evaluation bar shows viewers the position's assessment and how it
changes with each move.

### Option A: Screen Recording of eval-bar.html

1. During your OBS recording session, run eval-bar.html in a separate browser
   window alongside board-art.html.
2. Record both windows simultaneously (use OBS's multi-source capture).
3. In Premiere, place the eval bar recording on V2.
4. Use **Effect Controls > Motion > Position** and **Scale** to resize the eval
   bar to a thin vertical strip.
5. Position it on the left side of the screen, approximately 40px wide.
6. Crop any excess using **Effect Controls > Opacity > Mask** (draw a rectangle
   mask around just the eval bar).

### Option B: Static Eval Number Graphic

If you prefer a simpler approach:

1. Create a text layer on V3 (Type Tool > click on Program Monitor).
2. Display the current engine evaluation as a number: "+1.5" or "-0.8".
3. Style: bold monospace font, 36px, white with dark background box.
4. Position: top-left corner of the screen.
5. Update the number at key moments by creating a new text clip for each
   evaluation change.

**Styling the eval overlay:**
- White side advantage: white or light blue text
- Black/red side advantage: red or orange text
- Equal position (within 0.3): neutral gray text
- Winning advantage (over 2.0): larger font or pulsing animation
- Decisive advantage (over 5.0): add "winning" or "必胜" label

### Positioning

Place the eval bar on the left edge of the screen:
- X position: 20-40px from left edge
- Height: full screen height (1080px)
- Width: 30-40px
- This leaves the main board area unobstructed.

---

## 5. Chapter Markers

YouTube chapters allow viewers to jump to specific parts of the analysis.
Planning chapters during editing ensures accurate timestamps.

### Adding Markers in Premiere

1. Move the playhead to the start of each chapter section.
2. Press **M** to add a marker.
3. Double-click the marker to open the Marker dialog.
4. Enter the chapter name in the **Name** field.
5. Set **Duration** to 0 (point marker, not a range).

### Standard Chapter Structure for Game Analysis

| Timestamp | Chapter Name | Content |
|-----------|-------------|---------|
| 0:00 | 开局介绍 (Introduction) | Players, tournament, context |
| ~1:00 | 布局阶段 (Opening) | Opening moves and theory |
| ~5:00 | 中局分析 (Middlegame) | Tactical and strategic analysis |
| ~12:00 | 关键时刻 (Critical Moment) | The turning point of the game |
| ~18:00 | 残局阶段 (Endgame) | Endgame technique |
| ~25:00 | 总结 (Summary) | Lessons learned, key takeaways |

### Exporting Timestamps for YouTube Description

After editing, review your markers and write the chapter list for the YouTube
description:

```
0:00 开局介绍 Introduction
1:15 布局：中炮对屏风马 Opening: Central Cannon vs Screen Horse
5:30 中局：红方弃车攻杀 Middlegame: Red sacrifices Rook
12:00 关键时刻：黑方漏着 Critical Moment: Black's mistake
18:45 残局分析 Endgame Analysis
25:10 总结与要点 Summary & Key Points
```

The first chapter must start at 0:00 for YouTube to recognize the chapter format.
Each chapter must be at least 10 seconds long.

---

## 6. Captions and Subtitles

### Chinese Hardcoded Subtitles (Burned In)

For Chinese subtitles that are permanently visible in the video:

1. Generate an SRT file using translate.html's subtitle generator, or
   transcribe manually.
2. Import the SRT file: **File > Import** and select the .srt file.
3. Drag the SRT file onto V3 (or a higher video track).
4. Premiere will create individual caption clips for each subtitle segment.
5. Alternatively, use **Captions** workspace: **Window > Workspaces > Captions
   and Graphics**.
   - Go to the **Text** panel, click **Transcribe sequence** or import your SRT.
   - Select **Create captions** to generate a caption track.

**Caption styling:**
- Font: Source Han Sans (思源黑体) Bold or Noto Sans CJK Bold
- Size: 42-48px
- Color: White with black outline (stroke 3px) or white on semi-transparent
  black background
- Position: bottom center, above the lower 10% of the screen

### English Soft Subtitles (Separate Upload)

For international viewers, create English subtitles as a separate SRT file
and upload to YouTube:

1. In YouTube Studio, go to the video's **Subtitles** section.
2. Click **Add language** > English.
3. Upload the English SRT file.

This keeps the English subtitles optional — viewers toggle them on or off.

---

## 7. Export Settings

### YouTube Export

1. Go to **File > Export > Media** (Ctrl/Cmd + M).
2. **Format:** H.264
3. **Preset:** Start with "YouTube 1080p Full HD" then customize:
   - **Resolution:** 1920 x 1080
   - **Frame Rate:** 30 fps
   - **Bitrate Encoding:** VBR, 2 Pass
   - **Target Bitrate:** 16 Mbps
   - **Maximum Bitrate:** 20 Mbps
4. **Audio:** AAC, 320 kbps, 48 kHz, Stereo
5. Check **Use Maximum Render Quality**.
6. Set output file name: `analysis-[date]-[players]-youtube.mp4`
7. Click **Export** (or **Queue** to send to Media Encoder).

### Bilibili Export

Bilibili has a 8GB file size limit for most uploaders and prefers smaller files.

1. Export from Premiere with the same YouTube settings above.
2. If the file is too large (over 4GB), reduce the target bitrate to 10-12 Mbps
   or use a tool like HandBrake or MediaCoder to re-encode:
   - **HandBrake settings:** H.264, RF 20-22, Preset "Fast 1080p30"
   - This typically produces a 1-2GB file for a 20-minute video.
3. Output file name: `analysis-[date]-[players]-bilibili.mp4`

**Bilibili-specific notes:**
- Maximum resolution accepted: 4K (but 1080p is standard)
- Accepted formats: MP4, FLV, AVI
- Audio: AAC preferred
- Bilibili re-encodes all uploads, so very high bitrates are wasted

### Quick Export Comparison

| Setting | YouTube | Bilibili |
|---------|---------|----------|
| Format | H.264 | H.264 |
| Resolution | 1920x1080 | 1920x1080 |
| Frame Rate | 30fps | 30fps |
| Bitrate | 16-20 Mbps VBR | 10-12 Mbps VBR |
| Audio | AAC 320kbps | AAC 256kbps |
| File size (20 min) | ~2-3 GB | ~1-2 GB |

---

## 8. Premiere Template (.mogrt) and Project Template

### Motion Graphics Template (.mogrt)

Create reusable graphic elements as .mogrt files using After Effects or
Premiere's Essential Graphics panel.

**Lower third template:**
1. In Premiere, go to **Graphics > Essential Graphics**.
2. Click **New > From file** or design in the Program Monitor using the Type
   and Shape tools.
3. Create a lower third with:
   - Player name field (editable text)
   - Tournament name field (editable text)
   - Semi-transparent background bar
   - Animate: slide in from left over 0.5 seconds, hold for 4 seconds, fade out
4. Select all layers of the graphic, right-click > **Export as Motion Graphics
   Template**.
5. Save as `xiangqi-lower-third.mogrt`.

**Eval bar template:**
1. Create a vertical bar graphic (40px wide, 1080px tall).
2. Add a fill that can be adjusted via a slider (representing evaluation).
3. White section = white advantage, dark section = black advantage.
4. Add a numeric readout text field at the center.
5. Export as `xiangqi-eval-bar.mogrt`.

**Intro and outro templates:**
1. Design a 5-second intro with:
   - Channel name / logo
   - Video title (editable text field)
   - Game info: players, tournament, date (editable text fields)
   - Background: subtle xiangqi board pattern or piece silhouettes
2. Design a 5-10 second outro with:
   - Subscribe reminder
   - Links to related videos (use YouTube end screen elements, not burned-in)
   - Channel logo
3. Export each as .mogrt files.

### Project Template

For the fastest workflow, create a template Premiere project:

1. Set up the full multi-track layout (V1-V4, A1-A3) with tracks named.
2. Place the intro .mogrt on V3 at the start of the timeline.
3. Place the outro .mogrt on V3 at a placeholder position near the end.
4. Add placeholder eval bar on V2.
5. Add a background music track on A2, already set to 10-15% volume.
6. Save this project as `game-analysis-template.prproj`.

For each new analysis video:
1. Copy the template file and rename it.
2. Import new footage and audio into the appropriate bins.
3. Place footage on V1, voiceover on A1.
4. Update editable text fields in the intro and lower thirds.
5. Add arrows and annotations on V3.
6. Adjust the outro position to the actual end of the video.
7. Export.

---

## Editing Workflow Summary

Follow this order for efficient editing:

1. **Import** all footage, audio, and assets into the correct bins.
2. **Rough cut** on V1/A1: lay down the main board recording and voiceover.
   Trim out mistakes, long pauses, and off-topic segments.
3. **Add eval overlay** on V2: sync the eval bar to the main footage.
4. **Annotations** on V3: add arrows, highlights, and move labels at key
   analysis moments.
5. **Text overlays** on V3: chapter title cards, player names (lower thirds),
   position descriptions.
6. **Picture-in-picture** on V4: if using webcam, position it (typically
   bottom-right corner, 20-25% of screen size).
7. **Background music** on A2: set to 10-15% volume, fade in at the start,
   fade out at the end.
8. **Captions**: import or generate Chinese subtitles.
9. **Review**: watch the entire video start to finish. Check audio levels,
   caption accuracy, arrow timing, and eval bar sync.
10. **Chapter markers**: add markers and prepare the YouTube description
    timestamp list.
11. **Export**: render for YouTube and Bilibili.

---

## Keyboard Shortcuts Reference

| Action | Shortcut (Mac) | Shortcut (PC) |
|--------|---------------|---------------|
| Import | Cmd + I | Ctrl + I |
| New sequence | Cmd + N | Ctrl + N |
| Razor tool (split) | C | C |
| Selection tool | V | V |
| Add marker | M | M |
| Ripple delete | Shift + Delete | Shift + Delete |
| Export | Cmd + M | Ctrl + M |
| Undo | Cmd + Z | Ctrl + Z |
| Play/Pause | Space | Space |
| Step forward 1 frame | Right arrow | Right arrow |
| Step back 1 frame | Left arrow | Left arrow |
| Zoom in timeline | = | = |
| Zoom out timeline | - | - |
| Add default transition | Cmd + D | Ctrl + D |

---

## Troubleshooting

**Timeline playback is laggy:**
- Create proxies: right-click footage in the Project panel > **Proxy > Create
  Proxies**. Select "H.264, 1280x720" for proxy format.
- Enable proxy playback: click the wrench icon in the Program Monitor > **Enable
  Proxies**.

**Audio levels are uneven:**
- Select the entire voiceover track on A1.
- Go to **Essential Sound** panel (Window > Essential Sound).
- Tag it as **Dialogue** and enable **Auto Match** to normalize levels.

**SRT import does not align with video:**
- Check that the SRT timestamps match your timeline. If you recorded in segments,
  you may need to offset the SRT times.
- In the Captions panel, you can manually adjust each caption's in/out point.

**Export file is too large for Bilibili:**
- Reduce bitrate to 8-10 Mbps.
- Use HandBrake for a second-pass compression if needed.
- Consider splitting videos longer than 25 minutes into two parts.
