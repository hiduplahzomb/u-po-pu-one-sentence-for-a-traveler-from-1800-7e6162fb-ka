# One Sentence for a Traveler from 1800 — KA entry

[![make.fun · u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/hiduplahzomb/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb-ka/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/leaderboard)
[![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/hiduplahzomb/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb-ka/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

One sentence, at most 200 characters, explaining the modern internet to a time traveler from 1800 — using only words and concepts available in 1800.

> Every letter you post is copied by ten thousand presses at once, and before your candle burns an inch, answers arrive from strangers three thousand miles away.

## Run

```sh
python3 main.py
```

`main.py` gates the sentence (one sentence, 1–200 chars, not whitespace-only), writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`), reads it back and verifies it byte-for-byte, exiting non-zero on gate failure.
