# Complete Bilibili Channel Setup Guide

A comprehensive guide to launching and growing a xiangqi (Chinese chess) channel on Bilibili (B站). Covers every technical detail, spec, and strategy from account creation to monetization.

---

## 1. Account Creation

1. Go to bilibili.com or download the Bilibili app (iOS / Android).
2. Click **注册** (Register).
3. Register with a Chinese phone number (+86), email, or linked WeChat/QQ account.
4. Complete CAPTCHA verification.
5. Choose initial interests: select **知识** (Knowledge), **棋牌** (Board Games), and **生活** (Lifestyle) to seed recommendations.

### Becoming an UP主 (Content Creator)

Any registered Bilibili account can upload videos immediately — there is no separate application. However, to unlock full features:

1. **Pass the 会员考试 (Member Exam):** 100 questions about Bilibili community guidelines and general knowledge. Passing grants "正式会员" (official member) status, which unlocks bullet comments (弹幕), voting, and other community features.
2. **Real-Name Verification (实名认证):** Required for monetization. Go to **设置 → 安全隐私 → 实名认证**. Requires a Chinese ID card or passport.

### Creator Certification (UP主认证)

- **个人认证:** For individual creators. Requirements: 1,000+ followers and consistent content history.
- **机构认证:** For organizations. Requires business license.
- Apply at: member.bilibili.com → 认证中心.
- Benefits: verified badge, priority in search results, access to 花火 brand platform.

---

## 2. Profile Optimization

### Display Name (昵称)

- Maximum 16 characters.
- Include a xiangqi keyword for discoverability.
- Suggested formats:
  - `象棋[Name]` — e.g., 象棋小许
  - `[Name]的象棋课堂` — e.g., 老李的象棋课堂
  - `[Name]Chess` — bilingual appeal

### Avatar (头像)

- **Dimensions:** 300 x 300 px minimum.
- **Format:** JPG, PNG, or GIF (animated avatars are supported for 年度大会员).
- **File size:** Under 2 MB.
- Displayed as a circle. Keep key elements in the center 80% area.

### Banner / Top Image (头图)

- **Dimensions:** 2120 x 340 px.
- **Safe area:** Center 1240 x 340 px (this is what displays on most screens; sides may be cropped on narrower windows).
- **Format:** JPG or PNG, under 5 MB.
- Include: channel name, posting schedule, and a xiangqi visual. Place critical text and imagery in the center safe area.

### Bio (个人简介)

Maximum 70 characters visible without expansion (full bio up to 100 characters).

**Variant 1 — Professional / Authoritative:**
```
象棋国家级裁判 | 专注布局与残局教学
每周三、六更新 | 合作私信联系
棋力提升，从理解每一步开始
```

**Variant 2 — Casual / Community-Focused:**
```
下棋十五年的普通爱好者
实战复盘 · 残局拆解 · 新手避坑指南
评论区是最好的棋室，欢迎来聊
```

**Variant 3 — Bilingual:**
```
Xiangqi (Chinese Chess) Analysis & Tutorials
象棋布局·中局·残局 全阶段教学
English subtitles available | 中英双字
```

### Additional Profile Fields

- **Tags (标签):** Add up to 5. Use: 象棋, 棋牌, 中国象棋, 教学, 传统文化.
- **Links:** Add your Douyin, YouTube, and personal website links in the profile social section.

---

## 3. Content Settings and Video Specs

### Recommended Upload Settings

| Setting | Value |
|---|---|
| Resolution | 1920 x 1080 px (1080p) minimum; 2560 x 1440 (2K) or 3840 x 2160 (4K) preferred |
| Aspect Ratio | 16:9 (landscape) |
| Frame Rate | 30 fps standard; 60 fps for live game replays |
| Codec | H.264 (AVC) for widest compatibility; H.265 (HEVC) accepted |
| Container | MP4 (.mp4) or FLV (.flv) |
| Video Bitrate | 8–16 Mbps for 1080p; 20–35 Mbps for 4K |
| Audio Codec | AAC |
| Audio Bitrate | 192–320 kbps |
| Sample Rate | 48 kHz |
| Max File Size | 8 GB (regular), 32 GB (with higher member level) |
| Max Duration | No hard limit for uploads; 4+ hours supported |

### Avoiding Bilibili Re-Encoding Quality Loss

Bilibili re-encodes all uploaded videos. To minimize quality degradation:

1. **Upload at higher-than-target quality.** If you want viewers to see 1080p clearly, upload in 2K (2560x1440).
2. **Use high bitrate.** For 1080p, export at 15+ Mbps. This gives Bilibili's encoder more data to preserve.
3. **Use Constant Quality (CRF) encoding** in your export: CRF 16–18 in x264 yields excellent quality.

### MediaCoder Compression Settings (Optional Optimization)

If using MediaCoder for pre-upload optimization:

