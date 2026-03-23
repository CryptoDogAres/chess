# 第一集：象棋入门——规则与棋盘

# Episode 01: Getting Started — Rules & Board

**时长 Duration:** 约10分钟 (~10 min)
**平台 Platform:** Bilibili / YouTube
**系列 Series:** 象棋零基础教程 (Chinese Chess Beginner Tutorial) — Episode 1 of 12

---

## 本集概要 Episode Overview

这是整个系列的第一课。我们从最基本的开始：棋盘长什么样？棋子怎么摆？怎样算赢？不用任何专业术语，像聊天一样把规则讲清楚。

This is the very first lesson. We start from the absolute basics: what does the board look like? How do you set up the pieces? How do you win? No jargon — just a friendly conversation about the rules.

---

## 详细大纲 Detailed Outline

### 第一节：棋盘是什么样的 (The Board Layout) — 约3分钟

**核心要点 Key Talking Points:**

1. **棋盘的格子 (The Grid)**
   - 棋盘由9条竖线和10条横线组成，棋子走在交叉点上，不是格子里面
   - (The board has 9 vertical lines and 10 horizontal lines. Pieces go on the intersections, not inside the squares.)
   - 一共有90个交叉点，这就是棋子可以站的地方
   - (There are 90 intersections — these are where pieces can stand.)

2. **楚河汉界 (The River)**
   - 棋盘中间有一条"河"，把棋盘分成两半
   - (A "river" in the middle divides the board into two halves.)
   - 这条河会影响某些棋子的走法——有些棋子不能过河
   - (The river affects how some pieces move — some pieces cannot cross it.)
   - 历史小故事：楚河汉界来自楚汉争霸的历史 (Historical tidbit: the river references the Chu-Han war.)

3. **九宫格 (The Palace)**
   - 棋盘两端各有一个"九宫格"，画着斜线的3x3区域
   - (Each side has a "palace" — a 3x3 area with diagonal lines.)
   - 将/帅和士/仕只能在九宫格里面活动
   - (The King and Advisors can only move within the palace.)

**示例棋局 Example Position 1 — 空棋盘标注：**

```
FEN: 9/9/9/9/9/9/9/9/9/9 w - - 0 1
```
（用空棋盘标注河、九宫等关键区域）
(Use an empty board to highlight the river, palaces, and key areas.)

### 第二节：棋子怎么摆 (How to Set Up Pieces) — 约3分钟

**核心要点 Key Talking Points:**

1. **两方各有16个棋子 (Each Side Has 16 Pieces)**
   - 红方和黑方各16枚，共32枚棋子
   - (Red and Black each have 16 pieces, 32 total.)
   - 红方先走——就像国际象棋白方先走一样
   - (Red moves first — like White in international chess.)

2. **棋子种类与数量 (Piece Types and Counts)**
   - 帅/将 ×1（国王）— King ×1
   - 仕/士 ×2（侍卫）— Advisor ×2
   - 相/象 ×2（大象）— Elephant ×2
   - 马 ×2（马）— Horse ×2
   - 车 ×2（战车）— Chariot ×2
   - 炮 ×2（大炮）— Cannon ×2
   - 兵/卒 ×5（小兵）— Pawn ×5

3. **标准开局摆法 (Standard Starting Position)**
   - 从底线中间开始：帅在正中间
   - (Start from the back row center: King in the exact middle.)
   - 往两边依次是：士、象、马、车
   - (Moving outward: Advisor, Elephant, Horse, Chariot.)
   - 炮在第三行，兵在第四行，隔一个点放一个
   - (Cannons on the third row, Pawns on the fourth row, every other intersection.)

**示例棋局 Example Position 2 — 标准开局：**

```
FEN: rheakaehr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RHEAKAEHR w - - 0 1
```
（标准开局位置，红方在下，黑方在上）
(Standard starting position, Red at bottom, Black at top.)

### 第三节：基本规则 (Basic Rules) — 约2.5分钟

**核心要点 Key Talking Points:**

1. **轮流走棋 (Taking Turns)**
   - 红方先走，然后黑方，然后红方……交替进行
   - (Red goes first, then Black, then Red... alternating turns.)
   - 每次只能走一步，不能跳过
   - (One move per turn, no skipping.)

