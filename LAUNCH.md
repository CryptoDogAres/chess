# LAUNCH CHECKLIST — Go Live in 14 Days

Everything is prepared. Scripts are written, tools are built, the engine is running, OBS is configured. This is the master document that turns 43 remaining tasks into a day-by-day action plan. Follow it from top to bottom; nothing requires improvisation.

Every step references the exact guide, script, or tool you need. Open the referenced file, follow its instructions, check the box, move on.

---

## How to Use This Checklist

1. Work through each day in order. Do not skip ahead.
2. Each task has an estimated time. If you finish early, use the remaining time to preview the next day.
3. File paths are relative to the project root (`chess/`). Open them in your editor or browser as needed.
4. After completing each task, mark it done: `- [x]`

**Total estimated time: 25-40 hours over 14 days.**

---

## Day 1: Equipment & Accounts (2-3 hours)

### Task 1: Buy a Microphone (15 min to order)

- [ ] **Order a USB microphone** — Fifine K669B (~$25) is the recommended starter
  - Full comparison of budget/mid/pro options: `content/platform-guides/microphone-guide.md`
  - Key spec: Cardioid pattern, USB plug-and-play, 16-bit/48kHz
  - Also works: TONOR TC-777 (~$30) or Blue Yeti (~$100) if you want to invest more
- [ ] **Optional: Order a boom arm** (~$20) to reduce desk vibration noise
- [ ] **Skip webcam for now** — xiangqi content is board-focused; add a camera later only if viewers request it

### Task 2: Register Douyin Account (20 min)

- [ ] Download the Douyin app (iOS App Store or douyin.com for Android)
- [ ] Register with phone number (+86) — full steps in `content/platform-guides/douyin-guide.md` Section 1
- [ ] Switch to Creator Account (创作者账号): 我 > 三横线 > 设置 > 账号与安全 > 切换为创作者账号
- [ ] Select category: 教育 > 兴趣教学
- [ ] Set display name: include 象棋 for discoverability (format suggestions in `content/platform-guides/douyin-guide.md` Section 2)
- [ ] Upload avatar: open `branding.html` in browser > Logo section > Download PNG
- [ ] Upload banner: `branding.html` > Douyin Banner section > Download
- [ ] Write bio: copy template from `content/platform-guides/douyin-guide.md` Section 2

### Task 3: Register Bilibili Account (20 min)

- [ ] Go to bilibili.com or download the Bilibili app
- [ ] Register with phone number, email, or linked WeChat/QQ — full steps in `content/platform-guides/bilibili-guide.md` Section 1
- [ ] Pass the Member Exam (会员考试) for official member status — details in `content/platform-guides/bilibili-guide.md` Section 1
- [ ] Complete Real-Name Verification (实名认证) for future monetization
- [ ] Set display name: include 象棋 keyword (format suggestions in `content/platform-guides/bilibili-guide.md` Section 2)
- [ ] Upload avatar: same PNG from `branding.html`
- [ ] Upload banner: `branding.html` > Bilibili Banner section > Download
- [ ] Write bio: copy template from `content/platform-guides/bilibili-guide.md` Section 2

### Task 4: Create YouTube Channel (30 min)

- [ ] Follow the complete setup checklist: `content/platform-guides/youtube-setup-checklist.md`
- [ ] Create channel with custom name (bilingual recommended, e.g., 象棋ChessLab)
- [ ] Claim your @handle — match your Douyin/Bilibili handles if possible
- [ ] Upload profile picture: same PNG from `branding.html` (800x800)
- [ ] Upload banner: `branding.html` > YouTube Banner section > Download (2560x1440)
- [ ] Write channel description using template from `content/platform-guides/youtube-setup-checklist.md` Section 3
- [ ] Create 7 playlists as listed in `content/platform-guides/youtube-setup-checklist.md`:
  - Puzzle Challenge (残局挑战)
  - Famous Game Analysis (名局解说)
  - Beginner Tutorial Series (零基础学象棋)
  - Would You Play This? (这步你会走吗)
  - Engine vs Grandmaster (引擎vs大师)
  - Famous Game Stories (名局故事)
  - Live Stream Highlights (直播精华)
- [ ] Set default upload description template from `content/platform-guides/templates.md`
- [ ] Enable YouTube Shorts uploads

### Task 5: Register on Chess Platforms (15 min)

