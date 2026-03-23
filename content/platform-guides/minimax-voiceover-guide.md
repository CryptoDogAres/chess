# MiniMax AI Voiceover Production Workflow for Xiangqi Commentary

A complete guide to producing xiangqi (Chinese chess) commentary videos using MiniMax AI text-to-speech instead of a physical microphone. This workflow eliminates the need for recording equipment, soundproofing, or vocal training — you write the script, MiniMax speaks it, and you edit it together with board animations. The result is a professional-sounding video produced entirely from your desk.

---

## 1. What is MiniMax and Why Use It

MiniMax is a Chinese AI platform that generates natural-sounding speech from text input. Unlike older TTS engines that sound flat and mechanical, MiniMax produces voices with realistic intonation, emotional range, and clear Chinese diction. For xiangqi content creators, this solves several real problems at once.

**Why AI voiceover makes sense for xiangqi commentary:**

- **No equipment barrier.** You do not need a USB microphone, pop filter, shock mount, or quiet room. If you have a laptop and an internet connection, you can produce voiceover.
- **Consistent quality.** Every take sounds the same. No vocal fatigue after recording five scripts in a row, no background noise from air conditioning, no re-takes because you stumbled over 胡荣华's career statistics.
- **Speed.** A 10-minute voiceover script can be generated in under 2 minutes. Recording it yourself, with mistakes and re-takes, might take 30-45 minutes.
- **Language clarity.** MiniMax produces standard 普通话 (Mandarin) with perfect pronunciation. If your own Mandarin has regional accent features that might distract viewers, AI voiceover sidesteps the issue entirely.
- **Low cost.** MiniMax offers free tiers and affordable paid plans. Even the paid tiers cost less per month than a mid-range USB microphone costs once.

**When you might still prefer a real microphone:** If your personality and voice are core to your brand identity, or if you do live commentary and interaction, a real voice is irreplaceable. But for pre-produced puzzle videos, game analysis, and educational content, AI voiceover is a legitimate and increasingly common production choice.

---

## 2. Voice Selection

MiniMax offers a library of voice options. Choosing the right voice is one of the most important decisions you will make — it becomes your channel's identity. Do not rush this step.

### Recommended Voice Profiles for Xiangqi Content

| Voice Style | Best For | Feel |
|---|---|---|
| Male authoritative (百家讲坛 host style) | Famous game analysis, historical content | Scholarly, trustworthy, serious |
| Female warm teacher | Puzzle walkthroughs, beginner lessons | Approachable, patient, encouraging |
| Male casual/conversational | Quick puzzle shorts, entertaining commentary | Energetic, relatable, modern |

### How to Choose

1. Write a single 30-second test script that includes typical xiangqi content: a player name, a move description, a question to the audience, and an emotional reveal. Example:

   > 1956年全国象棋锦标赛，胡荣华对阵杨官璘。局面走到这里，红方面临一个关键选择。你觉得红方应该怎么走？......答案是：车八进五！一步弃车，打开了通往胜利的大门。

2. Generate this same script with 3-5 different voices.
3. Listen to each one and evaluate: Does the voice sound natural during the analytical parts? Does the dramatic pause before the reveal feel right? Does the player name sound correct?
4. Ask a friend or family member to listen blind (without knowing which is which) and pick their favorite.
5. Once you commit to a voice, use it consistently across all videos. Viewers associate the voice with your channel.

### Characteristics to Prioritize

- **Clear diction (字正腔圆).** Every chess term must be intelligible. If the voice swallows syllables or blurs tones, reject it.
- **Natural pacing.** The voice should not sound like it is reading a grocery list. Look for slight variations in rhythm.
- **Appropriate energy.** For 10-30 minute content, the voice needs to sustain interest without being exhausting to listen to.
- **Pronunciation of names.** Test with: 胡荣华 (Hu Ronghua), 许银川 (Xu Yinchuan), 杨官璘 (Yang Guanlin), 赵国荣 (Zhao Guorong). If any sound wrong, try a different voice or add pronunciation hints.

---

## 3. Script Preparation for TTS

Your scripts from `content/puzzles/*.md`, `content/famous-games/*.md`, and other content directories are written in Markdown with formatting intended for human readers. MiniMax needs plain text with specific punctuation cues to produce natural-sounding speech.

### Conversion Steps

**Step 1: Strip Markdown formatting.**
Remove all headers (`#`, `##`), bold markers (`**`), italic markers (`*`), bullet points, and code blocks. MiniMax will read these characters literally or skip them unpredictably.

