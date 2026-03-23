# Monthly Tournament Format / 月赛规则

## Task: cc6 — 棋道 ChessDAO Monthly Tournament

---

## Tournament Overview / 锦标赛概述

| Item | Details |
|------|---------|
| Name | 棋道月赛 / ChessDAO Monthly |
| Frequency | Monthly, 1st Saturday of each month / 每月第一个周六 |
| Format | Swiss System, 5 rounds / 瑞士制，5轮 |
| Time Control | 15 min + 5 sec increment / 15分钟 + 每步加5秒 |
| Platform | 天天象棋 or xiangqi.com / 天天象棋或弈天 |
| Entry | Free / 免费 |
| Max Participants | 32 (expandable) / 32人（可扩展） |

---

## Schedule / 时间安排

| Phase | Time (CST / 北京时间) |
|-------|------|
| Registration Opens | 7 days before tournament / 赛前7天开始报名 |
| Registration Closes | 1 day before, 23:59 / 赛前1天 23:59 截止 |
| Round 1 | Saturday 14:00 / 周六 14:00 |
| Round 2 | Saturday 14:45 / 周六 14:45 |
| Round 3 | Saturday 15:30 / 周六 15:30 |
| Break | Saturday 16:15–16:30 / 周六 16:15–16:30 休息 |
| Round 4 | Saturday 16:30 / 周六 16:30 |
| Round 5 | Saturday 17:15 / 周六 17:15 |
| Results & Awards | Saturday 18:00 / 周六 18:00 |

---

## Swiss System Rules / 瑞士制规则

1. **Pairing / 配对:** Players with the same score are paired together. No rematches. / 相同积分的选手配对，不重复对局。
2. **Scoring / 计分:**
   - Win / 胜: **3 points / 3分**
   - Draw / 和: **1 point / 1分**
   - Loss / 负: **0 points / 0分**
