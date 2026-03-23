# Video Engagement Tracking System

A comprehensive system for tracking video performance across Douyin, Bilibili, and YouTube, and using data to iterate on content format and strategy.

---

## 1. Metrics to Track Per Video

Every video you publish should be measured against a consistent set of metrics. Not all platforms expose the same data, but the goal is to normalize performance tracking so you can compare across platforms and over time.

### Universal Metrics

| Metric | Definition | Good Benchmark | Great Benchmark |
|--------|-----------|----------------|-----------------|
| Views (24h) | Total views within the first 24 hours of posting | Depends on follower count | 10%+ of follower count |
| Views (48h) | Total views within 48 hours | 1.3x of 24h views | 1.5x+ of 24h views |
| Views (7d) | Total views within 7 days | 2x of 24h views | 3x+ of 24h views |
| Views (30d) | Total views within 30 days — indicates long-tail | 2.5x of 24h views | 5x+ (evergreen content) |
| Completion Rate | % of viewers who watched the entire video | >40% | >60% |
| Avg Watch Time % | Average percentage of the video watched | >50% | >70% |
| Like-to-View Ratio | (Likes / Views) x 100 | >3% | >5% |
| Comment Count | Total comments on the video | >0.5% of views | >1% of views |
| Reply Ratio | Your replies / total comments | >30% | >50% |
| Share Count | Number of times the video was shared | >0.3% of views | >1% of views |
| Follower Conversion | New followers gained from this video | >0.1% of views | >0.5% of views |

### Platform-Specific Metrics

**Douyin (抖音)**
- 完播率 (Completion Rate): The single most important metric on Douyin. The algorithm heavily weights this. Target above 40% for videos under 60 seconds.
- 互动率 (Interaction Rate): Calculated as (likes + comments + shares + favorites) / views. Target above 5%.
- 转粉率 (Follow Conversion): Percentage of viewers who followed after watching. Important for growth phase.
- 首页推荐占比: What percentage of traffic came from the "For You" page. Higher means the algorithm is pushing your content.

**Bilibili (B站)**
- 三连率 (Triple-combo Rate): Likes + coins + favorites combined. This is the holy grail metric on Bilibili. A viewer who does all three signals strong approval.
- 弹幕数 (Danmaku Count): Number of real-time bullet comments. High danmaku means the content is engaging moment-to-moment.
- 投币数 (Coin Count): Viewers spend their limited coins on your video. This is the strongest positive signal on the platform.
- 收藏率 (Favorite Rate): Indicates the video has long-term reference value (great for tutorials and analysis).

**YouTube**
- CTR (Click-Through Rate): Percentage of people who saw your thumbnail and clicked. Benchmark: 4-10%.
- Average View Duration: Measured in minutes and seconds, not percentage. YouTube cares about total watch time contributed.
- Impression Share: How many times YouTube showed your thumbnail in browse/search.
- Subscriber Conversion: New subscribers gained per video. Check YouTube Studio analytics.

---

## 2. Tracking Spreadsheet Template

Use this markdown table as the basis for a spreadsheet (Google Sheets, Excel, or Notion database). Log every video within 24 hours of posting, then update at the 7-day mark.

| Date | Title | Platform | Type | Views-24h | Views-7d | Completion% | Likes | Comments | Shares | Notes |
|------|-------|----------|------|-----------|----------|-------------|-------|----------|--------|-------|
| 2026-03-10 | 这步弃车你敢走吗？ | Douyin | Puzzle | 12,400 | 28,500 | 62% | 890 | 134 | 67 | Hook worked well, sacrifice theme |
| 2026-03-10 | 弃车妙手解析 | Bilibili | Analysis | 3,200 | 8,100 | 48% | 245 | 89 | 23 | Good danmaku at sacrifice moment |
| 2026-03-12 | Beginner Trap: The Cannon Sacrifice | YouTube | Tutorial | 1,800 | 5,400 | 55% | 142 | 38 | 12 | English title performed better than bilingual |
| 2026-03-14 | 残局挑战：3步杀 | Douyin | Puzzle | 18,200 | 41,000 | 71% | 1,340 | 210 | 145 | Best performer this week, short and punchy |
| 2026-03-15 | 胡荣华经典名局 | Bilibili | Famous Game | 5,100 | 14,300 | 42% | 380 | 112 | 34 | Long video, completion rate lower as expected |
| 2026-03-16 | 这步你会走吗？ | Douyin | Interactive | 9,800 | 22,100 | 58% | 720 | 312 | 56 | High comment count from interactive format |
| 2026-03-18 | Engine vs Grandmaster: Who Wins? | YouTube | Engine | 2,400 | 7,200 | 51% | 198 | 67 | 28 | Thumbnail A/B test version A |
| 2026-03-19 | 新手必学：当头炮开局 | Douyin | Tutorial | 7,600 | 16,800 | 45% | 410 | 78 | 34 | Tutorial gets lower engagement but good follow conversion |
| 2026-03-20 | 象棋AI分析：这步电脑都算不到 | Bilibili | Engine | 4,300 | 11,700 | 53% | 310 | 145 | 41 | AI angle drives comments and debate |
| 2026-03-22 | 5秒找到杀棋 | Douyin | Puzzle | 15,600 | 35,200 | 68% | 1,120 | 178 | 98 | Time pressure in title creates urgency |