- [ ] Create account on tiantianchess.com — steps in `content/platform-guides/tiantianchess-guide.md`
- [ ] Create account on xiangqi.com — steps in `content/platform-guides/xiangqi-com-guide.md`
- [ ] These accounts are for playing games on-stream and sourcing positions

---

## Day 2: Software Setup & Test Recording (1.5-2.5 hours)

### Task 6: Configure OBS Studio (30 min)

- [ ] Open OBS Studio (already installed at /Applications/OBS.app)
- [ ] Run the setup script:
  ```bash
  chmod +x chess/obs-config/setup.sh
  bash chess/obs-config/setup.sh
  ```
- [ ] Import profiles from `obs-config/`:
  - `landscape-profile.ini` — 1920x1080 for analysis videos and live streams
  - `vertical-profile.ini` — 1080x1920 for Douyin/YouTube Shorts
- [ ] Create 4 scenes following `obs-config/README.md`:
  - **Board Analysis** (landscape) — browser source pointing to `board-art.html`
  - **Explain Mode** (landscape) — browser source pointing to `explain.html`
  - **Vertical Short** (vertical) — browser source pointing to `board-art.html`, cropped for 9:16
  - **Live Stream** — browser source + overlays from `overlays/stream-frame.html`
- [ ] Import scene collection from `obs-config/scenes.json` if supported, otherwise create manually
- [ ] Configure audio: Settings > Audio > Mic/Auxiliary Audio > select your USB microphone
- [ ] Add audio filters (in order) per `content/platform-guides/streaming-test-guide.md`:
  1. Noise Suppression (RNNoise)
  2. Compressor (Ratio 4:1, Threshold -18 dB, Attack 6 ms, Release 60 ms)
  3. Limiter (Threshold -1 dB)
- [ ] Verify video settings:
  - Landscape: Base 1920x1080, Output 1920x1080, CBR 6000 Kbps, H.264
  - Vertical: Base 1080x1920, Output 1080x1920, same bitrate

### Task 7: Set Up OBS Overlays (15 min)

- [ ] Add browser sources for overlays (used during live streams):
  - `overlays/eval-bar.html` — engine evaluation display
  - `overlays/player-info.html` — player names and ratings
  - `overlays/move-ticker.html` — scrolling move list
  - `overlays/puzzle-challenge.html` — puzzle overlay for interactive segments
  - `overlays/subscriber-alert.html` — follower/subscriber notifications
  - `overlays/stream-frame.html` — decorative stream border
- [ ] Position each overlay in the Live Stream scene per `obs-config/README.md`

### Task 8: Set Up CapCut / Jianying (15 min)

- [ ] Open CapCut (already installed at /Applications/CapCut.app)
- [ ] Follow initial setup in `content/platform-guides/capcut-editing-guide.md` Section 1
- [ ] If publishing primarily on Douyin, use Jianying (剪映) instead for direct Douyin integration
- [ ] Familiarize yourself with: Import > Timeline > Auto-Captions > Export workflow

### Task 9: Test the Full Recording Pipeline (30 min)

- [ ] Open `board-art.html` in your browser
- [ ] Switch OBS to **Board Analysis** scene
- [ ] Verify the board renders correctly in the OBS preview — pieces visible, no cropping issues
- [ ] Start a test recording
- [ ] Read 30-60 seconds of `content/puzzles/01-ma-hou-pao.md` aloud while moving pieces
- [ ] Stop recording
- [ ] Watch playback and check:
  - Audio: clear voice, no clipping, peaks between -12 dB and -6 dB
  - Video: board sharp, pieces readable, no frame drops
  - Sync: audio matches piece movements
- [ ] Switch OBS to **Vertical Short** scene and repeat a 15-second test
- [ ] If issues, consult `content/platform-guides/streaming-test-guide.md` for troubleshooting

### Task 10: Test Live Stream Setup (20 min)

- [ ] Follow the complete pre-stream checklist: `content/platform-guides/streaming-test-guide.md`
- [ ] Switch OBS to **Live Stream** scene
- [ ] Verify all overlays render correctly
- [ ] Do a dry run: speak for 2 minutes, move pieces, check overlay positioning
- [ ] Test stream key setup for Douyin (do NOT go live yet; just confirm the connection works)

---

## Day 3: Record First Batch of Puzzle Videos (2-3 hours)

