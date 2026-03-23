# Discord Server Setup Guide / Discord 服务器创建指南

## Task: cc2 — Launch Discord Server for 棋道 ChessDAO

---

## Step 1: Create the Server / 创建服务器

1. Open Discord → Click **"+"** (Add a Server) on the left sidebar
2. Select **"Create My Own"**
3. Select **"For a club or community"**
4. Server name: **棋道 ChessDAO**
5. Click **Create**

## Step 2: Server Settings / 服务器设置

### General Settings / 常规设置

| Setting | Value |
|---------|-------|
| Server Name | 棋道 ChessDAO |
| Server Description | 象棋学习与交流社区 · Xiangqi Learning & Community |
| Default Notification Settings | Only @mentions |
| System Messages Channel | #welcome |
| Primary Language | Chinese (中文) |

### Server Icon / 服务器图标

- Use the logo from `branding.html`
- Export at **512 x 512 px** (PNG, under 8 MB)
- If the logo has a transparent background, place it on a solid dark red (#8B0000) or black (#1a1a1a) circle

### Server Banner / 服务器横幅 (Requires Boost Level 1)

- Adapt the YouTube banner to **960 x 540 px**
- Keep the 棋道 ChessDAO branding centered
- Ensure text is readable at small sizes

### Server Invite Splash (Requires Boost Level 1)

- Use a cropped version of the banner at **1920 x 1080 px**

## Step 3: Enable Community Features / 启用社区功能

1. Go to **Server Settings → Enable Community**
2. Follow the setup wizard:
   - Rules channel: `#rules`
   - Updates channel: `#announcements`
   - Enable **Welcome Screen**
   - Enable **Server Discovery** (once eligible, 500+ members)

## Step 4: Configure Welcome Screen / 配置欢迎界面

Navigate to **Server Settings → Welcome Screen** and add:

| Channel | Description |
|---------|-------------|
| #welcome | 📋 Read the rules and server intro / 阅读规则和服务器介绍 |
| #introductions | 👋 Introduce yourself / 自我介绍 |
| #daily-puzzle | ♟️ Try today's xiangqi puzzle / 挑战今日象棋谜题 |
| #general-chat | 💬 Chat with the community / 与社区交流 |
| #video-discussion | 🎬 Discuss latest videos / 讨论最新视频 |

## Step 5: Safety & Moderation / 安全与审核

1. **Verification Level**: Set to **Medium** (must be registered for 5+ minutes)
2. **Explicit Media Content Filter**: Filter messages from all members
3. **AutoMod**: Enable default keyword filters + custom rules:
   - Block spam links
   - Block excessive caps
   - Block repeated messages
4. **2FA Requirement**: Enable for moderators

## Step 6: Create Channels / 创建频道

See `channels.md` for the full channel structure. Create categories and channels in the order listed.

## Step 7: Set Up Roles / 设置身份组

See `roles.md` for the full role hierarchy and permissions.

## Step 8: Configure Bots / 配置机器人

See `bot-commands.md` for bot setup instructions.

## Step 9: Post Welcome Message / 发布欢迎消息

Copy the content from `welcome-message.md` and post it in `#welcome`.

## Step 10: Create Invite Links / 创建邀请链接

1. Go to `#welcome` → **Create Invite**
2. Set to **Never Expire**
3. Copy the link for use across platforms:
   - Douyin bio / 抖音简介
   - Bilibili bio / B站简介
   - YouTube description / YouTube 描述
   - Video end screens / 视频结尾画面

---

## Launch Checklist / 上线检查清单

- [ ] Server name and icon set / 服务器名称和图标已设置
- [ ] All channels created per `channels.md` / 所有频道已按 channels.md 创建
- [ ] All roles created per `roles.md` / 所有身份组已按 roles.md 创建
- [ ] Welcome message posted in #welcome / 欢迎消息已发布到 #welcome
- [ ] Bot(s) configured per `bot-commands.md` / 机器人已按 bot-commands.md 配置
- [ ] Permissions verified for each role / 各身份组权限已验证
- [ ] Invite link created and added to all platforms / 邀请链接已创建并添加到所有平台
- [ ] AutoMod and safety settings configured / 自动审核和安全设置已配置
- [ ] Test: new member join flow works correctly / 测试：新成员加入流程正常
- [ ] First daily puzzle posted / 第一个每日谜题已发布