2. **吃子 (Capturing)**
   - 把你的棋子走到对方棋子的位置，就把它吃掉了
   - (Move your piece to an opponent's piece's position to capture it.)
   - 吃掉的棋子从棋盘上拿走，不能再用
   - (Captured pieces are removed from the board permanently.)

3. **将军 (Check)**
   - 当你的棋子威胁到对方的将/帅时，就叫"将军"
   - (When your piece threatens the opponent's King, that's called "check".)
   - 被将军的一方必须马上应对，不能不管
   - (The checked side must respond immediately — you can't ignore it.)

4. **应将的三种方法 (Three Ways to Answer Check)**
   - 躲开：把将/帅移到安全的地方 (Move: move the King to safety.)
   - 挡住：用别的棋子挡在中间 (Block: put another piece in the way.)
   - 吃掉：把威胁你的棋子吃掉 (Capture: take the piece that's checking you.)

**示例棋局 Example Position 3 — 简单将军局面：**

```
FEN: 3aka3/9/9/9/9/9/9/9/1R7/4K4 w - - 0 1
```
（红车在b2位置，展示将军的概念）
(Red Chariot on b2, demonstrating the concept of check.)

### 第四节：怎样算赢 (How to Win) — 约1.5分钟

**核心要点 Key Talking Points:**

1. **将杀 = 胜利 (Checkmate = Victory)**
   - 对方被将军，而且无论怎么走都逃不掉——这就是"将杀"，你赢了
   - (The opponent is in check and has no legal way to escape — that's "checkmate," you win.)

2. **困毙 (Stalemate)**
   - 在象棋里，如果轮到你走但你没有合法的棋可走，你就输了
   - (In Chinese chess, if it's your turn but you have no legal moves, you LOSE.)
   - 注意：这和国际象棋不一样！国际象棋里无棋可走是和棋
   - (Note: this is different from international chess, where stalemate is a draw!)

3. **和棋 (Draw)**
   - 双方都无法取胜时可以和棋
   - (When neither side can win, it's a draw.)
   - 初学者不用太纠结和棋规则，先学会赢棋
   - (Beginners don't need to worry too much about draw rules — focus on winning first.)

**示例棋局 Example Position 4 — 简单将杀：**

```
FEN: 3k5/4a4/9/9/9/9/9/4R4/9/4K4 w - - 0 1
```
（红车将杀黑方的简单示例）
(Simple example of Red Chariot delivering checkmate.)

**示例棋局 Example Position 5 — 困毙示例：**

```
FEN: 3k5/9/4R4/9/9/9/9/9/9/4K4 b - - 0 1
```
（黑方无合法走法，困毙输棋）
(Black has no legal moves — stalemate, Black loses.)

---

## 练习题 Practice Puzzle

**问题：请看下面这个局面，红方走一步能将杀吗？**
(Question: In the following position, can Red checkmate in one move?)

```
FEN: 4k4/4a4/9/9/9/9/9/4R4/9/4K4 w - - 0 1
```

**提示 Hint:** 想想车可以走到哪一条线上，让黑方的将无处可逃。
(Think about which line the Chariot can move to so the Black King has nowhere to run.)

**答案 Answer:** 车e8进7（车走到e9），黑将被将杀。将无法移动，士挡不住。
(Chariot advances to e9 — checkmate. The King cannot move, the Advisor cannot block.)

---

## 本集总结 Key Takeaways

1. **棋盘** 有90个交叉点，中间有河，两端有九宫格
   (The board has 90 intersections, a river in the middle, and palaces on each end.)
2. **每方16子**，一共七种棋子
   (Each side has 16 pieces across seven types.)
3. **轮流走棋**，红先行
   (Players alternate turns; Red goes first.)
4. **将杀对方的将/帅就赢了**，被困住无棋可走也算输
   (Checkmate the opponent's King to win; having no legal moves also means you lose.)

---

## 下集预告 Next Episode Preview

下一集，我们来认识三个最厉害的棋子——**车、马、炮**！车为什么是最强的？马怎么走那个奇怪的L形？炮的"翻山"吃法是怎么回事？我们一个一个讲清楚。

Next time, we'll meet the three most powerful pieces — **Chariot, Horse, and Cannon**! Why is the Chariot the strongest? How does the Horse move in that strange L-shape? What's the Cannon's unique "jump-over" capture? We'll explain each one clearly.