**Step 2: Add punctuation for pacing.**
- Use commas (，) for short pauses within a thought.
- Use periods (。) for full stops and longer pauses between thoughts.
- Use ellipsis (......) for dramatic pauses. This is crucial for puzzle reveals — the pause before "答案是" should feel deliberate.
- Use exclamation marks (！) sparingly to signal emphasis.

**Step 3: Add pronunciation guides.**
For player names and unusual terms, include pinyin in parentheses if the TTS mispronounces them. Test each name first; only add guides where needed.

Common names in xiangqi content:
- 胡荣华 (Hú Rónghuá)
- 许银川 (Xǔ Yínchuān)
- 杨官璘 (Yáng Guānlín)
- 赵国荣 (Zhào Guóróng)
- 柳大华 (Liǔ Dàhuá)
- 吕钦 (Lǚ Qīn)

**Step 4: Split into segments.**
Do not paste an entire 10-minute script as a single block. Split it into logical sections, each generating its own audio file:

| Segment | Typical Length | Content |
|---|---|---|
| Intro hook | 15-30 seconds | "This position has stumped grandmasters..." |
| Background/context | 60-90 seconds | Player bios, tournament setting, significance |
| Position analysis | 2-5 minutes | Walk through the position, explain candidate moves |
| Audience question | 10-15 seconds | "What would you play here? Pause and think..." |
| Answer reveal | 30-60 seconds | The correct move and why it works |
| Follow-up analysis | 2-5 minutes | Continuation lines, what happens after the key move |
| Closing | 15-30 seconds | Summary, subscribe prompt, next video teaser |

Keeping segments separate gives you flexibility in editing. You can adjust timing, re-generate one segment without redoing the whole script, and mix different emotion settings per segment.

**Step 5: Mark emphasis (if supported).**
Some MiniMax voice options support SSML-like emphasis tags. If available, mark words that should receive stress: key move names, surprising revelations, important chess terms. Test whether emphasis tags actually improve the output — sometimes they make it worse.

---

## 4. Recommended TTS Settings

### Audio Parameters

| Setting | Recommended Value | Notes |
|---|---|---|
| Speed | 0.9x - 1.0x (analysis), 1.05x - 1.1x (exciting moments) | Slower for complex analysis helps viewers follow along |
| Emotion | Neutral (analysis), Excited/Surprised (reveals) | Match emotional tone to content moment |
| Language | Simplified Chinese, 普通话 | Standard Mandarin for broadest audience |
| Export format | WAV preferred, MP3 acceptable | WAV is lossless; use MP3 only if file size is a concern |
| Sample rate | 48 kHz | Matches standard video editing project settings |
| Channels | Mono | Voiceover does not need stereo; mono keeps files smaller |

### Speed Adjustments by Segment

- **Intro hook:** 1.0x — confident, steady, draws the viewer in.
- **Background context:** 1.0x — informational, clear.
- **Position analysis:** 0.9x — slower so viewers can follow along with the board.
- **Audience question:** 0.9x with a long pause (......) — give them time to think.
- **Answer reveal:** 1.05x-1.1x — slightly faster, more energy, excitement.
- **Closing:** 1.0x — return to calm, professional tone.

---

## 5. Production Pipeline with MiniMax

Here is the complete workflow from script to published video. Each step feeds into the next.

```
Step 1: Write script in scripts.html tool
        └─ Structured script with sections, timing notes, move references

Step 2: Export script as plain text
        └─ Strip markdown, add TTS punctuation, split into segments

Step 3: Paste segments into MiniMax → generate voiceover audio files
        └─ One WAV/MP3 file per segment (intro.wav, analysis.wav, reveal.wav, etc.)

Step 4: Import audio files into your video editor (CapCut/剪映, Shotcut, or Premiere)
        └─ Arrange segments on the audio timeline in order

Step 5: Screen-record board animation from explain.html (muted)
        └─ Record the full game/puzzle playback with no audio

Step 6: Sync audio + video in the editor
        └─ Align move animations with the narration describing those moves

Step 7: Add captions, text overlays, and thumbnail frame
        └─ Auto-captions in 剪映, manual in other editors; add move notation overlays

Step 8: Export final video and publish to platforms
        └─ 1080p, H.264, AAC audio, platform-appropriate aspect ratio
```

**Time estimate for one video:** Once you have practiced this workflow 3-4 times, a single 10-minute video takes approximately 45-60 minutes from script to export. The first few will take longer as you learn the tools.

---

## 6. Syncing Audio with Board Animation

