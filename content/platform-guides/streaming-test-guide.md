# Live Stream Testing Checklist

A step-by-step guide for testing your xiangqi (Chinese chess) streaming setup before going live. Covers hardware verification, OBS configuration, single-platform testing on Bilibili and Douyin, quality assurance, multi-platform streaming options, and a dry-run protocol.

---

## 1. Pre-Stream Hardware Check

Run through this checklist every time before you stream. It takes two minutes and prevents the most common technical failures.

### Microphone

1. **Physically verify the USB connection.** Unplug and re-plug the microphone. USB connections can loosen over time, causing intermittent audio dropout.
2. **Confirm OBS recognizes the mic:**
   - Open OBS Studio.
   - Go to **Settings → Audio**.
   - Under **Mic/Auxiliary Audio**, confirm your USB microphone appears by name (e.g., "Blue Yeti," "Fifine K669B," "Wave:3").
   - If the mic does not appear, check: Is it plugged in? Is another application (Zoom, Discord) holding exclusive access? Try a different USB port.
3. **Test audio levels:**
   - Look at the **Audio Mixer** panel at the bottom of the OBS window.
   - Speak at your normal commentary volume. The green meter should peak between **-12 dB and -6 dB**.
   - Speak at your loudest excited commentary voice. The meter should never hit red (0 dB). If it does, reduce the mic gain.
   - Whisper as you would during a tense endgame. The meter should still show movement. If it does not, your gain is too low.
4. **Verify audio filters are active:**
   - In the Audio Mixer, click the gear icon next to your mic → **Filters**.
   - Confirm these filters are present and enabled (in this order):
     - **Noise Suppression** (RNNoise)
     - **Compressor** (Ratio 4:1, Threshold -18 dB, Attack 6 ms, Release 60 ms)
     - **Limiter** (Threshold -1 dB)
   - If any filter is missing, add it now. Do not stream without at least Noise Suppression.

### Board Tool

1. Open your board tool in the browser:
   - **board-art.html** for artistic board display.
   - **explain.html** for analysis/explanation mode with engine integration.
2. Confirm the board renders correctly — pieces load, drag-and-drop works, move history displays.
3. If using engine evaluation, verify the engine is running and the eval bar updates when you make moves.
4. Resize the browser window to match your OBS capture region (typically 1920x1080 or the board area within your scene).

### OBS Scene

1. Load your streaming scene (created using the obs-config scene templates).
2. Verify each source is visible and positioned correctly:
   - Board capture (window or browser source) fills the main area.
   - Overlay graphics (if any) are in the correct corners.
   - Webcam (if using) is in the designated corner, not overlapping the board.
3. Lock all sources to prevent accidental movement during the stream: right-click each source → **Lock**.

---

## 2. OBS Settings Verification

Before your first stream on a new platform, verify these output settings. After initial setup, you only need to recheck if you change hardware or OBS versions.

### Video Settings

- Navigate to **Settings → Video**.
- **Base (Canvas) Resolution:** 1920x1080.
- **Output (Scaled) Resolution:** 1920x1080. Do not downscale unless your upload bandwidth is limited, in which case use 1280x720.
- **Common FPS Values:** 30. Xiangqi commentary does not benefit from 60fps — the board is mostly static, and 30fps halves your bandwidth requirement.
- **Downscale Filter:** Lanczos (if scaling). Bicubic is acceptable.

### Output Settings

- Navigate to **Settings → Output**. Set **Output Mode** to **Advanced** for full control.

**Streaming Tab:**
- **Encoder:** x264 (software, works on any CPU) or hardware encoder if available:
  - NVIDIA: NVENC H.264
  - AMD: AMF H.264
  - Apple Silicon: Apple VT H264 Hardware Encoder
- **Rate Control:** CBR (Constant Bit Rate).
- **Bitrate:** 4000–6000 kbps. Start at 4500 kbps. If your upload speed is above 10 Mbps, use 6000 kbps for maximum quality.
- **Keyframe Interval:** 2 seconds (required by most platforms).
- **CPU Usage Preset (x264 only):** "veryfast" is the safe default. If your CPU handles it without dropping frames, try "faster" or "medium" for better quality.
- **Profile:** High.

**Recording Tab (for simultaneous local recording):**
- **Recording Format:** MKV (resilient to crashes — if OBS crashes during stream, MKV files remain playable; MP4 files would be corrupted). Remux to MP4 after recording via **File → Remux Recordings**.
- **Encoder:** Same as streaming, or use CQP/CRF mode at quality 18–20 for higher-quality local copies.