### How to Use This Table

- Update Views-7d exactly 7 days after posting. This gives you a consistent comparison window.
- The Notes column is critical. Write down your hypothesis for why the video performed the way it did. After 20-30 videos, patterns will emerge.
- Color-code rows by performance: green for top 25%, yellow for middle 50%, red for bottom 25%.
- At the end of each month, export and archive the data. Start a fresh sheet.

---

## 3. Weekly Analysis Framework

Every Sunday (or your chosen day), spend 30-60 minutes reviewing the week's data. Follow this exact framework.

### Step 1: Identify Top Performer

Look at the video with the highest overall engagement (not just views). Ask yourself:
- What was the topic? Was it a puzzle, analysis, tutorial, or interactive format?
- What was the hook? Write out the exact first 3 seconds or first line of the title.
- What time was it posted? Did timing matter?
- Was there anything unusual? A trending topic, a collaboration, a controversial take?
- Can you replicate the formula? Write down the replicable elements.

### Step 2: Identify Worst Performer

Look at the video with the lowest engagement relative to your average. Ask yourself:
- Was the topic weak, or was the execution weak?
- Did the thumbnail/title fail to attract clicks (low impressions-to-view ratio)?
- Did viewers drop off early (low completion rate) or just not engage (low likes/comments)?
- Was it posted at a bad time or on a day with unusual competition?
- What would you change if you remade this video?

### Step 3: Pattern Check

After 4+ weeks of data, look for patterns across content types:

| Content Type | Avg Completion% | Avg Like Rate | Avg Comment Rate | Verdict |
|-------------|----------------|---------------|-----------------|---------|
| Puzzle | ? | ? | ? | |
| Famous Game Analysis | ? | ? | ? | |
| Beginner Tutorial | ? | ? | ? | |
| Interactive (Would You Play?) | ? | ? | ? | |
| Engine vs Human | ? | ? | ? | |

Fill this in monthly. The content type that consistently wins deserves more of your production time.

### Step 4: Hook Effectiveness

For each video, check the audience retention graph (available on all three platforms). Look specifically at the first 3 seconds:
- What percentage of viewers made it past 3 seconds?
- If below 70% at the 3-second mark, your hook is failing.
- Compare hooks across videos: which style retains viewers best?
  - Question hook: "这步你会走吗？"
  - Shock hook: "这步棋99%的人走错"
  - Stakes hook: "一步定胜负"
  - Visual hook: Start on the critical board position, no intro

### Step 5: Thumbnail CTR Comparison (YouTube Specific)

Review YouTube Studio impressions and CTR for each video:
- Sort by CTR. What do the top thumbnails have in common?
- Test patterns: board close-up vs. face + board, text overlay vs. clean, red arrows vs. no arrows.
- Keep a thumbnail swipe file of your best performers.

---

## 4. Iteration Playbook: Decision Tree

Use this decision tree to diagnose problems and decide what to change. Work through it top to bottom for any underperforming video.

### Problem: Completion Rate Below 40%

**Diagnosis**: Your hook is not working. Viewers are clicking but leaving quickly.

**Action**:
- Rewrite your hook. The first 3 seconds must create curiosity or tension.
- Try starting with the most dramatic moment of the video (the sacrifice, the checkmate threat).
- Remove any intro, logo animation, or "hello everyone" greeting. Get straight to the position.
- Test shorter video length. If your 90-second videos get 35% completion, try 45-second versions.

### Problem: Completion Rate Above 60% but Low Views

**Diagnosis**: The content is good, but nobody is finding it. This is a discovery problem: title, thumbnail, or SEO.

**Action**:
- Rewrite the title with stronger keywords. Use search-friendly terms.
- On Douyin: ensure your hashtags match trending topics. Check the "热搜" for relevant chess terms.
- On YouTube: check your CTR in YouTube Studio. If below 4%, the thumbnail needs work.
- On Bilibili: make sure your video is tagged in the right category (棋牌 section).
- Consider re-uploading with a new title/thumbnail if the video is genuinely good but got no traction.