### Task 11: Record 5 Puzzle Videos in One Session

Record all 5 back-to-back to stay in flow. Each takes approximately 15 minutes including setup.

**Per-video workflow:**
1. Open `explain.html` in browser and load the puzzle position
2. Switch OBS to **Vertical Short** scene (1080x1920 for Douyin)
3. Start OBS recording
4. Read the script aloud while demonstrating moves on the board
5. Stop recording
6. Save file with naming convention: `puzzle-01-ma-hou-pao-raw.mp4`

- [ ] **Video 1: Ma Hou Pao (马后炮)**
  - Script: `content/puzzles/01-ma-hou-pao.md`
  - Target duration: 45-90 seconds
- [ ] **Video 2: Tian Di Pao (天地炮)**
  - Script: `content/puzzles/02-tian-di-pao.md`
  - Target duration: 45-90 seconds
- [ ] **Video 3: Men Gong (闷宫)**
  - Script: `content/puzzles/03-men-gong.md`
  - Target duration: 45-90 seconds
- [ ] **Video 4: Tie Men Shuan (铁门栓)**
  - Script: `content/puzzles/04-tie-men-shuan.md`
  - Target duration: 45-90 seconds
- [ ] **Video 5: Qi Xing Ju Hui (七星聚会)**
  - Script: `content/puzzles/05-qi-xing-ju-hui.md`
  - Target duration: 45-90 seconds

### Task 12: Review Raw Recordings (15 min)

- [ ] Watch all 5 recordings back-to-back
- [ ] Note any that need re-recording (audio issues, major stumbles, wrong moves)
- [ ] Re-record any that have critical problems before moving on

---

## Day 4: Record Game Analysis & Tutorial (2-3 hours)

### Task 13: Record Game Analysis #1 (45 min)

- [ ] Open `board-art.html` and load the game position
- [ ] Switch OBS to **Board Analysis** scene (landscape 1920x1080)
- [ ] Script: `content/famous-games/02-hu-ronghua-vs-yang-guanlin-1962.md`
- [ ] Start recording
- [ ] Walk through the entire game following the script (target: 15-25 minutes)
- [ ] Stop recording, review for major issues

### Task 14: Record Tutorial Episode #1 (30 min)

- [ ] Open `explain.html` and set up the rules demonstration
- [ ] Switch OBS to **Explain Mode** scene (landscape)
- [ ] Script: `content/tutorials/01-rules.md`
- [ ] Start recording (target: 8-12 minutes)
- [ ] Stop recording, review

### Task 15: Record Series Pilot (30 min)

- [ ] Script: `content/series/01-would-you-play-this-pilot.md`
- [ ] Use `explain.html` with the critical position loaded
- [ ] Switch OBS to **Board Analysis** scene
- [ ] Start recording (target: 5-10 minutes)
- [ ] Stop recording, review

### Task 16: Record Game Analysis #2 (45 min)

- [ ] Script: `content/famous-games/01-hu-ronghua-vs-lu-qin-1988.md`
- [ ] Same workflow as Task 13
- [ ] Start recording (target: 15-25 minutes)

---

## Day 5: Edit All Videos (3-4 hours)

### Task 17: Edit 5 Puzzle Videos in CapCut (2.5 hours, ~30 min each)

Follow `content/platform-guides/capcut-editing-guide.md` for the complete workflow.

For each puzzle video:
- [ ] Import raw recording into CapCut
- [ ] Trim dead air at start and end
- [ ] Add auto-captions (Chinese for Douyin version)
- [ ] Add bold text overlays for key moves and puzzle prompts
- [ ] Add background music (subtle, low volume)
- [ ] Export at 1080x1920, 30fps, high quality
- [ ] Save as: `puzzle-01-ma-hou-pao-final.mp4` (etc.)

Checklist per video:
- [ ] Puzzle 1 (马后炮) edited and exported
- [ ] Puzzle 2 (天地炮) edited and exported
- [ ] Puzzle 3 (闷宫) edited and exported
- [ ] Puzzle 4 (铁门栓) edited and exported
- [ ] Puzzle 5 (七星聚会) edited and exported

### Task 18: Edit Game Analysis #1 in Premiere Pro or CapCut (45 min)

Follow `content/platform-guides/premiere-editing-guide.md` for long-form workflow.

