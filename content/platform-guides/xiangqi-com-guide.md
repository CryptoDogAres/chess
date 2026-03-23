# xiangqi.com Account and Analysis Setup

This guide covers how to set up and use xiangqi.com as a complementary analysis
and sharing tool for your Xiangqi content workflow. While board-art.html with a
local Pikafish engine server is the primary analysis environment, xiangqi.com
provides useful features for quick online analysis, position sharing, and
cross-referencing evaluations.

---

## 1. Account Creation

### Signing Up

1. Open your browser and navigate to **https://www.xiangqi.com**.
2. Click **Sign Up** or **Register** (注册) in the top-right corner of the page.
3. You can register with:
   - **Email:** Enter your email address and choose a password.
   - **Google account:** Click the Google sign-in button for one-tap
     registration.
   - **Social login:** Some versions support WeChat or other social logins
     depending on your region.
4. Choose a **username** that matches or is recognizable alongside your channel
   name. If your Douyin/YouTube channel is "象棋每日一题", consider a username
   like "xiangqi-daily" or similar.
5. Confirm your email address by clicking the verification link sent to your
   inbox.
6. Log in with your new credentials.

### Profile Setup

1. Go to your profile page (click your username or avatar in the top-right).
2. Upload a profile picture — use your channel logo for brand consistency.
3. Add a bio mentioning your channel: "象棋教学频道 — YouTube/Douyin/Bilibili"
   with links if the platform allows.
4. Set your preferred language to Chinese (中文) or English depending on your
   audience context. The analysis board works the same in both languages.

### Account Tiers

xiangqi.com may offer free and premium tiers. For content creation purposes:

- **Free tier** is sufficient for basic analysis, position loading, and sharing.
- **Premium/paid tier** (if available) may unlock deeper engine analysis, longer
  computation time, opening databases, or endgame tablebases.
- Evaluate whether premium features add value to your workflow before
  subscribing. Your local Pikafish setup already provides strong engine analysis.

---

## 2. Analysis Board Features

The analysis board is the core tool you will use on xiangqi.com. It provides a
web-based interface for exploring positions, running engine evaluation, and
annotating moves.

### Accessing the Analysis Board

1. From the xiangqi.com homepage, look for an **Analysis** or **Board Editor**
   link in the navigation menu.
2. Alternatively, navigate directly to the analysis URL (often something like
   `xiangqi.com/analysis` or `xiangqi.com/editor`).
3. You should see an empty Xiangqi board with the standard starting position.

### Loading a Position from FEN

FEN (Forsyth-Edwards Notation) is the standard way to describe a Xiangqi board
position as a text string.

**To paste a FEN and load a position:**

1. On the analysis board page, look for a **FEN input field**, often labeled
   "FEN" or "局面" or accessible via a **Setup** / **编辑** button.
2. Click the FEN input field.
3. Paste your FEN string. Example:
   ```
   rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w - - 0 1
   ```
4. Press **Enter** or click **Load** / **加载**.
5. The board should update to display the described position.

**Where to get FEN strings:**
- From board-art.html: the FEN is displayed in the interface and can be copied.
- From Pikafish analysis output: the engine logs include the current FEN.
- From game databases or PGN files: many tools convert PGN moves to FEN.

**Tip:** Keep a text file of FEN strings for positions you plan to analyze or
use in videos. This makes it easy to load them anywhere — xiangqi.com, board-art,
or any other compatible tool.

### Real-Time Engine Evaluation

xiangqi.com typically runs a server-side engine to evaluate the current position.

1. After loading a position, look for an **Analyze** or **Engine** button
   (often represented by a computer/CPU icon or labeled 分析/引擎).
2. Click to enable engine analysis.
3. The engine will display:
   - **Evaluation score:** A numerical assessment (positive = advantage for the
     side to move, or explicitly labeled for Red/Black).
   - **Best line (PV):** The principal variation — the engine's recommended
     sequence of moves.
   - **Depth:** How many moves ahead the engine has calculated.
4. The evaluation updates as the engine thinks deeper. Wait a few seconds for
   the evaluation to stabilize.

**Comparing with Pikafish:**
- xiangqi.com's engine may differ from your local Pikafish in strength and
  evaluation.
- Use xiangqi.com's evaluation as a cross-reference, not as the sole authority.
- If evaluations disagree significantly, investigate the position more deeply.
  The disagreement itself can be interesting content for analysis videos.

### Arrow and Highlight Drawing

Most xiangqi.com analysis boards support visual annotations.

**Drawing arrows:**
1. **Right-click** (or long-press on mobile) on the starting square of a piece.
2. While holding, **drag** to the destination square.
3. Release to draw an arrow from the origin to the destination.
4. The arrow typically appears in green by default.

**Drawing square highlights:**
1. **Right-click** on a single square (without dragging).
2. The square will be highlighted (usually in green or yellow).
3. Click again to cycle through colors or remove the highlight.