This is the trickiest part of the workflow. The narration says "红方走车八进五" and the board needs to show that move at the same moment. Three approaches, from easiest to most polished:

### Method A: Simple Overlay (Easiest)

1. Generate all audio segments and note the total duration.
2. Open explain.html, set the auto-play speed so the full game takes roughly the same total time as your audio.
3. Screen-record the board playback (muted).
4. In your editor, place the audio track and video track together. They will be approximately aligned.
5. Make small cuts and adjustments where moves and narration drift apart.

**Pros:** Fast. Good enough for your first 10-20 videos.
**Cons:** Timing will never be perfect. Some moves will appear slightly before or after the narration.

### Method B: Cut-to-Match (Better)

1. Generate all audio segments.
2. Screen-record each move on the board individually — pause between moves, or record the full sequence and note timestamps.
3. In the editor, cut the board video so each move appears exactly when the narration describes it.
4. Use freeze frames to hold a position while the narration provides analysis.

**Pros:** Precise sync. Professional result.
**Cons:** More editing time. Requires familiarity with your editor's cut and freeze-frame tools.

### Method C: Pre-Timed Recording (Best)

1. Generate all audio segments and measure the exact duration of each.
2. In explain.html, configure auto-play delays to match: if the narration spends 45 seconds on the first move's analysis, set a 45-second delay before the next move plays.
3. Screen-record the board with these custom timings. The board and narration are now synchronized by design.
4. Import both into the editor — they should align with minimal adjustment.

**Pros:** Minimal editing. Scales well for batch production.
**Cons:** Requires upfront timing work. If you re-generate audio, you need to re-time the board recording too.

### General Sync Tips

- Record board animations at a higher speed (1.5x) and slow them down in the editor. This gives you smoother move transitions.
- Leave 1-2 seconds of silence between audio segments. This buffer makes syncing much more forgiving.
- For puzzle videos under 60 seconds (Shorts/Douyin), Method A is perfectly adequate. Save Method B and C for longer-form content.

---

## 7. Batch Production Strategy

The biggest efficiency gain comes from batching. Instead of producing one video at a time from start to finish, do each phase for multiple videos in one sitting.

### Recommended Batch Workflow

| Phase | Batch Size | Time | Output |
|---|---|---|---|
| Script writing | 5 scripts | 60-90 min | 5 plain-text TTS-ready scripts |
| MiniMax voiceover generation | 5 sets of audio | 20-30 min | 15-25 audio segment files |
| Board animation recording | 5 screen recordings | 30-45 min | 5 video files |
| Video editing and sync | 5 videos | 60-90 min | 5 finished videos |
| **Total** | **5 videos** | **3-4 hours** | **Ready to publish** |

### Why Batching Works

- **Context switching is expensive.** Opening MiniMax, configuring settings, and uploading text has overhead. Doing it once for five scripts is faster than doing it five separate times.
- **Creative momentum.** Writing five scripts in a row keeps you in the analytical mindset. You will spot connections between games, reuse framing techniques, and develop a consistent voice.
- **Editing muscle memory.** By the third video in a batch editing session, you are cutting and syncing twice as fast as the first.
- **Publishing buffer.** Five videos gives you nearly a week of daily content (or 2+ weeks at 2-3 per week). You can batch-produce on weekends and publish throughout the week.

### Weekly Schedule Example

| Day | Activity |
|---|---|
| Saturday morning | Write 5 scripts, generate 5 voiceovers |
| Saturday afternoon | Record 5 board animations, edit 5 videos |
| Sunday | Review, add thumbnails, schedule for the week |
| Monday-Friday | Publish one video per day (pre-scheduled) |

---

## 8. Quality Checklist

Before exporting any video, verify every item on this list. Print it out or keep it open in a browser tab during editing sessions.

- [ ] **Voice naturalness.** Does the AI voice sound conversational, not robotic? If any segment sounds stiff, re-generate it with slight wording changes.
- [ ] **Audio-visual sync.** Every move on the board appears within 1 second of its narration. No move animates before the narrator mentions it.
- [ ] **Dramatic pauses.** There is a clear 2-3 second pause at every "What would you play?" moment. The viewer needs time to think.
- [ ] **Emotional tone at reveals.** The "答案是......" moment sounds genuinely excited or surprised, not flat.
- [ ] **Player name pronunciation.** Listen specifically for each player name. 胡荣华, 许银川, and others should have correct tones.
- [ ] **No awkward cuts.** Transitions between audio segments sound continuous, not like two separate recordings spliced together.
- [ ] **Volume consistency.** All segments are at the same volume level. No sudden loud or quiet sections.
- [ ] **Caption accuracy.** If you used auto-captions, check that chess terms and player names are displayed correctly. Auto-caption tools frequently get chess notation wrong.
- [ ] **Intro hook strength.** Play the first 3 seconds. Would you keep watching?
- [ ] **Clean ending.** No abrupt cutoff. The closing line finishes naturally, with a brief fade-out or end card.

