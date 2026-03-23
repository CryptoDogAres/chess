# A/B Testing and Series Optimization Guide

**Purpose:** Systematically test different content variables to find what resonates most with your audience, then double down on winners and retire underperformers.

**Tasks completed:** cs6 (series testing framework), cs7 (optimization based on data)

---

## 1. What to A/B Test for Series Retention

You cannot improve what you do not measure. These are the four highest-impact variables to test.

### Variable A: Episode Length

| Variant | Length | Best For |
|---------|--------|----------|
| Short | 4-6 minutes | Douyin, TikTok, casual viewers, puzzle content |
| Medium | 8-12 minutes | Bilibili, YouTube, game analysis, tutorials |
| Long | 14-18 minutes | YouTube deep dives, full game analysis, dedicated audience |

**How to test:** Take the SAME content topic and produce it at two different lengths. For example, analyze the same famous game in a 6-minute version (key moments only) and a 12-minute version (full walkthrough). Publish both on the same platform one week apart, same day and time.

**What to measure:** Completion rate is the primary metric. A 6-minute video with 70% completion outperforms a 12-minute video with 35% completion in terms of algorithm favor, but the 12-minute video delivers more total watch time per viewer (4.2 min vs 4.2 min -- in this example they tie). Calculate both.

### Variable B: Hook Style

Test these three opening styles across your videos:

**Style 1: Question Hook (问题式)**
```
"如果你是红方，面对这个局面你会怎么走？大多数人都会走错。"
```

**Style 2: Bold Claim Hook (大胆声明式)**
```
"这一步棋，直接决定了全国冠军的归属。"
```

**Style 3: Action Start Hook (直接开始式)**
```
[No intro. Board appears immediately, pieces start moving.]
"炮二平五，马八进七，红方开局就暗藏杀机。"
```

**How to test:** Use a different hook style each week for the same series. After 4 weeks, you have data on all three styles for that series. Some series may favor different hooks -- puzzle videos might work best with questions, while famous game analysis might work best with bold claims.

### Variable C: Thumbnail Style

| Style | Description | Example Elements |
|-------|-------------|-----------------|
| **Board Close-Up** | Zoomed-in critical position with an arrow or highlight | Board image, red circle on key piece, minimal text |
| **Face + Emotion** | Your face showing surprise/excitement with small board in corner | Expressive face, small board overlay, 1-2 Chinese characters |
| **Text-Heavy** | Large bold text with board as background | "99%的人走错了！", board slightly blurred behind text |

**How to test:** For each video, create two thumbnail versions. Publish with Thumbnail A for the first 48 hours, then switch to Thumbnail B for the next 48 hours. Compare CTR (click-through rate) for each period. On YouTube, use the built-in A/B thumbnail test feature if available.

### Variable D: Series Format

If you run multiple series (e.g., Puzzles, Famous Games, Opening Tutorials), track each separately to see which format your audience prefers:

| Series | Format Description | Key Metric |
|--------|-------------------|------------|
| Weekly Puzzle Challenge | Short, interactive, single position | Engagement (comments with answers) |
| Famous Game Analysis | Story-driven, full game walkthrough | Watch time and completion rate |
| Opening Tutorial | Educational, structured lessons | Subscriber conversion rate |

---

## 2. How to Measure Retention: Platform-Specific Metrics

### Douyin (抖音)

| Metric | Chinese Name | Where to Find | What It Tells You |
|--------|-------------|---------------|-------------------|
| Completion Rate | 完播率 | Creator Dashboard > Video Data | % of viewers who watched to the end |
| Average Watch Duration | 平均播放时长 | Creator Dashboard > Video Data | How long viewers stay on average |
| Interaction Rate | 互动率 | Creator Dashboard > Video Data | Likes + comments + shares / views |
| Follow Conversion | 关注转化率 | Creator Dashboard > Fan Data | % of viewers who followed after watching |
| Traffic Source | 流量来源 | Creator Dashboard > Video Data | Recommender vs search vs profile visits |

