# Discord Role Structure / Discord 身份组结构

## Task: cc5 — Role Hierarchy for 棋道 ChessDAO

---

## Role Hierarchy (Top to Bottom) / 身份组层级（从高到低）

Create roles in this order (highest first in Discord settings):

---

### 1. 🛡️ 管理 Moderator

| Field | Value |
|-------|-------|
| Name | 🛡️ 管理 Moderator |
| Color | `#E74C3C` (Red) |
| Display separately | Yes |
| Allow mentioning | No |

**Permissions / 权限:**
- Manage Messages / 管理消息
- Kick Members / 踢出成员
- Ban Members / 封禁成员
- Mute Members / 禁言成员
- Manage Channels / 管理频道
- Manage Roles (below their level) / 管理身份组
- View Audit Log / 查看审核日志
- Manage Threads / 管理帖子
- Timeout Members / 暂时禁言

**How to assign / 分配方式:** Manual by server owner only / 仅服务器所有者手动分配

---

### 2. 🏆 大师 Master

| Field | Value |
|-------|-------|
| Name | 🏆 大师 Master |
| Color | `#F1C40F` (Gold) |
| Display separately | Yes |
| Allow mentioning | Yes |

**Permissions / 权限:**
- All default permissions
- Attach Files / 上传文件
- Embed Links / 嵌入链接
- Use External Emojis / 使用外部表情
- Add Reactions / 添加反应
- Connect & Speak in Voice / 连接和在语音中发言
- Priority Speaker in Voice / 语音优先发言
- Share Screen / 共享屏幕

**Requirements / 要求:**
- 月赛冠军或前三名 / Monthly tournament winner or top 3
- 连续30天每日谜题全部正确 / 30-day daily puzzle streak (all correct)
- 或由管理员认定的高水平棋手 / Or recognized high-level player by moderators

**How to assign / 分配方式:** Manual by moderators / 管理员手动分配

---

### 3. 🟢 高手 Expert

| Field | Value |
|-------|-------|
| Name | 🟢 高手 Expert |
| Color | `#2ECC71` (Green) |
| Display separately | Yes |
| Allow mentioning | Yes |

**Permissions / 权限:**
- All default permissions
- Attach Files / 上传文件
- Embed Links / 嵌入链接
- Use External Emojis / 使用外部表情
- Add Reactions / 添加反应
- Connect & Speak in Voice / 连接和在语音中发言
- Share Screen / 共享屏幕
- Create Public Threads / 创建公开帖子

**Requirements / 要求:**
- 活跃1个月以上 / Active for 1+ month
- 500+ 条消息 / 500+ messages
- 经常帮助其他成员 / Regularly helps other members
- 在 #game-analysis 或 #opening-theory 有高质量贡献 / Quality contributions in analysis channels

**How to assign / 分配方式:** Nomination by moderators or self-request with evidence / 管理员提名或自荐（需提供证据）

---

### 4. 🟡 棋手 Player

| Field | Value |
|-------|-------|
| Name | 🟡 棋手 Player |
| Color | `#F39C12` (Orange/Yellow) |
| Display separately | No |
| Allow mentioning | No |

**Permissions / 权限:**
- All default permissions
- Attach Files / 上传文件
- Embed Links / 嵌入链接
- Use External Emojis / 使用外部表情
- Add Reactions / 添加反应
- Connect & Speak in Voice / 连接和在语音中发言

**Requirements / 要求:**
- 加入1周以上 / Member for 1+ week
- 50+ 条消息 / 50+ messages

**How to assign / 分配方式:** Automatic via bot (MEE6 Level 3 or equivalent) / 机器人自动分配

---

### 5. 🎬 观众 Viewer

| Field | Value |
|-------|-------|
| Name | 🎬 观众 Viewer |
| Color | `#9B59B6` (Purple) |
| Display separately | No |
| Allow mentioning | No |

**Permissions / 权限:**
- All default permissions
- Add Reactions / 添加反应

**Requirements / 要求:**
- 已订阅频道（任何平台）/ Subscribed to channel (any platform)
- 在 #roles 中使用表情反应自助获取 / Self-assign via reaction role in #roles

**How to assign / 分配方式:** Reaction role (self-assign) / 表情反应自助获取

---

### 6. 🔴 红方 Red Side (Default)

| Field | Value |
|-------|-------|
| Name | 🔴 红方 Red Side |
| Color | `#E74C3C` (Light Red) |
| Display separately | No |
| Allow mentioning | No |

**Permissions / 权限:**
- Read Messages / 读取消息
- Send Messages / 发送消息
- Read Message History / 读取消息历史
- Add Reactions / 添加反应
- Connect to Voice / 连接语音

**Requirements / 要求:**
- 无 — 加入即获得 / None — assigned on join

**How to assign / 分配方式:** Auto-assign on join via bot / 机器人自动分配

---

## Notification Roles (Reaction Roles) / 通知身份组（表情反应身份组）

Create these additional roles for opt-in notifications. Set up reaction roles in a `#roles` channel.

| Role Name | Emoji | Purpose |
|-----------|-------|---------|
| 📺 新视频通知 New Video | 📺 | Pinged when new video is uploaded / 新视频上传时通知 |
| ♟️ 每日谜题 Daily Puzzle | ♟️ | Pinged when daily puzzle is posted / 每日谜题发布时通知 |
| 🏆 锦标赛 Tournament | 🏆 | Pinged for tournament announcements / 锦标赛公告通知 |
| 🔴 直播通知 Live Stream | 🔴 | Pinged when going live / 直播时通知 |

---

## Setup Instructions / 设置步骤

1. Go to **Server Settings → Roles** / 进入服务器设置 → 身份组
2. Create each role from top to bottom (highest rank first) / 从高到低依次创建
3. Set the colors using the hex codes above / 使用上方色值设置颜色
4. Configure permissions as listed / 按列表配置权限
5. Set up bot auto-role for 🔴 红方 Red Side on join / 设置机器人在加入时自动分配红方身份
6. Set up bot level-based promotion for 🟡 棋手 Player / 设置机器人按等级自动升级棋手身份
7. Create a reaction role message in #roles for notification roles / 在 #roles 创建表情反应身份消息

### Reaction Role Message (post in #roles) / 表情反应身份消息（发布到 #roles）

```
选择你想接收的通知 / Choose your notifications:

📺 — 新视频通知 / New video alerts
♟️ — 每日谜题通知 / Daily puzzle alerts
🏆 — 锦标赛通知 / Tournament alerts
🔴 — 直播通知 / Live stream alerts

点击下方表情即可！/ Click the reactions below!
```
