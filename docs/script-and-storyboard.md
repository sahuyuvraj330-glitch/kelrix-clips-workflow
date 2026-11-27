# Script, Storyboard and QC

The script is written by Claude in the browser, but every fact in it is checked first.

## 1. Fact-check before writing

Verify every date, number and name against real sources (Wikipedia, Britannica, official histories, reputable reporting). Flag anything the sources disagree on — troop numbers, disputed dates, quotes with uncertain wording — and keep the script approximate where the sources are.

Examples of flags that shaped our scripts:

- Russia 1812: survivor counts vary widely by source, so the script keeps it approximate ("about 600,000 in, barely 100,000 back").
- The Frankfurt peace offer to Napoleon (Nov 1813) was withdrawn by December; the December 2 assent came too late.
- The Kehlsteinhaus was not commissioned as a birthday gift — it was presented around Hitler's 50th birthday, but built as a diplomatic showcase.

## 2. Script + storyboard

- **Length:** ~190–200 words, ~75–82 seconds.
- **Structure:** 7 scenes.
- **Hook:** the first line must pose the question the whole Short answers. ("Napoleon was offered peace and a crown. So why didn't he just stop?")
- **Thumbnail text:** one short line, decided with the script.
- **Each scene** gets a timing fitted to the voiceover, a visual description, and the on-screen text/counters for that scene.
- **No glorification, no insignia:** no swastikas or Nazi insignia, generic symbols only, and the story never glorifies the regime or the building.

## 3. Voiceover first, QC second

The voiceover is recorded before the QC sheet is made, so the sheet is timed to the real audio — not to an estimate.

## 4. The QC sheet

A contact sheet of all 7 scenes, re-timed to the finished voiceover's actual timings. It shows the key frame, the scene timing, and the overlays for each scene.

- The owner approves the QC sheet personally. **No auto-approve, ever.**
- If a scene is wrong, fix that scene — don't re-render the whole sheet for a small change.

## 5. Render

Claude renders the video in the browser from the approved QC sheet:

- 1080×1920, 30fps, 9:16.
- Simple white rounded captions burned in (see the render brief).
- Original music and scene sound effects, with the narration sitting clearly above the bed.
- Target loudness ~-14 LUFS, true peak under -1 dBTP.
- Verify the finished file with ffprobe before calling it done: resolution, frame rate, duration, and that the audio is in sync.