**Color modifiers (if supported):**
- **Right-click drag:** Green arrow (default)
- **Shift + right-click drag:** Red arrow
- **Ctrl + right-click drag:** Blue arrow
- **Alt + right-click drag:** Yellow arrow

These conventions follow the pattern established by lichess.org and similar
platforms. The exact modifiers may vary on xiangqi.com — experiment to confirm.

**Clearing annotations:**
- Right-click on an empty area of the board, or
- Look for a **Clear arrows** button in the toolbar, or
- Press **Escape** to clear all drawn arrows and highlights.

### Move Quality Symbols

When reviewing a game, xiangqi.com may allow you to annotate moves with standard
quality symbols:

| Symbol | Meaning | Chinese |
|--------|---------|---------|
| ! | Good move | 好棋 |
| !! | Brilliant move | 妙棋 |
| ? | Mistake | 失误 |
| ?? | Blunder | 漏着 |
| !? | Interesting move | 有趣的走法 |
| ?! | Dubious move | 可疑的走法 |

To add these annotations, look for a comment or annotation panel alongside the
move list. Click on a move, then select the appropriate symbol from a dropdown
or toolbar.

### Game Trend Charts

Some analysis platforms display a game trend chart — a graph showing the engine
evaluation over the course of the entire game.

1. After loading and analyzing a complete game (not just a single position),
   look for a **Graph** or **Trend** icon, often below the move list.
2. The chart displays:
   - X-axis: move number
   - Y-axis: engine evaluation (positive = Red advantage, negative = Black
     advantage)
   - The line shows how the advantage shifted throughout the game.
3. Peaks and valleys in the chart indicate critical moments — mistakes, blunders,
   or brilliant moves.
4. Click on any point in the chart to jump to that position on the board.

**Content use:** Screenshots of the game trend chart make excellent visuals for
analysis videos. They give viewers an immediate overview of the game's flow
before you dive into specific positions.

---

## 3. Using xiangqi.com Alongside Our Tools

xiangqi.com is one tool in a larger workflow. Here is how it fits in.

### Primary Analysis: board-art.html + Pikafish

Your main analysis environment remains:
- **board-art.html** for board visualization, annotation, and recording.
- **Local Pikafish engine** for deep analysis with full hardware utilization.
- This combination gives you the most control, the strongest analysis, and the
  best recording workflow.

### When to Use xiangqi.com Instead

**Quick analysis on the go:**
- When you are away from your desktop and want to check a position on your
  phone or a different computer.
- xiangqi.com works in any browser — no local setup needed.

**Cross-checking evaluations:**
- After analyzing a position with Pikafish, load the same FEN on xiangqi.com
  to see if their engine agrees.
- Disagreements can reveal interesting nuances in the position.
- If both engines agree on the evaluation, you can be more confident in your
  analysis.

**Sharing positions with collaborators:**
- When discussing positions with other Xiangqi players or content creators,
  xiangqi.com provides shareable links (see section 4 below).
- This is much easier than sending FEN strings and asking others to set up a
  local board.

**Accessing opening databases:**
- If xiangqi.com provides an opening book or database, use it to research
  opening theory for your analysis videos.
- Compare the database moves with your Pikafish recommendations.

### Workflow Integration

A typical analysis session might look like this:

1. Load the game in board-art.html with Pikafish for primary analysis.
2. Identify the 3-5 critical positions in the game.
3. For each critical position, also check it on xiangqi.com to cross-reference.
4. If xiangqi.com has a game trend chart, screenshot it for the video intro.
5. Use xiangqi.com's shareable links in your video description so viewers can
   explore positions themselves.
6. Record the analysis video from board-art.html (using OBS).

---

## 4. Sharing Positions

One of xiangqi.com's most useful features for content creators is the ability
to create shareable links to specific positions.

### Creating a Shareable Link

1. Load the position you want to share on the analysis board.
2. Look for a **Share** button (often an icon that looks like a chain link,
   an arrow, or is labeled 分享/Share).
3. Click it to generate a URL.
4. Copy the URL.

The URL typically encodes the FEN in the query string, so anyone who opens it
will see the exact position you set up.

### Where to Use Shareable Links

**Video descriptions:**
Include links to key positions from your analysis videos. Example YouTube
description:

```
关键局面链接 / Key Position Links:
第15回合 红方弃车: https://www.xiangqi.com/analysis?fen=...
第23回合 黑方漏着: https://www.xiangqi.com/analysis?fen=...
最终局面: https://www.xiangqi.com/analysis?fen=...
```

**Social media posts:**
Share a puzzle position on Weibo, Twitter, or in Xiangqi forums with a link
that lets viewers try solving it interactively.

**Community engagement:**
Post a link in your video comments or Discord/WeChat group and ask viewers to
find the best move. This drives engagement and encourages viewers to interact
with the position rather than just watching passively.

### Embedding (if available)

Some platforms offer embed codes (iframe) that let you place an interactive
board directly on a webpage or blog post. Check xiangqi.com's share options
for an embed or iframe option.