- Video codec: x264
- Rate control: CRF, value 17
- Profile: High
- Level: 4.1
- Preset: Slow (better compression, higher quality)
- Audio: AAC-LC, 192 kbps, 48 kHz
- Container: MP4

### Cover Image (封面)

- **Dimensions:** 1146 x 717 px (displayed at 16:10 aspect ratio).
- Bilibili cover images are critical for click-through rate. Use the **封面大粗字** (big bold text cover) strategy:
  - Font size: equivalent to 100–140pt.
  - Maximum 6–10 Chinese characters on the cover.
  - High contrast: white or yellow text with dark stroke/shadow on a board screenshot background.
  - Example text: "这步棋90%的人下错" or "残局一招制胜".
- Bilibili shows covers as thumbnails in feeds, recommendations, and search. Test readability at small sizes.

---

## 4. Optimal Posting Schedule

| Day | Best Upload Time | Notes |
|---|---|---|
| Weekdays | 5:00–5:30 PM (17:00–17:30) | Upload before the evening traffic peak (6–10 PM). Bilibili's recommendation engine starts distributing ~30 min after processing. |
| Saturday | 2:00 PM or 7:00 PM | Two traffic peaks on weekends. |
| Sunday | 10:00 AM or 5:00 PM | Morning learners + evening casual viewers. |

- **Key insight:** Upload at 5:30 PM on weekdays so the video is processed and entering distribution by 6:00–6:30 PM, catching the largest viewership window.
- Use Bilibili's scheduled publishing (定时发布) feature to queue uploads.
- Consistency signals: pick 2–3 fixed days per week and maintain the schedule for at least 8 weeks before evaluating.

---

## 5. Tag Strategy

### Top 30 Xiangqi Tags for Bilibili

Use 5–10 tags per video. Mix broad and specific.

**High Traffic:**
1. 象棋
2. 中国象棋
3. 象棋残局
4. 棋牌
5. 象棋教学
6. 下棋
7. 象棋对弈
8. 象棋高手
9. 残局
10. 象棋入门

**Medium Traffic:**
11. 象棋布局
12. 象棋中局
13. 象棋战术
14. 象棋技巧
15. 象棋实战
16. 棋谱讲解
17. 象棋大师
18. 象棋比赛
19. 残局破解
20. 象棋杀法

**Niche / Specific:**
21. 飞相局
22. 中炮对屏风马
23. 顺炮直车
24. 仙人指路
25. 象棋复盘
26. 象棋AI
27. 天天象棋
28. 象棋名局
29. 象棋思维
30. 棋力提升

### Tag Placement

- Add tags in the dedicated tag field during upload (not in the title or description).
- First 3 tags carry the most weight. Put your primary keyword tag first.

---

## 6. Understanding the Bilibili Algorithm (B站推荐算法)

Bilibili uses a multi-signal recommendation system. Videos are evaluated on a combination of engagement ratios relative to impressions.

### Key Ranking Factors

1. **Play Count (播放量):** Base metric. But raw plays alone are not enough — ratios matter more.
2. **Like Ratio (点赞率):** Likes / views. Target: >5%.
3. **Coin Ratio (投币率):** Coins / views. Coins are a finite resource for viewers (they get ~5 per day), so a coin is a strong quality signal. Target: >2%.
4. **Favorite Ratio (收藏率):** Favorites / views. Educational content naturally favors this. Target: >3%. Xiangqi tutorials and opening guides should aim for >5% since viewers save them for reference.
5. **Share Ratio (分享率):** Shares / views. Target: >1%.
6. **Bullet Comments (弹幕) and Comments:** Active discussion signals value. Encourage viewers to post their move suggestions in 弹幕 during puzzle moments.
7. **Completion Rate (完播率):** Full-watch ratio. Important but weighted slightly less than on Douyin.
8. **三连 (Triple Combo):** When a viewer likes + coins + favorites in one action, it is the strongest single engagement signal on Bilibili.

### Actionable Takeaways

- Explicitly ask for 三连 (一键三连) at the end of every video. This is standard Bilibili culture and not considered pushy.
- For puzzle content, pause the video with on-screen text "暂停想一想" before the solution. This increases watch time and engagement.
- Educational/tutorial content gets a boost in Bilibili's knowledge (知识区) recommendation pool. Tag and categorize appropriately.
- Reply to comments within the first 2 hours after posting.

---

## 7. Monetization

### Creation Incentive Program (创作激励计划)

- **Requirements:** 1,000+ followers OR total play count of 100,000+.
- Revenue is based on play count, engagement quality, and content category. Estimated rate: 1–3 RMB per 1,000 views for knowledge/education content.
- Enroll at: member.bilibili.com → 创作激励.
- Payment: Monthly settlement to linked bank card. Minimum withdrawal: 100 RMB.

### 充电 (Power-Up / Tipping)

- Viewers can "充电" (power up) your videos or channel with real money.
- Revenue split: creator receives approximately 70% after platform commission.
- Enable in: 创作中心 → 收益管理 → 充电设置.
- Two modes: per-video charging and monthly channel charging (like a subscription).

