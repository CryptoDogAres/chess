# Practice Position Files for Beginner Tutorial Series

# 象棋零基础教程练习局面文件索引

Downloadable FEN practice positions for all 12 episodes. Each file contains Xiangqi FEN strings with bilingual descriptions (Chinese + English). Load these into any Xiangqi software or website that supports FEN to practice on the board.

每集对应一个练习文件，包含象棋FEN字符串和中英文双语说明。可导入任何支持FEN的象棋软件或网站进行练习。

---

## File Index / 文件索引

| File | Episode | Topic (EN) | Topic (CN) | Positions |
|------|---------|------------|------------|-----------|
| `ep01-rules-positions.txt` | Ep 01 | Rules & Board | 规则与棋盘 | 5 |
| `ep02-pieces1-positions.txt` | Ep 02 | Chariot, Horse, Cannon | 车马炮 | 8 |
| `ep03-pieces2-positions.txt` | Ep 03 | Pawn, Advisor, Elephant, King | 兵士象帅 | 8 |
| `ep04-basic-kills1-positions.txt` | Ep 04 | Horse-Behind-Cannon & Heaven-Earth Cannons | 马后炮与天地炮 | 6 |
| `ep05-basic-kills2-positions.txt` | Ep 05 | Smothered Mate, Iron Door Bolt & Double Cannon | 闷宫、铁门栓与重炮 | 6 |
| `ep06-opening-positions.txt` | Ep 06 | Opening Principles | 开局原则 | 5 |
| `ep07-openings-positions.txt` | Ep 07 | 5 Popular Openings | 五大常见开局 | 5 |
| `ep08-tactics-positions.txt` | Ep 08 | Discovered Check, Pins, Forks & Discovered Attacks | 抽将、牵制、捉双与闪击 | 8 |
| `ep09-coordination-positions.txt` | Ep 09 | Chariot-Horse, Chariot-Cannon, Horse-Cannon Combos | 车马、车炮、马炮配合 | 6 |
| `ep10-endgame-basics-positions.txt` | Ep 10 | Chariot Endgames | 车的残局 | 6 |
| `ep11-endgame-advanced-positions.txt` | Ep 11 | Horse & Cannon Endgames | 马炮残局 | 6 |
| `ep12-full-game-positions.txt` | Ep 12 | Full Game Analysis | 完整对局分析 | 8 |

**Total: 77 practice positions across 12 files**

---

## FEN Format / FEN格式说明

Each line follows this format:

```
FEN_STRING # Description 说明
```

- Lines starting with `#` are comments
- FEN uses standard Xiangqi notation: uppercase = Red, lowercase = Black
- Piece letters: R=Chariot, H=Horse, E=Elephant, A=Advisor, K=King, C=Cannon, P=Pawn
- `w` = Red to move, `b` = Black to move

## How to Use / 使用方法

1. Open any Xiangqi application that supports FEN import
2. Copy a FEN string (everything before the `#` comment)
3. Paste it into the FEN import field
4. Study the position and try to find the best move before reading the description
