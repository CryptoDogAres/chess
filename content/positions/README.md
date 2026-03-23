# Position Collection Index

A curated collection of 85 famous Chinese chess (Xiangqi) positions for study, training, and analysis.

## Collection Summary

| File | Count | Category | Difficulty Range |
|------|-------|----------|-----------------|
| `classic-endgames.txt` | 30 | Ancient manual compositions | ★★ - ★★★★★ |
| `famous-game-moments.txt` | 20 | Tournament critical moments | ★★★ - ★★★★★ |
| `tactical-puzzles.txt` | 20 | Checkmate puzzles | ★ - ★★★★★ |
| `opening-positions.txt` | 15 | Opening theory positions | ★★ - ★★★ |
| **Total** | **85** | | |

## Sources

### Ancient Manuals
- **适情雅趣** (Elegant Pastime Manual, 1570) — Ming Dynasty endgame collection
- **桔中秘** (Secret Inside the Orange, 1632) — Ming Dynasty tactical and strategic manual
- **梅花谱** (Plum Blossom Manual, 1670) — Qing Dynasty opening and middlegame treatise
- **反梅花谱** (Anti-Plum Blossom Manual) — Qing Dynasty counter-strategies

### Professional Players Featured
- 胡荣华 (Hu Ronghua) — 14-time National Champion
- 许银川 (Xu Yinchuan) — Multiple-time National Champion
- 王天一 (Wang Tianyi) — Modern era dominant player
- 吕钦 (Lu Qin) — Known for aggressive attacking style
- 杨官璘 (Yang Guanlin) — Founding era master
- 李来群 (Li Laiqun) — Renowned for defensive technique

## FEN Format

All positions use standard Xiangqi FEN notation:

- **Uppercase** = Red pieces: `R`(Rook), `N`(Knight/Horse), `B`(Bishop/Elephant), `A`(Advisor), `K`(King), `C`(Cannon), `P`(Pawn)
- **Lowercase** = Black pieces: `r`, `n`, `b`, `a`, `k`, `c`, `p`
- Numbers represent consecutive empty squares
- `/` separates rows (10 rows total, from Black's back rank to Red's back rank)
- Space followed by `w` (Red to move) or `b` (Black to move)

## How to Use

### Interactive Board Visualization
Load any FEN into the project's web tools:
- **board-art.html** — Render the position as a visual board
- **explain.html** — Get AI-powered explanations of the position
- **analyze.html** — Run engine analysis on the position

### Batch Analysis
Run engine analysis on an entire file of positions:
```bash
python3 engine/analyze.py --file positions/tactical-puzzles.txt
```

### Daily Puzzle Posts
Use positions from `tactical-puzzles.txt` for daily puzzle posts on community channels. The difficulty ratings help schedule appropriate challenges:
- Monday-Tuesday: ★ - ★★ (Mate in 1)
- Wednesday-Thursday: ★★★ (Mate in 2)
- Friday: ★★★★ (Mate in 3)
- Weekend: ★★★★★ (Mate in 4-5)

### Study Plans
- **Beginners**: Start with `tactical-puzzles.txt` Mate-in-1 section, then study `opening-positions.txt`
- **Intermediate**: Work through `classic-endgames.txt` and Mate-in-2/3 puzzles
- **Advanced**: Study `famous-game-moments.txt` and attempt Mate-in-4-5 expert puzzles
