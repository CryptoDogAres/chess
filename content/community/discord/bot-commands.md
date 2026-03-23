# Discord Bot Setup / Discord 机器人设置

## Recommended Bots / 推荐机器人

---

## Option A: MEE6 (Recommended for simplicity / 推荐，简单易用)

### Installation / 安装
1. Go to https://mee6.xyz/
2. Click **"Add to Discord"**
3. Select the **棋道 ChessDAO** server
4. Authorize the bot

### Configuration / 配置

#### Welcome Plugin / 欢迎插件
- Enable **Welcome** plugin
- Welcome channel: `#welcome`
- Welcome message (DM to new members):

```
欢迎加入 棋道 ChessDAO！🏯
Welcome to 棋道 ChessDAO!

请先阅读 #welcome 和 #rules 频道。
Please read the #welcome and #rules channels first.

然后在 #introductions 自我介绍，开始你的象棋之旅！
Then introduce yourself in #introductions and start your xiangqi journey!

📺 YouTube: [链接/Link TBD]
📱 抖音 Douyin: [链接/Link TBD]
📺 哔哩哔哩 Bilibili: [链接/Link TBD]
```

- Join role: **🔴 红方 Red Side**

#### Leveling Plugin / 等级插件
- Enable **Leveling** plugin
- Level-up announcement channel: `#general-chat`
- Level-up message:

```
恭喜 {user} 升到等级 {level}！🎉
Congratulations {user}, you reached level {level}!
```

- Role rewards:
  | Level | Role |
  |-------|------|
  | 3 | 🟡 棋手 Player |

- XP rate: Default (15-25 XP per message, 60s cooldown)
- No XP channels: `#bot-commands`, `#memes`

#### Reaction Roles Plugin / 表情反应身份插件
- Enable **Reaction Roles** plugin
- Create in `#roles` channel
- See `roles.md` for the reaction role message and mappings

#### Moderator Plugin / 管理插件
- Enable **Moderator** plugin
- Mod log channel: Create a private `#mod-log` channel (visible only to moderators)
- Auto-mod rules:
  - Ban words: (configure as needed)
  - Anti-spam: Enable
  - Anti-link: Enable for new members (🔴 红方 Red Side only)

---

## Option B: Carl-bot (Recommended for advanced features / 推荐，功能更强)

### Installation / 安装
1. Go to https://carl.gg/
2. Click **"Invite"**
3. Select the **棋道 ChessDAO** server
4. Authorize the bot

### Configuration / 配置

#### Reaction Roles / 表情反应身份
Carl-bot has more flexible reaction roles than MEE6.

1. Go to Carl-bot dashboard → Reaction Roles
2. Create a new reaction role group in `#roles`
3. Add the notification role mappings from `roles.md`
4. Mode: **Toggle** (click to add/remove)

#### Welcome / 欢迎
- Same DM message as MEE6 section above
- Auto-role on join: **🔴 红方 Red Side**

#### Automod / 自动审核
- Configure anti-spam, anti-raid, word filters
- Log to private `#mod-log` channel

---

## Custom Bot Commands / 自定义机器人命令

Set up the following custom commands using MEE6 or Carl-bot:

### !puzzle / 今日谜题

**Description:** Show today's daily puzzle / 显示今日谜题
**Response:**

```
♟️ 今日谜题 / Today's Puzzle
{puzzle_content}

在 #daily-puzzle 中查看完整题目和讨论！
Check #daily-puzzle for the full puzzle and discussion!
```

**Note:** This will need to be updated daily. Consider using a scheduled message bot or manual daily posting. For automation, see the scheduling section below.

---

### !fen [fen_string]

**Description:** Generate a board image from a FEN string / 根据 FEN 字符串生成棋盘图片
**Response:**

```
棋盘链接 / Board link:
https://www.xiangqi.com/fen/{fen_string}

(如果链接无效，请检查 FEN 格式)
(If the link doesn't work, check the FEN format)
```