---

## 5. Study Feature

The study feature (if available on xiangqi.com) lets you create, annotate, and
save collections of analyzed positions and games.

### Creating a Study

1. Look for a **Studies** or **Learn** section in the site navigation, or check
   if the analysis board has a **Save** or **Create Study** option.
2. Click **New Study** or **创建研究**.
3. Give it a name, such as "中炮对屏风马 — 常见变例" (Central Cannon vs Screen
   Horse — Common Variations).
4. Set visibility: **Public** if you want to share with viewers, **Private** if
   it is for your own reference.

### Adding Chapters to a Study

Studies are typically organized into chapters, each focusing on a specific
position or variation.

1. Within the study, click **Add Chapter** or **添加章节**.
2. Name the chapter descriptively: "第一变：红方先手攻杀" (Variation 1: Red's
   First-Move Attack).
3. Set up the starting position — either the standard starting position or a
   custom FEN.
4. Add moves by clicking on the board. Each move is recorded in the move list.
5. Add **comments** and **annotations** to individual moves:
   - Click on a move in the move list.
   - Type your commentary in the comment field.
   - Add move quality symbols (!, ?, !!, ??) as described in section 2.
6. Add **branching variations** by going back to an earlier move and playing a
   different continuation. The study should create a branching tree of moves.

### Saving and Organizing Studies

1. Click **Save** or the study auto-saves as you work (platform-dependent).
2. Organize studies by topic:
   - Opening studies: one study per opening system you cover.
   - Tactical studies: collections of puzzles grouped by theme (smothered mate,
     double check, sacrifice patterns).
   - Game analysis studies: one study per notable game you analyze.

### Using Studies for Content Creation

**As a preparation tool:**
- Before recording a video, create a study with all the positions and
  variations you plan to cover.
- This serves as your script outline — you know exactly which positions to show
  and what to say about each one.
- During recording, keep the study open in a browser tab for quick reference.

**As viewer resources:**
- Share the study link in your video description.
- Viewers can step through your analysis at their own pace, replay variations,
  and run their own engine analysis on interesting positions.
- This adds significant value beyond the video itself.

**As a collaboration tool:**
- If the platform supports it, invite collaborators to edit a study.
- Work with other Xiangqi content creators to build comprehensive opening
  guides or puzzle collections.

---

## Platform Comparison: xiangqi.com vs Local Tools

| Feature | xiangqi.com | board-art.html + Pikafish |
|---------|------------|--------------------------|
| Setup required | None (browser only) | Local server and files |
| Engine strength | Server-dependent | Full local hardware |
| Analysis depth | Limited by server | Unlimited (your CPU) |
| Recording workflow | Separate screen capture needed | Integrated with OBS |
| Annotation tools | Built-in arrows/highlights | Built-in + Premiere post-production |
| Sharing positions | One-click shareable links | Must share FEN manually |
| Offline access | No (requires internet) | Yes |
| Study/save feature | Built-in studies | Save as FEN/PGN files |
| Mobile access | Yes (responsive browser) | Limited |
| Cost | Free / optional premium | Free |

**Recommendation:** Use both tools. board-art.html + Pikafish for deep analysis
and video recording, xiangqi.com for sharing, quick checks, and mobile access.

---

## Quick Start Checklist

Use this checklist when setting up xiangqi.com for the first time:

- [ ] Account created and email verified
- [ ] Profile picture uploaded (channel logo)
- [ ] Bio includes channel name and platform links
- [ ] Successfully loaded a test FEN on the analysis board
- [ ] Engine analysis tested — evaluation and best line displayed
- [ ] Arrow drawing tested (right-click drag)
- [ ] Created a shareable link for a test position
- [ ] Bookmarked the analysis board URL for quick access
- [ ] Created a test study with at least one chapter
- [ ] Compared a position's evaluation between xiangqi.com and local Pikafish

---

## Troubleshooting

**FEN does not load or board shows an error:**
- Verify the FEN string is valid Xiangqi FEN (not international chess FEN).
- Xiangqi FEN uses: R, N, B, A, K, C, P for Red pieces and r, n, b, a, k, c, p
  for Black pieces. The letter "C" represents the Cannon, which does not exist
  in international chess FEN.
- Check for extra spaces or missing characters in the FEN string.

**Engine analysis is slow or unavailable:**
- Server-side engines depend on the platform's servers. During peak hours,
  analysis may be slower.
- If analysis is consistently slow, rely on your local Pikafish for depth and
  use xiangqi.com only for sharing and quick checks.

**Cannot draw arrows on mobile:**
- On touchscreens, long-press on the starting square, then drag to the
  destination.
- Some mobile browsers may intercept the gesture. Try using the platform's
  mobile app if one is available.

**Shared link does not show the correct position:**
- Some share links may expire or be session-dependent.
- Always test a shared link in an incognito/private browser window before
  publishing it in a video description.
- If links are unreliable, include the FEN string as text in addition to the
  link, so viewers can manually load the position.