**Douyin-specific notes:**
- Completion rate is the MOST important metric for Douyin's algorithm
- Videos under 60 seconds: aim for 40%+ completion
- Videos 1-3 minutes: aim for 25%+ completion
- Videos 3+ minutes: aim for 15%+ completion
- Check data at 24h, 48h, and 7-day marks

### Bilibili (B站)

| Metric | Chinese Name | Where to Find | What It Tells You |
|--------|-------------|---------------|-------------------|
| Play Completion Rate | 播放完成率 | Creator Center > Video Data > Playback | % who watched to the end |
| Average Watch Duration | 平均观看时长 | Creator Center > Video Data > Playback | Average minutes watched |
| Coin Rate | 投币率 | Creator Center > Video Data > Interaction | Coins per 1000 views (strong approval signal) |
| Danmaku Density | 弹幕密度 | Creator Center > Video Data | Where viewers are most engaged |
| Three-Hit Rate | 三连率 | Creator Center > Video Data | Like + coin + favorite combo -- the strongest signal |

**Bilibili-specific notes:**
- Bilibili favors longer content and rewards watch time
- Track danmaku timestamps to find which moments resonate
- Coin rate above 3% is excellent
- Pay attention to 收藏率 (favorite rate) -- indicates rewatchable content

### YouTube

| Metric | English Name | Where to Find | What It Tells You |
|--------|-------------|---------------|-------------------|
| Audience Retention | Audience Retention | YouTube Studio > Analytics > Engagement | Second-by-second % of viewers still watching |
| Average View Duration | Average View Duration | YouTube Studio > Analytics > Overview | Average minutes watched per view |
| Click-Through Rate | CTR | YouTube Studio > Analytics > Reach | % of impressions that became views |
| Subscriber Conversion | Subscribers Gained | YouTube Studio > Analytics > Audience | New subs from each video |
| Returning Viewers | Returning Viewers % | YouTube Studio > Analytics > Audience | % of viewers who have watched before |

**YouTube-specific notes:**
- The retention curve shape matters more than the raw number
- Look for drop-off points: if 40% leave in the first 30 seconds, your hook needs work
- A flat retention curve (even at lower %) is better than a steep initial drop
- Average view duration directly correlates with search ranking
- Compare "New Viewers" vs "Returning Viewers" retention separately

---

## 3. Decision Framework

### Testing Protocol

**Duration:** 4 weeks minimum per test

**Volume:** At least 1 episode per series per week (3 videos per week if testing 3 series)

**Consistency:** Same upload day/time for each series throughout the test period

**Isolation:** Only change ONE variable at a time. If you are testing episode length, keep the hook style, thumbnail style, and content quality the same.

### Metrics to Compare

For each video, record these core numbers:

| Metric | Why It Matters |
|--------|---------------|
| Views (7-day) | Raw reach |
| Completion Rate | Content quality signal |
| Average Watch Duration | Algorithm fuel |
| Likes / Interactions | Engagement depth |
| New Subscribers | Growth signal |
| Comments Count | Community engagement |

### The Winner Formula

**Winner Score = Completion Rate x Views (7-day)**

This formula balances reach with quality. A video with 10,000 views and 40% completion scores 4,000. A video with 5,000 views and 90% completion scores 4,500. The second video wins because it resonated more deeply despite lower reach.

**Secondary tiebreaker:** Subscriber conversion rate. If two variants score similarly, the one that converts more subscribers wins.

### Decision Rules

| Result | Action |
|--------|--------|
| Clear winner (>20% higher score) | Double down immediately |
| Slight winner (5-20% higher) | Run one more week to confirm, then double down |
| Tie (within 5%) | Test a different variable -- these options are equivalent |
| Clear loser (>30% lower score) | Reduce to 1x/month or retire |

---

## 4. "Double Down" Playbook

Once you have identified a winning series or format, execute this playbook.