- [ ] Import raw recording of Hu Ronghua vs Yang Guanlin 1962
- [ ] Add chapter markers per the timestamps in `content/growth/first-month-plan.md` Day 2 section
- [ ] Add engine evaluation overlay where relevant
- [ ] Add Chinese captions for Bilibili version
- [ ] Add English captions/subtitles for YouTube version
- [ ] Export landscape 1920x1080
- [ ] Extract one 45-second highlight clip and export as vertical 1080x1920 (bonus Douyin content)

### Task 19: Edit Tutorial #1 (30 min)

- [ ] Import raw recording of Rules tutorial
- [ ] Trim, add captions, add chapter markers
- [ ] Export landscape 1920x1080 for Bilibili and YouTube
- [ ] Cut a 60-second "piece movement highlights" vertical clip for Douyin

### Task 20: Edit Series Pilot (20 min)

- [ ] Import raw recording of "Would You Play This?" pilot
- [ ] Add a "pause here" prompt overlay at the critical moment
- [ ] Add captions, trim, export landscape 1920x1080

### Task 21: Edit Game Analysis #2 (45 min)

- [ ] Same workflow as Task 18 for Hu Ronghua vs Lu Qin 1988

---

## Day 6: Thumbnails, Titles & Metadata (1.5-2 hours)

### Task 22: Generate Thumbnails (30 min)

- [ ] Open `branding.html` in your browser
- [ ] Generate a thumbnail for each video using the matching template:
  - Puzzles 1-5: use **Puzzle (谜题挑战)** template
  - Game Analysis 1-2: use **Famous Game (名局对弈)** template
  - Tutorial 1: use **Tutorial (教学入门)** template
  - Series Pilot: use **Puzzle** template with series branding
- [ ] Download each thumbnail as PNG
- [ ] Naming convention: `thumb-puzzle-01.png`, `thumb-game-01.png`, etc.

### Task 23: Prepare All Titles and Descriptions (30 min)

Every title, description, hashtag set, and pinned comment is pre-written. Copy them from:

- [ ] **Week 1 titles and descriptions**: `content/growth/first-month-plan.md` — Week 1 section (Days 1-7)
- [ ] **Week 2 titles and descriptions**: `content/growth/first-month-plan.md` — Week 2 section (Days 8-14)
- [ ] Create a spreadsheet or text file mapping each video to its:
  - Platform-specific title (Douyin / Bilibili / YouTube)
  - Platform-specific description
  - Hashtags
  - Pinned comment text
  - Posting time

Reference documents:
- Title templates: `content/platform-guides/templates.md`
- Bilibili title format (【brackets】style): `content/platform-guides/bilibili-titles.md`
- Hook formulas: `content/platform-guides/video-hooks.md`
- SEO optimization: `seo.html`

### Task 24: Prepare SEO for YouTube Videos (20 min)

- [ ] Open `seo.html` in your browser
- [ ] Generate optimized tags for each YouTube video
- [ ] Prepare YouTube descriptions using the templates from `content/growth/first-month-plan.md`
- [ ] Include timestamps in descriptions for all long-form videos

### Task 25: Set Up Content Calendar (15 min)

- [ ] Open `calendar.html` in your browser
- [ ] Enter all 14 days of scheduled content with dates and platforms
- [ ] Cross-reference posting times from `content/growth/first-month-plan.md`:
  - Douyin: 19:30 CST (7:30 PM)
  - Bilibili: 17:30 CST (5:30 PM)
  - YouTube: 17:00 EST (next-day for North American audience)

---

## Day 7: PUBLISH DAY (1-2 hours)

This is Day 1 of the first-month plan in `content/growth/first-month-plan.md`.

### Task 26: Publish Puzzle #1 on Douyin (15 min)

- [ ] Upload `puzzle-01-ma-hou-pao-final.mp4` to Douyin at **19:30 CST**
- [ ] Title: 90%的人走错这步棋！你能找到正确答案吗？
- [ ] Description: copy from `content/growth/first-month-plan.md` Day 1
- [ ] Hashtags: #象棋 #残局 #象棋残局 #你会走吗 #马后炮
- [ ] Pin comment: 你觉得正确答案是什么？写在回复里！答对的第一个人我会置顶你的评论

### Task 27: Cross-Post Puzzle #1 to YouTube Shorts (10 min)