### Audio Settings

- Navigate to **Settings → Audio**.
- **Sample Rate:** 48 kHz (matches most USB microphones natively).
- **Channels:** Stereo.
- Navigate to **Settings → Output → Audio Tab** (within the Output section):
  - **Audio Bitrate:** 160 kbps AAC. This is more than sufficient for voice commentary. Going higher wastes bandwidth with no audible benefit.

### Settings Summary Table

| Setting | Value |
|---------|-------|
| Resolution | 1920x1080 |
| Frame rate | 30 fps |
| Encoder | x264 or hardware H.264 |
| Video bitrate | 4000–6000 kbps CBR |
| Keyframe interval | 2 seconds |
| Audio sample rate | 48 kHz |
| Audio bitrate | 160 kbps AAC |
| Recording format | MKV (remux to MP4 after) |

---

## 3. Single-Platform Test

Test one platform at a time. Get it working perfectly before adding a second platform.

### Bilibili (B站)

1. **Get your RTMP stream key:**
   - Log in to Bilibili on desktop.
   - Go to **直播中心** (Live Center): link.bilibili.com.
   - Click **开始直播** (Start Streaming).
   - Select your live category. Navigate to: **知识** → **棋牌** or **生活** → **其他** (whichever matches your content).
   - Bilibili will display your **服务器地址** (Server URL / RTMP URL) and **串流密钥** (Stream Key).
   - Copy both values.

2. **Configure OBS:**
   - Go to **Settings → Stream**.
   - **Service:** Select "Bilibili Live" if available, otherwise select "Custom."
   - **Server:** Paste the 服务器地址.
   - **Stream Key:** Paste the 串流密钥.
   - Click **Apply**, then **OK**.

3. **Start streaming:**
   - Click **Start Streaming** in OBS.
   - Wait 10–15 seconds for the stream to propagate.
   - Open Bilibili on your phone (or a second browser tab) and navigate to your live room (直播间).
   - Verify: video loads, audio is present, board is visible and legible.

4. **Check the following on the live stream:**
   - **Video quality:** Board pieces should be clearly distinguishable. Text (player names, move notation, eval numbers) should be readable.
   - **Audio sync:** Speak while making a move on the board. On the viewer side, your voice and the move should appear within 1 second of each other. If audio is ahead or behind, check OBS **Advanced Audio Properties** (right-click the audio source in Audio Mixer) and adjust **Sync Offset**.
   - **Overlay positioning:** Ensure overlays do not cover the board center, engine eval bar, or move list. Adjust in OBS if needed.
   - **Stream delay:** Note the delay between your action and what the viewer sees. Under 5 seconds is acceptable for Bilibili.

5. **Stop streaming** in OBS when testing is complete. Stop the live room on Bilibili.

### Douyin (抖音)

1. **Get your RTMP stream key:**
   - Option A — **抖音直播伴侣 (Douyin Live Companion):** Download and install from the Douyin website. Log in, and the RTMP URL and stream key are shown in the app settings. You can then ignore the companion app and use OBS directly with the RTMP credentials.
   - Option B — **Web dashboard:** Log in to the Douyin creator portal. Navigate to the live streaming section. Copy the RTMP URL and stream key.
   - Note: Douyin live streaming may require your account to meet follower thresholds or verification requirements. Check current requirements on the platform.

2. **Configure OBS:**
   - Go to **Settings → Stream**.
   - **Service:** Select "Custom."
   - **Server:** Paste the Douyin RTMP URL.
   - **Stream Key:** Paste the stream key.
   - Click **Apply**, then **OK**.

3. **Vertical vs. horizontal:**
   - Douyin is a mobile-first platform. Many viewers watch in portrait (vertical) mode.
   - If you want to stream in vertical format:
     - In OBS, go to **Settings → Video**.
     - Set **Base Resolution** to 1080x1920 (swap width and height).
     - Rearrange your scene to stack elements vertically: board on top, commentary text or webcam below.
   - If you prefer standard horizontal (landscape) format, Douyin supports it — viewers will see black bars on the sides on mobile, but the quality is fine.
   - **Recommendation:** Start with horizontal (your normal 1920x1080 setup). Most xiangqi boards are square and work well in landscape. Switch to vertical only if your Douyin analytics show strong mobile viewership demanding it.