### Step 1: Increase Frequency (Week 5)

| Series Performance | New Schedule |
|-------------------|-------------|
| Winner | 2x per week (e.g., Tuesday + Friday) |
| Middle performer | 1x per week (unchanged) |
| Loser | 1x per month (testing slot -- try new concepts) |

### Step 2: Reallocate Production Time (Week 5-6)

Calculate your current time allocation:

```
Before:
- Series A (winner): 4 hours/week (1 video)
- Series B (middle): 4 hours/week (1 video)
- Series C (loser): 4 hours/week (1 video)
Total: 12 hours/week for 3 videos

After:
- Series A (winner): 7 hours/week (2 videos)
- Series B (middle): 4 hours/week (1 video)
- Series C (experimental): 1 hour/month (1 quick video)
Total: 12 hours/week for 3 videos + 1 monthly
```

You produce more content without more total time by focusing effort on what works.

### Step 3: Deepen the Winner (Week 6-8)

- Create a playlist or series collection for the winning format
- Develop a backlog of 10+ episode ideas
- Improve production value specifically for this series
- Create series-specific thumbnails with consistent branding
- Add end-screen links between episodes to boost binge-watching

### Step 4: Test Within the Winner (Week 8+)

Now A/B test variables WITHIN your winning series:
- Hook variations
- Episode structure (linear analysis vs jumping to key moments)
- Thumbnail refinements
- Cross-platform timing (which platform first?)

### Step 5: Retire or Pivot the Loser (Week 8)

Options for the underperforming series:
1. **Retire completely** -- stop producing, leave existing videos up
2. **Merge concepts** -- take the best elements and fold them into the winner
3. **Transform** -- keep the topic but change the format entirely
4. **Seasonal return** -- bring it back monthly as a "special" rather than a regular series

---

## 5. Sample 4-Week A/B Test Schedule

**Test objective:** Determine which of three series formats gets the best retention.

**Series being tested:**
- Series A: Weekly Puzzle Challenge (每周一题) -- 5-6 minutes
- Series B: Famous Game Analysis (名局解析) -- 10-12 minutes
- Series C: Opening Tutorial (开局教学) -- 8-10 minutes

**Upload schedule:** Same day each week, consistent time.

### Week 1 (Monday April 6 - Sunday April 12, 2026)

| Day | Content | Platform | Hook Style |
|-----|---------|----------|------------|
| Tuesday Apr 7 | Puzzle #1: Chariot + Cannon mate | Douyin, Bilibili, YouTube | Question hook |
| Thursday Apr 9 | Famous Game #1: Hu Ronghua vs Yang Guanlin 1980 | Bilibili, YouTube | Bold claim hook |
| Saturday Apr 11 | Opening #1: Central Cannon basics (中炮入门) | Bilibili, YouTube, Douyin | Action start hook |

**Track by Sunday April 12:** Views, completion rate, likes, new subs for each video on each platform.

### Week 2 (Monday April 13 - Sunday April 19, 2026)

| Day | Content | Platform | Hook Style |
|-----|---------|----------|------------|
| Tuesday Apr 14 | Puzzle #2: Knight fork challenge | Douyin, Bilibili, YouTube | Question hook |
| Thursday Apr 16 | Famous Game #2: Xu Yinchuan vs Zhao Guorong 2001 | Bilibili, YouTube | Bold claim hook |
| Saturday Apr 18 | Opening #2: Screen Horse defense (屏风马) | Bilibili, YouTube, Douyin | Action start hook |

**Track by Sunday April 19:** Same metrics. Begin comparing Week 1 vs Week 2 trends.

### Week 3 (Monday April 20 - Sunday April 26, 2026)

| Day | Content | Platform | Hook Style |
|-----|---------|----------|------------|
| Tuesday Apr 21 | Puzzle #3: Cannon sacrifice mate | Douyin, Bilibili, YouTube | Question hook |
| Thursday Apr 23 | Famous Game #3: Wang Tianyi vs Zheng Weitong 2018 | Bilibili, YouTube | Bold claim hook |
| Saturday Apr 25 | Opening #3: Flying Elephant opening (飞相局) | Bilibili, YouTube, Douyin | Action start hook |