- [ ] Re-export without Douyin watermark if needed (see `content/platform-guides/cross-platform-strategy.md`)
- [ ] Upload to YouTube Shorts
- [ ] Title: 90% Get This Chess Puzzle WRONG! Can You Solve It? #xiangqi
- [ ] Description: copy from `content/growth/first-month-plan.md` Day 1
- [ ] Add to "Puzzle Challenge" playlist
- [ ] Pin comment: What's the best move here? First correct answer gets pinned!

### Task 28: Engage After Publishing (1 hour)

- [ ] Set a 2-hour timer immediately after publishing
- [ ] Stay on each platform for the first 30 minutes — reply to every comment in real time
- [ ] Check back at the 1-hour and 2-hour marks — reply to all new comments
- [ ] Strategy guide: `content/growth/comment-strategy.md`
- [ ] Key principle: every reply doubles your comment count and triggers return visits, boosting algorithmic reach by 15-20% on Douyin

### Task 29: Log Analytics (5 min)

- [ ] Open `analytics.html` in your browser
- [ ] Record Day 1 metrics: views, likes, comments, shares for each video
- [ ] Mark as published in `calendar.html`

---

## Day 8: Publish Game Analysis + Tutorial (1.5 hours)

This maps to Days 2 and 4 of the first-month plan. We publish both on the same day since we are compressing the preparation phase.

### Task 30: Publish Game Analysis #1 on Bilibili (15 min)

- [ ] Upload Hu Ronghua vs Yang Guanlin 1962 to Bilibili at **17:30 CST**
- [ ] Title: 【象棋名局】15岁少年击败全国冠军！胡荣华vs杨官璘 1962年经典对局
- [ ] Description and hashtags: copy from `content/growth/first-month-plan.md` Day 2
- [ ] Upload thumbnail from `thumb-game-01.png`
- [ ] Pin comment: 你觉得15岁的胡荣华最厉害的是计算力还是心理素质？评论区聊聊

### Task 31: Publish Game Analysis #1 on YouTube (15 min)

- [ ] Upload same video with English subtitles/voiceover
- [ ] Title: 15-Year-Old Beats the National Champion! Hu Ronghua's Legendary Game (1962)
- [ ] Description with timestamps: copy from `content/growth/first-month-plan.md` Day 2
- [ ] Custom thumbnail
- [ ] Add to "Famous Game Analysis" playlist
- [ ] Pin comment: What impresses you most about the 15-year-old Hu Ronghua — his calculation or his nerves?

### Task 32: Publish Tutorial #1 on Bilibili and YouTube (15 min)

- [ ] Bilibili title: 【零基础学象棋】第1集：认识棋盘和规则（10分钟学会下棋）
- [ ] YouTube title: Learn Chinese Chess in 10 Minutes! Complete Beginner Guide
- [ ] Descriptions, hashtags, pinned comments: copy from `content/growth/first-month-plan.md` Day 4
- [ ] Cross-post the 60-second vertical clip to Douyin with title: 10分钟学会下象棋！新手必看

### Task 33: Engage and Log (45 min)

- [ ] Reply to all comments within 2 hours on every platform — follow `content/growth/comment-strategy.md`
- [ ] Log metrics in `analytics.html`
- [ ] Update `calendar.html`

---

## Day 9: Publish Puzzle #2 + Series Pilot (1 hour)

### Task 34: Publish Puzzle #2 on Douyin at 19:30 CST

- [ ] Video: Tian Di Pao (天地炮)
- [ ] Title: 3步杀！大师级残局挑战，你敢试吗？
- [ ] Description, hashtags, pinned comment: `content/growth/first-month-plan.md` Day 3
- [ ] Cross-post to YouTube Shorts

### Task 35: Publish Series Pilot on Bilibili and YouTube

- [ ] Bilibili title: 【这步你会走吗？】第1期：一步看似平凡的兵，却暗藏杀机
- [ ] YouTube title: Would You Play THIS Move? Xiangqi Puzzle Series Ep.1
- [ ] All metadata from `content/growth/first-month-plan.md` Day 6 Part A
- [ ] Add to respective playlists

### Task 36: Engage and Log

- [ ] Reply to all comments within 2 hours
- [ ] Log metrics in `analytics.html`

---

## Day 10: Publish Puzzle #3 + Start Creator Engagement (1 hour)

### Task 37: Publish Puzzle #3 on Douyin at 19:30 CST

