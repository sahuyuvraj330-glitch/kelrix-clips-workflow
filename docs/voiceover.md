# Voiceover

One voice for every Short, same pace, verified word-for-word.

## The voice

- **Helio**, the same voice for every Kelrix Short — channel consistency matters more than variety.
- **Pace:** ~147–154 words per minute, natural and unhurried.
- Never switch voices without being asked.

## The split-render method

Long or date/number-dense scripts can make a text-to-speech engine loop — repeating a phrase over and over in the middle of the render. Every full-script render of one of our dense scripts looped at the same spot, at every speed.

The fix:

1. **Split the script in halves.**
2. **Render each half separately** at speed 100.
3. **Stitch the halves** with only a ~0.3s gap at the join.
4. Add no extra pauses and apply no tempo change.

The speed control works fine on short text — it's the long dense render that trips the engine.

## Verify before sending

Transcribe the stitched audio and check:

- Every word of the script is present, in order.
- The word count matches the script.
- No phrase repeats or loops.
- The total length matches the target pace.

Only a clean transcription gets sent for approval. A render that loops is a failed render — don't try another full-length speed, use the split method.

## Optional polish

The approved voiceover can be run through Adobe Podcast Enhance Speech (free account, default settings) for a cleaner sound. Keep the original file untouched and verify the enhanced file by transcription too — it must still be the complete script.

## Approval

Send the voiceover to the owner for approval. If there's no reply within 1 hour, it auto-approves and the work proceeds.