**Track by Sunday April 26:** Three data points per series. Trends should be emerging.

### Week 4 (Monday April 27 - Sunday May 3, 2026)

| Day | Content | Platform | Hook Style |
|-----|---------|----------|------------|
| Tuesday Apr 28 | Puzzle #4: Double cannon checkmate | Douyin, Bilibili, YouTube | Question hook |
| Thursday Apr 30 | Famous Game #4: Lu Qin vs Wang Jialiang 1990 | Bilibili, YouTube | Bold claim hook |
| Saturday May 2 | Opening #4: Immortal Guide opening (仙人指路) | Bilibili, YouTube, Douyin | Action start hook |

**Track by Sunday May 3:** Full 4-week dataset complete.

### Analysis Day: Monday May 4, 2026

Fill out this scorecard:

```
SERIES SCORECARD -- 4 Week Test Results

Series A: Weekly Puzzle Challenge
- Total views (all platforms, all 4 episodes): ______
- Average completion rate: ______%
- Average likes per video: ______
- New subscribers attributed: ______
- Winner Score (avg completion x total views): ______

Series B: Famous Game Analysis
- Total views (all platforms, all 4 episodes): ______
- Average completion rate: ______%
- Average likes per video: ______
- New subscribers attributed: ______
- Winner Score (avg completion x total views): ______

Series C: Opening Tutorial
- Total views (all platforms, all 4 episodes): ______
- Average completion rate: ______%
- Average likes per video: ______
- New subscribers attributed: ______
- Winner Score (avg completion x total views): ______

WINNER: Series ____ (highest Winner Score)
RUNNER-UP: Series ____
UNDERPERFORMER: Series ____

DECISION:
- Move Series ____ to 2x/week starting May 5
- Keep Series ____ at 1x/week
- Reduce Series ____ to 1x/month
```

---

## Tracking Spreadsheet Setup

Create a spreadsheet (Google Sheets or Excel) with these columns:

| Column | Description |
|--------|-------------|
| Date | Upload date |
| Series | A, B, or C |
| Episode # | Sequential number |
| Title | Video title |
| Platform | Douyin / Bilibili / YouTube |
| Length (min) | Video duration |
| Hook Style | Question / Bold Claim / Action Start |
| Thumbnail Style | Board / Face / Text |
| Views (24h) | Views after 24 hours |
| Views (7d) | Views after 7 days |
| Completion % | Platform-reported completion rate |
| Avg Watch (min) | Average watch duration in minutes |
| Likes | Total likes |
| Comments | Total comments |
| New Subs | New subscribers from this video |
| Winner Score | Completion % x Views (7d) |
| Notes | Anything unusual (holiday, trending topic, etc.) |

Update this after every video. Review weekly on Mondays. Make strategic decisions monthly.

---

## Common Pitfalls to Avoid

1. **Testing too many things at once.** Change one variable per test cycle. If you change the hook AND the length AND the thumbnail, you cannot know which change caused the result.

2. **Giving up too early.** One bad video does not kill a series. Random variation is real. Always test for at least 4 weeks.

3. **Ignoring platform differences.** A series that flops on Douyin might thrive on Bilibili. Always check per-platform data, not just totals.

4. **Optimizing for vanity metrics.** Views alone mean nothing. A video with 100,000 views but 5% completion rate is actively harming your channel. Completion rate and subscriber conversion are what matter.

5. **Not killing losers.** Emotional attachment to a series format is natural. But if the data says it is not working after 4-8 weeks, let it go. Your time is finite and should go to what your audience actually wants.

6. **Forgetting external factors.** A video posted during a major xiangqi tournament will perform differently than one posted during a holiday. Note external factors in your spreadsheet.