- [ ] Video: Men Gong (闷宫)
- [ ] Title: 这步棋99%的人都想不到！闷宫绝杀
- [ ] All metadata from `content/growth/first-month-plan.md` Day 5
- [ ] Cross-post to YouTube Shorts

### Task 38: Begin Creator Network Engagement (30 min)

- [ ] Read `content/growth/creator-network.md` fully
- [ ] Identify the first 3 creators to engage with (start with Tier 1 large creators)
- [ ] Leave one thoughtful, analytical comment on each creator's latest video
- [ ] Key rule: never self-promote; be the smartest comment in the room
- [ ] Repeat this daily — 10 creators total over the next week

---

## Day 11: Record Week 2 Batch + Publish (3-4 hours)

### Task 39: Record Week 2 Puzzle Videos (1 hour)

- [ ] **Puzzle 6: Ye Ma Cao Fei (野马操菲)** — Script: `content/puzzles/06-ye-ma-cao-fei.md`
- [ ] **Puzzle 7: Shuang Che Cuo (双车错)** — Script: `content/puzzles/07-shuang-che-cuo.md`
- [ ] **Puzzle 8: Pao Nian Dan Sha (炮碾丹砂)** — Script: `content/puzzles/08-pao-nian-dan-sha.md`
- [ ] Same recording workflow as Day 3 (Task 11)

### Task 40: Record Week 2 Long-Form Content (1.5 hours)

- [ ] **Game Analysis #3**: `content/famous-games/03-xu-yinchuan-vs-lu-qin-2000.md`
- [ ] **Tutorial #2**: `content/tutorials/02-pieces-1.md`
- [ ] **Series Episode #2**: `content/series/02-engine-vs-grandmaster-pilot.md`

### Task 41: Publish Puzzle #4 on Douyin at 19:30 CST

- [ ] Video: Tie Men Shuan (铁门栓)
- [ ] Title: 铁门栓！这道残局把象棋大师都难住了
- [ ] All metadata from `content/growth/first-month-plan.md` Week 2 Day 8
- [ ] Cross-post to YouTube Shorts

### Task 42: Publish Game Analysis #2 on Bilibili/YouTube

- [ ] Hu Ronghua vs Lu Qin 1988
- [ ] Bilibili title: 【象棋名局】胡荣华vs吕钦 1988：两代棋王的巅峰对决
- [ ] YouTube title: Two Xiangqi Kings Clash! Hu Ronghua vs Lu Qin 1988 — Full Analysis
- [ ] All metadata from `content/growth/first-month-plan.md` Week 2 Day 9

---

## Day 12: Edit Week 2 + Publish (3-4 hours)

### Task 43: Edit Week 2 Videos (2-3 hours)

- [ ] Edit Puzzles 6-8 in CapCut (same workflow as Task 17)
- [ ] Edit Game Analysis #3 in Premiere Pro (same workflow as Task 18)
- [ ] Edit Tutorial #2 (same workflow as Task 19)
- [ ] Edit Series Episode #2 (same workflow as Task 20)
- [ ] Generate thumbnails for all using `branding.html`

### Task 44: Publish Puzzle #5 on Douyin at 19:30 CST

- [ ] Video: Qi Xing Ju Hui (七星聚会)
- [ ] Title: 七星聚会！中国象棋最经典的古谱残局
- [ ] All metadata from `content/growth/first-month-plan.md` Week 2 Day 10
- [ ] Cross-post to YouTube Shorts

### Task 45: Publish Tutorial #2 on Bilibili/YouTube

- [ ] Bilibili title: 【零基础学象棋】第2集：车马炮的走法与实战技巧
- [ ] YouTube title: Xiangqi Pieces Explained: Chariot, Horse & Cannon — Beginner Series Ep.2
- [ ] All metadata from `content/growth/first-month-plan.md` Week 2 Day 11

---

## Day 13: Publish + Prepare for Live Stream (2 hours)

### Task 46: Publish Puzzle #6 on Douyin at 19:30 CST

- [ ] Video: Ye Ma Cao Fei (野马操菲)
- [ ] Title: 野马操菲！这招马的走法太惊艳了
- [ ] Metadata from `content/growth/first-month-plan.md` Week 2 Day 12

### Task 47: Publish Series Episode #2 on Bilibili/YouTube

