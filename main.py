#!/usr/bin/env python3
"""One-Line Office Joke: the empty square gets promoted.

Writes the chosen line to /output/entry.txt as UTF-8, with no trailing
newline. Deterministic: no clock, no randomness, no network, no
environment reads, no dependency outside this repository. The text is
147 Unicode code points, inside the gate's 1-200 characters.
"""

import os

TEXT = "My camera stayed off for the whole meeting, and my manager still thanked me for my 'great contributions' — my empty square is now up for promotion."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts characters, and one line means
    # exactly the text, nothing after it.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
