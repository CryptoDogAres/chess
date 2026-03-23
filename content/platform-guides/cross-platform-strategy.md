# Cross-Platform Publishing Workflow

A practical guide for producing xiangqi content once and distributing it across Douyin, Bilibili, and YouTube with platform-specific adaptations.

---

## 1. Core Philosophy: Create Once, Adapt Three Times

The goal is never to create entirely separate content for each platform. Instead, produce core content in a flexible format, then adapt the output for each platform's specs, audience expectations, and algorithm preferences.

**Production priority:** Shoot and edit the "master" version first (typically the long-form Bilibili/YouTube version), then derive short-form and vertical cuts from the same footage.

---

## 2. Content Adaptation Matrix

### Long-Form Analysis (10–30 min original)

| Original Content | Douyin Adaptation | Bilibili Adaptation | YouTube Adaptation |
|---|---|---|---|
| Full game analysis (20 min) | Extract 3 short clips (30–60 sec each): one opening trap, one critical tactic, one dramatic finish | Upload full video as-is; add 封面大粗字 cover; include 弹幕 pause moments for viewer interaction | Upload full video; add timestamps in description; create 1–2 Shorts from highlights |
| Opening theory deep dive (15 min) | 1 short per key variation (45 sec each), focus on the "trap" angle | Full video with detailed tags; write a companion 专栏 article | Full video with SEO title; add cards linking to related openings |
| Tournament round recap (25 min) | 2–3 highlight clips per round, focus on most dramatic moments | Full video; organize into tournament-specific playlist | Full video; add end screen linking to next round; Community tab post with bracket/standings |

### Short-Form Puzzles (30–90 sec original)

| Original Content | Douyin Adaptation | Bilibili Adaptation | YouTube Adaptation |
|---|---|---|---|
| Daily puzzle (60 sec vertical) | Native format; post directly; add trending audio if relevant | Add to a weekly "puzzle compilation" (combine 5–7 into one 5-min video); also post as individual dynamics (动态) | Upload as YouTube Short; also post puzzle image to Community tab as an engagement poll |
| Quick tactic (30 sec) | Post as-is; use as a "hook" video linking to longer content in bio | Post as a 动态 (dynamic/story); reference the full analysis video | Upload as Short with #Shorts tag |
| Opening trap (45 sec) | Post with hook caption: "你知道这个陷阱吗？" | Post individually + include in a "traps" compilation playlist | Short + pin a comment with the full variation in algebraic notation |

### Live Streams

| Original Content | Douyin Adaptation | Bilibili Adaptation | YouTube Adaptation |
|---|---|---|---|
| Live play session (1–2 hrs) | Stream directly on Douyin Live (vertical); clip 3–5 best moments post-stream as individual videos | Stream on Bilibili Live (horizontal); archive full replay; clip highlights | Do not stream simultaneously (unless using Restream); clip best moments as Shorts; consider a condensed "best of" highlights video (10–15 min) |
| Live puzzle solving with audience | Douyin Live; save and re-post the best puzzle solves as standalone clips | Bilibili Live; post full replay in a "Live Replays" playlist | Clip individual puzzles as Shorts; create a "community puzzle session highlights" long-form edit |

---

## 3. Weekly Content Schedule Template

This template assumes a production capacity of 2 long-form videos, 5 short clips, and 1 live stream per week.

| Day | Create | Post on Douyin | Post on Bilibili | Post on YouTube |
|---|---|---|---|---|
| **Monday** | Film long-form video #1 | Short clip (puzzle) at 7:30 PM | — | Community tab post (poll or puzzle image) |
| **Tuesday** | Edit long-form #1; cut short clips | Short clip (tactic) at 7:30 PM | Upload long-form #1 at 5:30 PM | Upload long-form #1 at 5:00 PM EST |
| **Wednesday** | Film/edit short clips batch | Short clip (highlight) at 7:30 PM | 动态 post (puzzle) | Upload Short #1 |
| **Thursday** | Film long-form video #2 | Short clip (puzzle) at 7:30 PM | 专栏 article (companion to Tuesday video) | Community tab (behind-the-scenes or puzzle) |
| **Friday** | Edit long-form #2; cut short clips | Short clip (opening trap) at 7:30 PM | Upload long-form #2 at 5:30 PM | Upload long-form #2 at 5:00 PM EST |
| **Saturday** | Prep for live stream | Live stream at 8 PM; post 1–2 clips after | — | Upload Short #2 |
| **Sunday** | Clip live stream highlights; plan next week | Rest or bonus clip | Post live stream highlight compilation at 2:00 PM | Upload Short #3; end-of-week Community post |