- [ ] Bilibili title: 【引擎vs大师】第1期：AI推荐的走法，许银川为什么没走？
- [ ] YouTube title: Engine vs Grandmaster Ep.1: Why Xu Yinchuan Ignored the Computer's Move
- [ ] Metadata from `content/growth/first-month-plan.md` Week 2 Day 13

### Task 48: Prepare for First Live Stream (30 min)

- [ ] Run the full pre-stream checklist: `content/platform-guides/streaming-test-guide.md`
- [ ] Prepare 10 puzzles to solve live (select from `content/puzzles/` scripts 01-10)
- [ ] Set up OBS **Live Stream** scene with overlays:
  - `overlays/stream-frame.html`
  - `overlays/puzzle-challenge.html`
  - `overlays/subscriber-alert.html`
- [ ] Write a pre-stream announcement post for Douyin (template in `content/growth/first-month-plan.md` Day 6 Part B)
- [ ] Post the announcement at 18:00 CST (2 hours before stream)

---

## Day 14: First Live Stream + Week 2 Wrap-Up (3-4 hours)

### Task 49: Go Live on Douyin at 20:00 CST (2-3 hours)

- [ ] Start OBS streaming to Douyin
- [ ] Title: 象棋直播：残局挑战赛！评论区出题我来解
- [ ] Format:
  - Solve prepared puzzles live
  - Take viewer-submitted puzzles from chat
  - Play casual games against audience members
  - Recap the first week of content
- [ ] Use `overlays/puzzle-challenge.html` for interactive puzzle segments
- [ ] After stream: clip 2-3 best moments as standalone Douyin videos (buffer content for next week)

### Task 50: Post Sunday Community Content (20 min)

- [ ] Post a Bilibili dynamic (动态) with a puzzle image and engagement prompt — template in `content/growth/first-month-plan.md` Day 7
- [ ] Post a YouTube Community tab poll:
  - "What content do you want to see more of this week?"
  - Options: More puzzles / Famous game analysis / Beginner tutorials / Live stream highlights

### Task 51: Week 2 Analytics Review (15 min)

- [ ] Open `analytics.html` and review all metrics from the past 7 publishing days
- [ ] Compare actual performance against benchmarks in `content/growth/first-month-plan.md`
- [ ] Identify: Which videos got the most views? Which had the best engagement rate?
- [ ] Open `report.html` for a formatted summary view
- [ ] Adjust Week 3 plans based on what performed best

---

## After Day 14: Ongoing Operations

You have now published 10+ videos across 3 platforms, completed your first live stream, and established a posting cadence. Here is what comes next.

### Week 3-4: Continue the First Month Plan

- [ ] Follow `content/growth/first-month-plan.md` Weeks 3 and 4 exactly (Days 15-30)
- [ ] Week 3 scripts ready:
  - Puzzles 7-9: `content/puzzles/07-shuang-che-cuo.md` through `content/puzzles/09-qi-zi-gui-bian.md`
  - Game Analysis 3: `content/famous-games/03-xu-yinchuan-vs-lu-qin-2000.md`
  - Tutorial 3: `content/tutorials/03-pieces-2.md`
  - Series 3: `content/series/03-famous-game-stories-pilot.md`
- [ ] Week 4 scripts ready:
  - Puzzle 10: `content/puzzles/10-da-dan-chuan-xin.md`
  - Game Analysis 4: `content/famous-games/04-wang-tianyi-vs-zheng-weitong-2018.md`
  - Tutorial 4: `content/tutorials/04-basic-kills-1.md`
- [ ] Start Wednesday Bilibili live streams in Week 3 (20:00 CST)

### Ongoing Weekly Schedule

Follow `content/growth/posting-schedule.md` for the steady-state 7-video weekly cadence:

| Day | Content | Platform | Script Source |
|-----|---------|----------|---------------|
| Monday | Puzzle | Douyin + YouTube Shorts | `content/puzzles/` |
| Tuesday | Game Analysis | Bilibili + YouTube | `content/famous-games/` |
| Wednesday | Puzzle | Douyin + YouTube Shorts | `content/puzzles/` |
| Thursday | Tutorial | Bilibili + YouTube | `content/tutorials/` |
| Friday | Puzzle | Douyin + YouTube Shorts | `content/puzzles/` |
| Saturday | Series Episode | Bilibili + YouTube | `content/series/` |
| Sunday | Live Stream | Douyin + Bilibili | Live / prepared topics |

### Growth Tasks