### Problem: High Views but Low Likes

**Diagnosis**: People are watching but not feeling compelled to engage. The content may be too surface-level or the CTA is missing.

**Action**:
- Add more depth. Instead of just showing the move, explain why it is surprising or what the opponent missed.
- Include a "like if you found it" moment before revealing the answer to a puzzle.
- Add personal commentary or reaction. Emotion drives engagement.
- Check if the video feels complete. Viewers who feel satisfied are more likely to like.

### Problem: High Likes but Low Comments

**Diagnosis**: Viewers enjoy the content but have no reason to comment. You need to prompt discussion.

**Action**:
- End with a question: "你会怎么走？评论区告诉我" (What would you play? Tell me in the comments).
- Present two candidate moves and ask viewers to vote in comments.
- Make a slightly controversial claim: "This is better than Hu Ronghua's move" — viewers will debate.
- Pin a comment with a question to seed the discussion.

### Problem: One Content Type Dominates

**Diagnosis**: This is not a problem. This is a signal.

**Action**:
- Produce 2x more of the winning content type next week.
- Test variations within that type. If puzzles win, try: timed puzzles, puzzle series, puzzle difficulty levels.
- Do not abandon other content types entirely. Keep 1-2 per week as experiments.
- Consider making the dominant type your channel identity.

---

## 5. A/B Testing Guide

A/B testing on social video platforms is not as clean as website A/B testing, but you can still get useful signal with a structured approach.

### What to Test

| Variable | How to Test | What to Measure |
|----------|-------------|-----------------|
| Thumbnails | Upload same video with different thumbnails, 1 week apart | CTR (YouTube), Views-24h (Douyin) |
| Titles | Same video, different title phrasing | Views-24h, CTR |
| Hook style | Same content, different first 3 seconds | Completion rate |
| Video length | Same topic, 45s vs 90s version | Completion rate, total engagement |
| Posting time | Same content type, different day/time | Views-24h |
| Format | Same topic as puzzle vs. analysis vs. tutorial | All metrics |

### How to Test Properly

1. **Isolate one variable**: Only change one thing at a time. If you change both the thumbnail and the title, you will not know which one caused the difference.
2. **Use similar content**: The two test videos should be as similar as possible in topic and quality. Do not compare your best puzzle against your worst tutorial.
3. **Space them out**: Publish version A and version B one week apart, on the same day of the week, at the same time. This controls for day-of-week effects.
4. **Same platform**: Compare within a single platform. Cross-platform comparisons have too many confounding variables.
5. **Wait for the data**: Do not check results after 2 hours. Wait a full 7 days before drawing conclusions.

### Sample Size Requirements

- **Minimum**: 1,000 views per variant before making any conclusion.
- **Preferred**: 5,000+ views per variant for reliable signal.
- **If you are below 1,000 views**: You cannot A/B test effectively yet. Focus on producing more content and growing your base audience first.

### Recording A/B Test Results

| Test # | Variable | Version A | Version B | Metric | Result A | Result B | Winner | Confidence |
|--------|----------|-----------|-----------|--------|----------|----------|--------|------------|
| 1 | Thumbnail | Board close-up | Board + face | CTR | 4.2% | 6.8% | B | High (5K+ views each) |
| 2 | Hook | Question hook | Visual hook | Completion% | 48% | 61% | B | Medium (2K views each) |
| 3 | Length | 90 seconds | 45 seconds | Completion% | 38% | 64% | B | High (8K views each) |
| 4 | Post time | 8pm Monday | 8pm Friday | Views-24h | 5,200 | 4,800 | A | Low (single test) |
| 5 | Title | 弃车杀棋 | 这步你敢走吗？ | Views-24h | 6,100 | 11,400 | B | High (algorithm gave both fair push) |

### Applying A/B Test Results

- After 3+ tests confirm the same finding, adopt it as your default.
- Document your findings in a "Content Playbook" document that you update monthly.
- Revisit old conclusions every 2-3 months. Platform algorithms change, and what worked in March may not work in June.
- Share learnings with collaborators or editors so the whole team operates from the same data.

---

## Monthly Review Checklist

At the end of each month, answer these questions:

1. How many videos did I publish this month? (Target: 12-20 across all platforms)
2. Which platform grew the fastest in followers?
3. What was my best-performing video and why?
4. What was my worst-performing video and why?
5. Did I run any A/B tests? What did I learn?
6. Which content type had the highest average engagement?
7. Am I spending my production time on the content types that perform best?
8. What is my one change for next month?

Write the answers down. Keep a running monthly log. After 3 months, you will have enough data to make confident strategic decisions about your content direction.
