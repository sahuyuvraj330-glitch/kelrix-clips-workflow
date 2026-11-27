# Kelrix Clips — How We Make a 60-Second History Short Every Day

The full workflow behind the [Kelrix Clips](https://www.youtube.com/@Kelrix-n1s) YouTube Shorts channel: one true-history story a day, told in 60 seconds of flat 2D cutout animation.

This repo documents the process, not the videos. No video files live here — it's the pipeline, the rules, and the helpers we actually use, so anyone can run the same loop.

## The channel

Wars, escapes, spies, heists. True history, 60 seconds. A new Short daily, for a US audience.

- YouTube: https://www.youtube.com/@Kelrix-n1s
- Instagram / Threads / Facebook: **Kelrix Clips** (`@kelrixclips`)

## The daily pipeline

1. **9:00 AM IST — topic research.** Find a past event with a video that gained 1–2M views in the past 6 months and is still growing. Small channels with breakout views are a strong signal. See [docs/topic-research.md](docs/topic-research.md).
2. **Pick a topic.** The picks go to the channel owner, who chooses one.
3. **Fact-check.** Verify every date and number against real sources before writing anything. See [docs/script-and-storyboard.md](docs/script-and-storyboard.md).
4. **Script + storyboard.** ~190–200 words, 7 scenes, ~75–82 seconds, hook in the first seconds, thumbnail text baked in.
5. **Voiceover.** One consistent voice (Helio) for every Short, verified word-for-word by transcription before it goes anywhere. See [docs/voiceover.md](docs/voiceover.md).
6. **QC sheet.** A 7-scene contact sheet fitted to the voiceover timings. The owner approves it personally — this step never auto-approves.
7. **Render.** Claude renders the video in the browser: cutout animation, white rounded captions burned in, original music and sound effects.
8. **Thumbnail.** A fresh standalone design in the video's own cutout style, judged by the curiosity test. See [docs/thumbnails.md](docs/thumbnails.md).
9. **Upload.** YouTube Studio, scheduled for the best US window. See [docs/upload-and-scheduling.md](docs/upload-and-scheduling.md).
10. **Repeat tomorrow.**

The full timetable with approval rules lives in [docs/daily-workflow.md](docs/daily-workflow.md).

## The stack

| Job | Tool |
|---|---|
| Script, storyboard, QC, render | Claude, in the browser |
| Voiceover | Helio voice, split-render method, transcription-verified |
| Voiceover polish (optional) | Adobe Podcast Enhance Speech (free) |
| Video checks | ffmpeg / ffprobe |
| Upload | YouTube Studio in the browser (free) |
| Research | YouTube + vidIQ (free plan) |
| Cross-posting | Instagram Reels / Threads / Facebook, daily 8:00 PM IST |

## The rules that matter

- **One voice, forever.** Helio, same pace (~147–154 wpm), every Short. Never switch without being asked.
- **Thumbnails match the video.** Same flat cutout style as the animation — small round head, dot eyes, jointed limbs, cream label boxes. Never clay, never paper texture, never a big-head chibi.
- **The curiosity test.** The subject must be mid-action, doing something that makes the viewer wonder what happens next. No standing-alone poses.
- **Captions in the video.** Simple, rounded, white, burned in during the render.
- **QC needs a human.** The script and the QC sheet are approved by a person every time. The voiceover auto-approves only if there's no reply within an hour.

## The workflow kit

The professional, reusable core of the repo — copy a template per video and fill it in:

- [docs/style-bible.md](docs/style-bible.md) — the visual specification for every Short: the cutout figure, colour, labels, captions, audio, and what never appears.
- [templates/claude-brief-template.md](templates/claude-brief-template.md) — the brief sent to Claude for each video: topic, verified facts, hook, 7-scene shape, fact flags, standing rules.
- [templates/publish-pack-template.md](templates/publish-pack-template.md) — the per-video pack: title, description, hashtags, thumbnail pick, facts checked, and the publishing checklist.

## Scripts

- `scripts/make-scene-thumbnails.py` — builds labelled thumbnails from extracted video frames with PIL (cream rounded labels over the burned-in captions).

## Credit

The animation method is inspired by [Grow With Kaz's Claude 2D animation workflow](https://youtu.be/bxfmJLSHLCg). Everything in this repo is written in our own words — no third-party prompts or assets are reproduced here.

## License

MIT — see [LICENSE](LICENSE).