- [ ] Install vidIQ Chrome extension for YouTube keyword and tag tracking
- [ ] Track traffic in `analytics.html` weekly — look for trends
- [ ] Use `seo.html` to optimize titles and descriptions based on performance data
- [ ] Continue engaging with 10 creators from `content/growth/creator-network.md` daily
- [ ] Use `content/platform-guides/shorts-repurposing.md` to extract short clips from long-form content
- [ ] Use `content/platform-guides/highlight-clips.md` to create live stream highlight reels
- [ ] Cross-reference `content/platform-guides/engagement-tracking.md` for comment and engagement metrics

### Community Building

- [ ] Create a Discord server using `content/community/discord/setup-guide.md`
- [ ] Set up channels per `content/community/discord/channels.md`
- [ ] Configure roles per `content/community/discord/roles.md`
- [ ] Post welcome message from `content/community/discord/welcome-message.md`
- [ ] Set up bot commands from `content/community/discord/bot-commands.md`
- [ ] Plan first tournament using `content/community/discord/tournament-format.md`
- [ ] Post weekly puzzle challenges using `content/community/puzzle-challenge-template.md`

### Revenue Milestones

- [ ] **Douyin**: 1,000 followers unlocks live streaming gifts and basic monetization
- [ ] **Bilibili**: 1,000 followers + official member status unlocks Creation Incentive Program (创作激励)
- [ ] **YouTube**: 1,000 subscribers + 4,000 watch hours unlocks YouTube Partner Program
- [ ] Register for 巨量星图 (Juliang Xingtu) when eligible — full guide: `content/revenue/brand-deal-guide.md`
- [ ] Plan online course using curriculum: `content/revenue/course-curriculum.md`
- [ ] Plan 1-on-1 coaching offering: `content/revenue/coaching-plan.md`
- [ ] Plan merchandise line: `content/revenue/merchandise-plan.md`
- [ ] Set up live stream tipping and gifts: `content/revenue/livestream-tips-guide.md`

---

## Quick Reference: All Tools

| Tool | Location | Purpose |
|------|----------|---------|
| Interactive Board | `board.html` | Play and demonstrate positions |
| Artistic Board | `board-art.html` | Beautiful board for recording |
| 3D Board | `board3d.html` | 3D perspective board view |
| Explanation Mode | `explain.html` | Analysis with engine + annotations |
| Analysis Tool | `analyze.html` | Deep engine analysis |
| Branding Generator | `branding.html` | Logos, banners, thumbnails |
| SEO Tool | `seo.html` | Title/tag optimization |
| Calendar | `calendar.html` | Content scheduling tracker |
| Analytics Dashboard | `analytics.html` | Performance metrics |
| Report Generator | `report.html` | Formatted analytics reports |
| Script Viewer | `scripts.html` | Browse all video scripts |
| Translation Tool | `translate.html` | Chinese/English content translation |
| Game Database | `games.html` | Browse famous game records |
| Master Dashboard | `dashboard.html` | Central hub for all tools |
| Index | `index.html` | Project overview and navigation |

## Quick Reference: All Content

| Content Type | Location | Count |
|-------------|----------|-------|
| Puzzle Scripts | `content/puzzles/` | 10 scripts ready |
| Famous Game Scripts | `content/famous-games/` | 5 scripts ready |
| Tutorial Scripts | `content/tutorials/` | 12 episodes ready |
| Series Pilots | `content/series/` | 3 pilots ready |
| Platform Guides | `content/platform-guides/` | 16 guides |
| Growth Strategies | `content/growth/` | 4 guides |
| Community Plans | `content/community/` | 7 documents |
| Revenue Plans | `content/revenue/` | 5 guides |
| OBS Configuration | `obs-config/` | 4 files + README |
| Stream Overlays | `overlays/` | 6 HTML overlays |

---

## The Math

- **30 scripts** are written and ready to record (10 puzzles + 5 famous games + 12 tutorials + 3 series pilots)
- **16 platform guides** tell you exactly how to set up, edit, publish, and optimize
- **6 stream overlays** are built and ready to load into OBS
- **All titles, descriptions, hashtags, and pinned comments** for the first 30 days are pre-written in `content/growth/first-month-plan.md`
- **Every thumbnail** can be generated from `branding.html` in under a minute

There is nothing left to prepare. Open OBS. Press record. Publish.