4. **Start streaming and verify** using the same checklist as Bilibili above.

---

## 4. Quality Checklist

Print this or keep it open in a second monitor. Run through every item before each stream.

### Visual Quality

- [ ] Board pieces are readable at 720p. Open the stream on your phone and hold it at arm's length — if you can identify every piece, you pass. Many viewers watch at 720p even if you stream at 1080p.
- [ ] Engine evaluation bar is updating in real time when you make moves.
- [ ] Player information lower-third (name, rating, time) looks correct and is not cut off.
- [ ] Overlays are positioned in non-critical areas (corners, edges) and do not obscure the board.
- [ ] Color contrast is adequate — board colors, piece colors, and overlay text are all legible.

### Audio Quality

- [ ] Voice is clear and intelligible.
- [ ] No echo or reverb (close windows, turn off speakers — use headphones while streaming).
- [ ] No background noise audible (fan, air conditioning, traffic, family members).
- [ ] Volume is consistent — quiet analysis and excited commentary are both audible without being jarring.
- [ ] No clipping on loud moments (check OBS meter — never hitting red).

### Technical Stability

- [ ] No frame drops. Check the OBS stats panel: **View → Stats** (or the bottom status bar). Dropped frames should read 0.0%. If frames are dropping:
  - Reduce output resolution to 1280x720.
  - Reduce bitrate to 3500 kbps.
  - Switch to a faster encoder preset.
  - Close other applications consuming CPU/GPU.
- [ ] Stream delay is acceptable. Under 5 seconds is typical. If delay exceeds 10 seconds, check your internet connection.
- [ ] No audio desync over time. After streaming for 10+ minutes, verify audio and video are still aligned. Persistent drift usually indicates a sample rate mismatch (check that OBS and your mic are both set to 48 kHz).

---

## 5. Multi-Platform Streaming

Once your single-platform setup works reliably, you may want to stream to multiple platforms simultaneously to maximize reach. Here are three approaches, ordered from simplest to most complex.

### Option A: Restream.io (Recommended for Beginners)

Restream is a cloud-based service that receives your single stream and redistributes it to multiple platforms.

1. **Sign up** at restream.io. The free tier supports 2 simultaneous platforms.
2. **Connect your platforms:**
   - Click **Add Channel**.
   - Connect Bilibili (may require RTMP custom setup), Douyin (custom RTMP), and/or YouTube.
   - For each platform, enter the RTMP URL and stream key from that platform.
3. **Get Restream's RTMP credentials:**
   - Restream provides a single RTMP URL and stream key.
   - Paste these into OBS (**Settings → Stream → Custom**).
4. **Stream to Restream** from OBS. Restream handles the rest.
5. **Benefits:**
   - You upload one stream — Restream's servers handle redistribution.
   - Lower upload bandwidth requirement (one outgoing stream instead of two or three).
   - Restream's dashboard shows chat from all platforms in one place.