### 花火 (Sparkle — Brand Collaboration Platform)

- Bilibili's official brand deal marketplace.
- **Requirements:** 10,000+ followers, personal or institutional certification, consistent posting history.
- Register at: huahuo.bilibili.com.
- Set pricing for: video integration, dedicated videos, live stream mentions, and banner placements.
- Xiangqi channels attract: educational apps, board game retailers, tea/culture brands, mobile game sponsors.

### Paid Courses (付费课程)

- Bilibili supports paid video series (付费系列) for creators with 10,000+ followers.
- Ideal for structured xiangqi courses: "象棋零基础到入门30讲" or "残局100题精讲."
- Pricing: set by the creator, typically 6–68 RMB per course.

### Live Stream Gifts (直播礼物)

- Similar to Douyin. Viewers send virtual gifts during live streams.
- Revenue split: approximately 50% to creator.
- Bilibili live threshold: no minimum follower count, but 实名认证 required.

---

## 8. QQ Group Community Setup

Bilibili creators commonly maintain a QQ group for community engagement. This is where dedicated fans gather.

### Setup Steps

1. Create a QQ group: open QQ → Groups → Create Group → select "兴趣爱好" → "棋牌."
2. Group name: match your Bilibili channel name + "粉丝群" (e.g., "象棋老李粉丝群").
3. Set group capacity: 200 (free), 500 or 1,000 (QQ VIP/SVIP).
4. Create group rules pinned announcement:
   ```
   欢迎加入[频道名]象棋交流群！
   1. 禁止广告、刷屏
   2. 可自由讨论象棋话题
   3. 每周日晚8点群内车轮战
   4. 新视频首发通知在群内发布
   ```
5. Add the QQ group number to your Bilibili profile bio and video descriptions.
6. Use the group for: early video access, poll-based content decisions, live watch parties, and community tournaments.

---

## 9. 专栏 (Column / Article Feature)

Bilibili's column feature lets you publish long-form written content (articles) alongside your videos.

### How to Use 专栏

1. Go to member.bilibili.com → 投稿 → 专栏.
2. Write articles with rich text, images, and embedded Bilibili videos.
3. Categories: select 棋牌 or 知识.

### Content Ideas for 专栏

- Written game analyses with board diagrams (screenshot each move).
- Opening theory reference guides (e.g., "中炮对屏风马完全指南").
- Xiangqi book reviews.
- Tournament recaps with annotated key positions.
- "How I analyze a game" — walkthrough of your review process.

### Why Use 专栏

- Written content is indexed by Baidu search, bringing external traffic.
- Articles complement videos: viewers who want to study at their own pace will favorite articles.
- 专栏 engagement (likes, coins, favorites) counts toward your overall creator metrics.

---

## 10. Live Streaming on Bilibili

### Setup

1. Go to link.bilibili.com and register as a live streamer.
2. **实名认证** is required.
3. Select live category: 棋牌 → 象棋.
4. Download **Bilibili Live Studio (直播姬)** for PC streaming, or use OBS with the provided RTMP information.

### RTMP Streaming (OBS)

1. In the Bilibili live dashboard, start a live room.
2. Copy the RTMP address (rtmp://live-push.bilivideo.com/live-bvc/) and stream key.
3. OBS settings:
   - Encoder: x264 or NVENC
   - Bitrate: 4000–6000 kbps
   - Resolution: 1920x1080
   - Keyframe interval: 2 seconds
4. Scene setup for xiangqi: board capture (window or screen region) + webcam overlay in corner + chat overlay.

### Live Stream Best Practices

- Stream 2–3 times per week at consistent times.
- Set a live stream cover (封面) and title with keywords: "象棋实战对弈" or "残局挑战赛."
- Interact with bullet comments constantly — Bilibili's live algorithm prioritizes active chat rooms.
- Use the "PK" feature to challenge other xiangqi streamers for cross-audience exposure.

---

## Quick-Start Checklist

- [ ] Register Bilibili account and pass 会员考试
- [ ] Complete 实名认证
- [ ] Set display name with "象棋" keyword
- [ ] Upload 300x300 avatar and 2120x340 banner (content in center 1240x340 safe area)
- [ ] Write bio using one of the 3 templates above
- [ ] Add 5 profile tags
- [ ] Upload first video: 16:9, 1080p+, with 1146x717 cover image using 封面大粗字 strategy
- [ ] Add 5–10 tags from the list above
- [ ] Post at 5:30 PM on a weekday
- [ ] Ask for 一键三连 at the end of the video
- [ ] Reply to every comment in the first 2 hours
- [ ] Create a QQ group and add the number to your bio
- [ ] Write your first 专栏 article complementing your video
- [ ] After 1,000 followers: enroll in 创作激励计划
- [ ] After 10,000 followers: register on 花火
- [ ] Set up live streaming in the 棋牌 category