---

## 9. Platform Considerations

AI voiceover is treated differently across platforms. Know the norms before publishing.

### Douyin (抖音)

AI voiceover is extremely common on Douyin. Many of the platform's most successful educational and commentary channels use synthesized voice. Viewers are accustomed to it and do not penalize content for using TTS. In fact, the consistency and clarity of AI voice can be an advantage in Douyin's fast-scrolling environment. No disclosure is required, though you may add a note if you wish.

### Bilibili (B站)

Bilibili's audience skews toward viewers who value personality and authenticity. Many popular UP主 (uploaders) are known for their distinctive voices. That said, AI voiceover is increasingly accepted, especially for educational and reference content. If your analysis is insightful and your production quality is high, viewers will watch regardless of voice source. Consider mentioning in your first video that you use AI voiceover — Bilibili audiences appreciate transparency and will respect the honesty.

### YouTube

YouTube requires transparency about AI-generated content. Add a disclosure line in your video description:

> Audio narration generated using AI text-to-speech (MiniMax). All analysis and commentary written by [your name].

This covers YouTube's guidelines and builds trust with your audience. In practice, YouTube's algorithm does not penalize AI voiceover — watch time and engagement are what matter.

### Xiaohongshu (小红书)

For short-form xiangqi content on Xiaohongshu, AI voiceover works well. Keep videos under 3 minutes. The platform favors polished, visually clean content, and consistent AI voice contributes to that polished feel.

---

## 10. Cost Optimization

MiniMax offers tiered pricing. Here is how to get the most value from every character you generate.

### Pricing Awareness

MiniMax typically charges based on character count. Exact pricing changes over time, so check their current rates. General principles:

- **Free tier** usually covers enough characters for 2-3 short videos per month. Use this to test and experiment before committing to a paid plan.
- **Paid tiers** unlock higher character limits, more voices, and priority generation. If you produce 5+ videos per week, a paid plan becomes cost-effective quickly.
- **Character count matters.** A 10-minute narration is roughly 1,500-2,000 Chinese characters. A 60-second short is 150-250 characters.

### How to Maximize Value

1. **Keep scripts under 2,000 characters per segment.** Longer segments tend to produce less natural audio. Splitting into shorter segments is better for quality and for staying within character limits.
2. **Batch-generate all audio for the week in one session.** This avoids repeated setup time and helps you track character usage.
3. **Edit scripts before generating.** Every re-generation due to a typo or phrasing change costs characters. Proofread carefully, read the script aloud yourself once, and only then paste it into MiniMax.
4. **Reuse intro and outro audio.** Your channel intro ("欢迎来到......") and outro ("如果你喜欢这期内容......") can be generated once and reused across every video. This saves hundreds of characters per video.
5. **Monitor your usage.** Track how many characters you use per video and per week. Set a budget and stick to it. A simple spreadsheet works.

### Cost Per Video Estimate

| Video Type | Characters | Approximate Cost |
|---|---|---|
| 60-second puzzle short | 150-250 | Minimal (often covered by free tier) |
| 5-minute game analysis | 800-1,200 | Low |
| 10-minute deep dive | 1,500-2,000 | Moderate |
| 20-minute historical feature | 3,000-4,000 | Higher (split across multiple segments) |

---

## Quick-Start Checklist

If you want to produce your first MiniMax-powered xiangqi video today, follow these steps in order:

1. Create a MiniMax account at their website.
2. Pick one puzzle from `content/puzzles/` and open its script.
3. Copy the script text, strip formatting, and add TTS punctuation.
4. Generate the voiceover in MiniMax using the default voice. Do not spend time choosing the perfect voice yet — just get one video done.
5. Screen-record the puzzle from explain.html.
6. Open CapCut/剪映, import both files, and sync them roughly (Method A).
7. Add auto-captions. Export. Publish to Douyin.
8. Watch it back. Note what you would improve. Then do the next one.

Your first video will not be perfect. Your fifth will be noticeably better. By your twentieth, you will have a smooth, repeatable system that produces consistent content with zero recording equipment. The workflow scales — the only limit is how many scripts you can write.