6. **Downsides:**
   - Free tier is limited to 2 platforms (paid plans start at ~$16/month for more).
   - Adds a small amount of latency (Restream's servers are an intermediary).
   - Platform-specific features (Bilibili 弹幕 overlay, Douyin gifts) may not work through Restream.

### Option B: OBS Multi-RTMP Plugin

This approach streams directly from your computer to multiple platforms simultaneously.

1. **Install the plugin:**
   - Search for "obs-multi-rtmp" on GitHub or the OBS plugin repository.
   - Download the version matching your OS and OBS version.
   - Install and restart OBS.
2. **Configure multiple outputs:**
   - In OBS, a new **Multi-RTMP** dock appears.
   - Click **Add New Target** for each platform.
   - Enter the platform name, RTMP URL, and stream key for each (Bilibili, Douyin, YouTube, etc.).
3. **Start streaming:**
   - Click **Start Streaming** in OBS for your primary platform.
   - In the Multi-RTMP dock, click **Start** next to each additional platform.
4. **Benefits:**
   - Free, no intermediary service.
   - No additional latency.
   - Full control over each output.
5. **Downsides:**
   - Your upload bandwidth must support multiple simultaneous streams. For two platforms at 5000 kbps each, you need at least 12–15 Mbps upload (accounting for overhead).
   - Higher CPU/GPU load — encoding multiple outputs simultaneously. Hardware encoders (NVENC) handle this better than x264.
   - If your internet connection is unstable, all streams suffer.

### Option C: Stream to One, Upload VODs to Others (Simplest)

The lowest-effort approach, and the one recommended if you are just starting out.

1. **Stream live to your primary platform** (whichever has your largest audience — likely Bilibili or Douyin).
2. **Record the stream locally** in OBS simultaneously (enable recording alongside streaming).
3. **After the stream ends,** remux the MKV to MP4: **File → Remux Recordings** in OBS.
4. **Upload the VOD** (video on demand) to your other platforms as a regular video.
5. **Benefits:**
   - Zero additional complexity during the live stream.
   - No bandwidth concerns.
   - You can edit the VOD before uploading (trim dead air at the start/end, add chapter markers).
   - Each platform gets a natively uploaded video, which algorithms tend to favor over third-party redistribution.
6. **Downsides:**
   - Other platforms get delayed content, not live.
   - You miss the live interaction (chat, donations, real-time viewers) on secondary platforms.

### Which Option to Choose

| Situation | Recommendation |
|-----------|----------------|
| First 1–3 months of streaming | Option C — focus on one platform |
| Established on one platform, testing a second | Option A (Restream.io) |
| Strong upload bandwidth (20+ Mbps), comfortable with OBS | Option B (obs-multi-rtmp) |
| Maximizing live engagement on all platforms | Option B |

---

## 6. First Stream Dry Run

Before your first public live stream, do a full rehearsal. This catches problems that only appear under real streaming conditions (encoding load, network behavior, platform processing).

### The 15-Minute Private Test

1. **Set your stream to private or unlisted:**
   - **Bilibili:** You cannot set a live room to private, but you can start streaming without announcing it. Your live room exists but is unlikely to be discovered in 15 minutes. Alternatively, stream during off-peak hours (e.g., 3 AM) when no one is browsing.
   - **Douyin:** Similar approach — start the stream without promotion.
   - **YouTube:** Set the stream to "Unlisted" in YouTube Studio → Go Live → Stream Settings.

2. **Enable simultaneous local recording:**
   - In OBS, click **Start Recording** before you click **Start Streaming**.
   - This gives you a local copy to review, independent of the platform's VOD quality.

3. **Perform your full streaming routine for 15 minutes:**
   - Start with your intro (greet viewers, state the topic).
   - Analyze a game on the board tool, narrating as you would in a real stream.
   - Include moments of excitement (test your audio handling under loud commentary).
   - Use any overlays, scene transitions, or tools you plan to use in real streams.
   - End with your outro.

4. **Stop streaming and recording.**

### Review the Recording

1. **Open the local recording** (remux MKV to MP4 first if needed).
2. **Watch the entire 15 minutes with headphones.** Do not skip ahead. You are watching as a viewer.
3. Check for:
   - **Audio issues:** Background noise, clipping, inconsistent volume, echo.
   - **Video issues:** Blurry board, unreadable text, overlay problems, frame stuttering.
   - **Pacing issues:** Long silences, awkward transitions, unclear explanations.
   - **Technical failures:** Dropped frames, encoding artifacts, audio desync.
4. **Also check the platform's VOD** (if available). Platform processing can introduce additional quality loss. If the platform's version looks significantly worse than your local recording, increase your streaming bitrate.

### Fix and Repeat

- For every issue found, make the fix in OBS or your setup.
- Run another 15-minute test.
- Repeat until you complete a clean test run with no issues.
- Only then schedule your first public stream.

### Pre-First-Stream Final Checklist

- [ ] Completed at least one clean 15-minute dry run with no issues
- [ ] Audio is clear, properly leveled, and free of background noise
- [ ] Board is legible at 720p viewing resolution
- [ ] Overlays are positioned correctly and do not obstruct the board
- [ ] No frame drops during the entire test
- [ ] Stream delay is under 5 seconds
- [ ] You have a local recording workflow as backup
- [ ] You know how to start and stop the stream on both OBS and the platform
- [ ] You have a rough outline of what you will cover in your first stream

---

## Summary

Testing before going live is not optional — it is the difference between a professional first impression and a technical disaster. Follow this checklist systematically: verify hardware, confirm OBS settings, test on a single platform, pass the quality checks, and complete a full dry run. Only after all of these pass should you go live. For multi-platform streaming, start with the simplest approach (Option C: stream to one, upload VODs to others) and graduate to simultaneous streaming only when your setup and bandwidth can handle it.