3. **Tiebreakers / 决胜规则（同分时）:**
   1. Head-to-head result / 直接对局结果
   2. Buchholz score (sum of opponents' scores) / 布赫兹分（对手积分之和）
   3. Number of wins / 胜局数
   4. Armageddon game (if needed for prizes) / 加赛（如需决定奖项）
4. **Byes / 轮空:** Odd number of players = lowest-ranked player gets a 1-point bye (max 1 per tournament). / 单数选手时，排名最低者轮空得1分（每人最多1次）。
5. **No-show / 弃权:** 10 minutes late = forfeit. / 迟到10分钟判负。

---

## Prizes / 奖励

| Place | Prize |
|-------|-------|
| 1st / 冠军 | 🏆 大师 Master Discord role + video shoutout + custom emoji / 大师身份 + 视频提及 + 自定义表情 |
| 2nd / 亚军 | 🥈 Video shoutout + custom emoji / 视频提及 + 自定义表情 |
| 3rd / 季军 | 🥉 Video shoutout / 视频提及 |
| Best Newcomer / 最佳新人 | Special mention in video / 视频特别提及 |

**Video shoutout:** Winner will be mentioned and their best game analyzed in the next video. / 获奖者将在下期视频中被提及，并分析其最佳对局。

---

## Registration / 报名

### Registration Command / 报名命令

Players register by posting in `#tournament` using the template below:

```
!register
```

Bot responds with a DM containing the registration form. Player replies with:

```
报名 / Registration

Discord 用户名 / Discord Username: @YourName
天天象棋 ID / Xiangqi App ID: your_id_here
当前等级 / Current Rating: (if known)
参赛经验 / Tournament Experience: 新手/有经验 (Beginner/Experienced)
```

### Registration Confirmation Message (Bot auto-reply) / 报名确认消息

```
✅ 报名成功！/ Registration confirmed!

选手 / Player: {user}
编号 / Number: #{number}

请在比赛当天 13:50 (CST) 前上线。
Please be online by 13:50 (CST) on tournament day.

祝你好运！/ Good luck!
```

---

## Match Reporting / 对局上报

After each game, BOTH players report the result in `#tournament`:

```
第_轮结果 / Round _ Result:
红方 / Red: @Player1
黑方 / Black: @Player2
结果 / Result: 红胜/黑胜/和棋 (Red wins / Black wins / Draw)
截图 / Screenshot: [attach game result screenshot]
```

**Important / 重要:**
- Both players must confirm the result / 双方都需确认结果
- Attach a screenshot of the final position or result screen / 附上最终局面或结果截图
- Disputes are resolved by moderators reviewing the screenshot / 争议由管理员查看截图裁决

---

## Bracket Tracking / 对阵表追踪

### Option 1: Google Sheets (Recommended) / 谷歌表格（推荐）

Create a shared Google Sheet with the following tabs:

**Tab 1: Participants / 选手名单**

| # | Discord | 天天象棋 ID | Rating | Score | W | D | L | Buchholz |
|---|---------|------------|--------|-------|---|---|---|----------|
| 1 | @Player1 | xxx | 1500 | 0 | 0 | 0 | 0 | 0 |

**Tab 2: Round 1 / 第一轮**

| Board | Red / 红方 | Black / 黑方 | Result / 结果 |
|-------|-----------|-------------|--------------|
| 1 | @Player1 | @Player2 | — |

(Repeat for Rounds 2–5)

**Tab 3: Final Standings / 最终排名**

| Rank | Player | Score | Buchholz | Wins |
|------|--------|-------|----------|------|
| 1 | @Player1 | 15 | 42 | 5 |

Share the Google Sheet link in `#tournament` channel, pinned.

### Option 2: Challonge / Challonge 在线对阵

1. Go to https://challonge.com/
2. Create a new Swiss tournament
3. Name: "棋道月赛 YYYY-MM / ChessDAO Monthly YYYY-MM"
4. Set to 5 rounds, Swiss format
5. Share the Challonge link in `#tournament`

---

## Announcement Templates / 公告模板

### Tournament Announcement (Post in #announcements and #tournament) / 赛前公告

```
🏆 棋道月赛 — [Month Year] / ChessDAO Monthly — [Month Year]

📅 日期 / Date: [1st Saturday], 14:00–18:00 CST
♟️ 赛制 / Format: 瑞士制5轮 / Swiss 5 rounds
⏱️ 用时 / Time: 15+5
🎮 平台 / Platform: 天天象棋 / xiangqi.com
👥 名额 / Spots: 32

🏆 奖励 / Prizes:
- 冠军: 大师身份 + 视频提及 / 1st: Master role + video shoutout
- 亚军: 视频提及 / 2nd: Video shoutout
- 季军: 视频提及 / 3rd: Video shoutout

📝 报名 / Register: 在本频道输入 `!register` / Type `!register` in this channel
📅 截止 / Deadline: [Day before], 23:59 CST

@锦标赛 祝各位好运！/ Good luck everyone!
```

---

### Round Start Announcement / 每轮开始公告

```
⚔️ 第{N}轮开始！/ Round {N} Start!

对阵表 / Pairings:
Board 1: @Player1 (红/Red) vs @Player2 (黑/Black)
Board 2: @Player3 (红/Red) vs @Player4 (黑/Black)
...

⏱️ 用时 / Time: 15+5
📝 完成后请上报结果 / Report results when finished

开始！/ Begin!
```

---

### Tournament Results Announcement / 赛后公告

```
🏆 棋道月赛 [Month Year] 结果 / ChessDAO Monthly [Month Year] Results

🥇 冠军 / Champion: @Player1 — {score} 分/pts
🥈 亚军 / Runner-up: @Player2 — {score} 分/pts
🥉 季军 / 3rd Place: @Player3 — {score} 分/pts
⭐ 最佳新人 / Best Newcomer: @Player4

完整排名 / Full standings: [Google Sheet / Challonge link]

恭喜所有参赛者！下月再战！
Congratulations to all participants! See you next month!

冠军的最佳对局将在下期视频中分析！
The champion's best game will be analyzed in the next video!
```

---

## Moderator Checklist / 管理员检查清单

### 7 Days Before / 赛前7天
- [ ] Create tournament bracket (Google Sheet or Challonge) / 创建对阵表
- [ ] Post announcement in #announcements and #tournament / 发布公告
- [ ] Pin the announcement / 置顶公告

### 1 Day Before / 赛前1天
- [ ] Close registration at 23:59 / 23:59 截止报名
- [ ] Finalize participant list / 确定参赛名单
- [ ] Generate Round 1 pairings / 生成第一轮配对
- [ ] DM all participants with schedule reminder / 私信提醒所有参赛者

### Tournament Day / 比赛当天
- [ ] Post Round 1 pairings at 13:50 / 13:50 发布第一轮配对
- [ ] Monitor results and update bracket after each round / 每轮更新对阵表
- [ ] Generate next round pairings after all results are in / 所有结果上报后生成下轮配对
- [ ] Handle disputes promptly / 及时处理争议
- [ ] Post final results and congratulations / 发布最终结果和祝贺

### After Tournament / 赛后
- [ ] Assign 🏆 大师 Master role to winner (if earned) / 给冠军分配大师身份
- [ ] Update tournament history / 更新锦标赛历史记录
- [ ] Share best game with content team for video analysis / 分享最佳对局供视频分析
- [ ] Collect feedback for improvements / 收集改进建议