### Adjusting by Production Capacity

- **Minimum viable cadence:** 1 long-form per week, 3 shorts, no live stream. Focus long-form on Bilibili + YouTube; shorts on Douyin + YouTube Shorts.
- **Growth-phase cadence:** 3 long-form per week, daily shorts, 2 live streams. Requires batch filming (film 3 videos in one session, edit across the week).

---

## 4. Tools for Each Step

### Short-Form Editing: 剪映 (CapCut China Edition)

- Best for: Douyin shorts and YouTube Shorts.
- Key features: auto-captions (Chinese), trending templates, vertical format presets, music library synced with Douyin trends.
- Workflow: Import board capture footage → trim to key moment → add captions → add background music → export 1080x1920.
- Export settings: 1080p, 30fps, high quality.

### Long-Form Editing: Adobe Premiere Pro (or DaVinci Resolve)

- Best for: Bilibili and YouTube long-form videos.
- Key features: multi-track timeline, color grading, advanced audio editing, template-based workflows.
- Workflow: Import board capture + webcam footage + audio → arrange on timeline → add annotations/arrows on board → add intro/outro → export 1920x1080 or higher.
- Premiere export preset: H.264, match source, target bitrate 15–20 Mbps, audio AAC 256 kbps.
- DaVinci Resolve alternative: free version handles everything needed for xiangqi content.

### Live Streaming: OBS Studio

- Best for: Bilibili Live and Douyin Live (via RTMP push).
- Scene setup for xiangqi:
  1. **Board capture source:** Window capture of your xiangqi software (天天象棋, XBoard, etc.) or game scene.
  2. **Webcam source:** Position in top-right or bottom-right corner (small, 20–25% of frame).
  3. **Chat overlay source:** Browser source connected to your live chat (optional).
  4. **Audio:** Microphone + optional background music at low volume.
- Output settings: x264 or NVENC, 4000–6000 kbps, 1080p, keyframe interval 2s.
- For streaming to multiple platforms simultaneously, use Restream.io (free for up to 2 destinations) or configure multiple outputs in OBS.

### Screen Capture for Board Recording

- **Windows:** OBS (game capture or window capture targeting the xiangqi software).
- **Mac:** OBS or built-in screen recording (Cmd+Shift+5), then import to editor.
- **Mobile:** Built-in screen recorder (iOS Control Center / Android quick settings) for capturing mobile xiangqi apps.

### Thumbnail and Cover Creation

- **Canva (canva.com):** Free templates for YouTube thumbnails (1280x720), Bilibili covers (1146x717), and Douyin covers (1080x1920). Use the "Bold text on image" templates.
- **Photoshop:** For more control. Create template files at each platform's dimensions and swap board screenshots and text per video.

### Scheduling and Publishing

- **YouTube:** YouTube Studio built-in scheduler.
- **Bilibili:** 定时发布 in the upload interface.
- **Douyin:** 定时发布 in the publish screen (up to 7 days ahead).
- No cross-platform scheduler handles all three natively. Manual upload to each platform is standard. Set a calendar reminder for each posting time.

---

## 5. Analytics Comparison Framework

Track the same content across platforms to understand where your audience responds best.

### Metrics to Compare (Same Video, Different Platforms)

| Metric | Douyin | Bilibili | YouTube |
|---|---|---|---|
| Views (48hr) | From 数据中心 | From 创作中心 → 数据 | From YouTube Studio → Analytics |
| Like ratio | 点赞数 / 播放量 | 点赞数 / 播放量 | Likes / Views |
| Comment count | Direct count | Direct count | Direct count |
| Share count | 转发数 | 分享数 | Shares (in advanced analytics) |
| Completion rate | 完播率 (in 数据中心) | 播放完成率 (estimated from retention curve) | Average view duration / video length |
| New followers gained | 涨粉数 per video | 涨粉数 per video | Subscribers gained per video |
| Revenue (once monetized) | 收益 in 创作者服务中心 | 收益 in 创作中心 | Revenue in YouTube Studio |

