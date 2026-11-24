"""One Sentence for a Traveler from 1800 — KA entry.

A single sentence, at most 200 characters, explaining the modern
internet to a time traveler from 1800, using only words and concepts
available in 1800 — no post-1800 coinage at all (no internet, computer,
phone, email, website, app, wifi, online, digital, screen).

The picture: a vast letter-office of presses that answers back.
Every letter posted is copied at once, and answers return from
strangers thousands of miles away before a candle burns an inch.
"""

import os
import sys

TEXT = (
    "Every letter you post is copied by ten thousand presses at once, "
    "and before your candle burns an inch, answers arrive from "
    "strangers three thousand miles away."
)


def main() -> int:
    text = TEXT.strip()
    if not text:
        print("gate failed: empty entry", file=sys.stderr)
        return 1
    if text.count("\n") > 0:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print(f"gate failed: {len(text)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("gate failed: entry must be exactly one sentence",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1

    print(f"ok: entry.txt written ({len(text)} chars, 1 sentence)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