**Note:** Replace with a working xiangqi FEN visualization URL. Alternatives:
- `https://play.xiangqi.com/#/fen/{fen_string}`
- Or use a self-hosted board image API

---

### !rank

**Description:** Show the user's current role and level / 显示用户当前身份和等级
**Response (MEE6):**

```
{user} 的信息 / {user}'s info:
身份 / Role: {role}
等级 / Level: {level}
经验 / XP: {xp}
排名 / Rank: {rank}

继续加油！/ Keep it up!
```

**Note:** MEE6 has a built-in `!rank` command. Just enable the Leveling plugin.

---

### !help / 帮助

**Description:** Show available commands / 显示可用命令
**Response:**

```
棋道 ChessDAO 命令列表 / Command List:

♟️ 象棋 / Xiangqi:
  !puzzle — 今日谜题 / Today's puzzle
  !fen [FEN] — 生成棋盘图 / Generate board image

📊 个人信息 / Profile:
  !rank — 查看等级和排名 / View level and rank

🏆 锦标赛 / Tournament:
  !tournament — 当前锦标赛信息 / Current tournament info
  !register — 报名参赛 / Register for tournament

ℹ️ 其他 / Other:
  !help — 显示此列表 / Show this list
  !links — 平台链接 / Platform links
```

---

### !links / 链接

**Description:** Show all platform links / 显示所有平台链接
**Response:**

```
棋道 ChessDAO 平台链接 / Platform Links:

📺 YouTube: [链接/Link TBD]
📱 抖音 Douyin: [链接/Link TBD]
📺 哔哩哔哩 Bilibili: [链接/Link TBD]
💬 Discord: 你已经在这里了！/ You're already here!
```

---

### !tournament / 锦标赛

**Description:** Show current tournament info / 显示当前锦标赛信息
**Response:**

```
🏆 棋道月赛 / ChessDAO Monthly Tournament

状态 / Status: [报名中/进行中/已结束]
日期 / Date: [TBD]
参赛人数 / Participants: [TBD]
平台 / Platform: 天天象棋 / xiangqi.com

详情请看 #tournament 频道！
See #tournament channel for details!
```

---

## Daily Puzzle Automation / 每日谜题自动化

### Option 1: Manual Posting / 手动发布
- Post a new puzzle each day in `#daily-puzzle`
- Pin the puzzle message
- Unpin previous day's puzzle

### Option 2: Scheduled Messages (MEE6 Premium) / 定时消息
- Use MEE6's scheduled messages feature
- Prepare puzzles a week in advance
- Schedule each for 8:00 AM CST

### Option 3: Custom Bot (Advanced) / 自定义机器人
If comfortable with coding, create a simple bot that:
1. Reads from a puzzle database (Google Sheet or JSON file)
2. Posts a new puzzle daily at 8:00 AM CST to `#daily-puzzle`
3. Pins the message automatically
4. Posts the previous day's solution

---

## YouTube Upload Notifications / YouTube 上传通知

### Using MEE6:
1. Enable the **YouTube** plugin
2. Add your YouTube channel URL
3. Set notification channel: `#announcements`
4. Notification message:

```
📺 新视频！/ New Video!
{video_title}
{video_url}

@新视频通知 快来看！/ Come watch!
```

### Using Carl-bot:
1. Go to Dashboard → Feeds
2. Add YouTube RSS feed: `https://www.youtube.com/feeds/videos.xml?channel_id=YOUR_CHANNEL_ID`
3. Set output channel: `#announcements`

---

## Bilibili Notifications / B站通知

No native Discord integration for Bilibili. Options:
1. **Manual posting** — Post links manually in `#announcements`
2. **IFTTT/Zapier** — Set up an RSS-to-Discord webhook
3. **Custom webhook** — Use Bilibili RSS + Discord webhook URL

### Discord Webhook Setup:
1. Go to `#announcements` → Edit Channel → Integrations → Webhooks
2. Create a new webhook named "棋道 Bilibili"
3. Copy the webhook URL
4. Use it with IFTTT, Zapier, or a custom script