### Tracking Spreadsheet Structure

Create a spreadsheet with one row per piece of content:

| Content Title | Publish Date | Douyin Views | Douyin Likes | Douyin Completion | Bili Views | Bili Coins | Bili Favorites | YT Views | YT Watch Time | YT CTR | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|

Review this spreadsheet weekly. After 30+ data points, patterns emerge: certain topics may perform 3x better on one platform than another.

---

## 6. Platform Prioritization by Growth Stage

### Stage 1: Starting Out (0–1,000 followers per platform)

**Priority: Douyin > Bilibili > YouTube**

- Douyin's algorithm gives new creators the most initial distribution. Even with zero followers, a well-made video can reach thousands.
- Focus 60% of effort on Douyin shorts to build momentum and confidence.
- Upload the same content to Bilibili and YouTube but do not stress about optimizing for them yet.
- Goal: Find your content style, improve production speed, and build a small initial audience.

### Stage 2: Building Momentum (1K–10K followers)

**Priority: Bilibili = YouTube > Douyin**

- Shift focus to long-form content on Bilibili and YouTube. These platforms reward depth and have higher monetization potential.
- Continue posting shorts on Douyin but treat it as a "top of funnel" — use Douyin to drive followers to your Bilibili/YouTube for longer content.
- Start live streaming on Bilibili or Douyin (1K follower threshold on Douyin).
- Goal: Establish authority with high-quality long-form content; begin building a community (QQ group, Discord, or Community tab).

### Stage 3: Established Creator (10K–100K followers)

**Priority: YouTube = Bilibili > Douyin**

- YouTube becomes increasingly valuable as subscriber count and watch hours compound. Ad revenue and membership revenue scale better on YouTube.
- Bilibili remains strong for Chinese-language audience engagement and brand deals (花火).
- Douyin remains a short-form distribution engine — continue posting but do not increase effort significantly.
- Begin monetizing on all three platforms.
- Goal: Diversify revenue (ads, memberships, brand deals, courses); hire or outsource editing.

### Stage 4: Scaling (100K+ followers)

**Priority: Balance all three; add new formats**

- At this stage, each platform contributes meaningful audience and revenue.
- Consider: paid courses (Bilibili 付费课程 or external platforms), xiangqi merchandise, coaching services, event hosting.
- Hire a dedicated editor or VA for platform-specific adaptations so you focus only on content creation.
- Goal: Turn the channel into a sustainable business.

---

## 7. Cross-Platform Content Rules

### What NOT to Do

1. **Do not post Douyin-watermarked videos on YouTube or Bilibili.** Re-export from your editing software without watermarks. Platforms deprioritize content with competitor watermarks.
2. **Do not post identical descriptions across platforms.** Each platform's algorithm indexes text differently, and audience expectations differ (Chinese-first on Douyin/Bilibili, English-first or bilingual on YouTube).
3. **Do not go live on all three platforms simultaneously** unless you use a multi-streaming service and can manage all three chats. Better to alternate: Douyin Live on Saturdays, Bilibili Live on Wednesdays.
4. **Do not ignore platform-specific features.** Bilibili has 弹幕 and 专栏; YouTube has Community tab and end screens; Douyin has 合集 and 合拍. Use them.

### What TO Do

1. **Stagger posting times** so you can engage with comments on each platform separately. E.g., Bilibili at 5:30 PM, Douyin at 7:30 PM, YouTube at 5:00 PM EST (next day if you are in a China timezone).
2. **Adapt thumbnails/covers** for each platform's display format and audience expectations.
3. **Maintain a content calendar** that shows what goes where and when. The weekly template above is a starting point — customize it to your capacity.
4. **Review analytics monthly** using the comparison framework to reallocate effort toward the highest-performing platform.
