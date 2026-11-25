#!/usr/bin/env python3
"""Two Lines to Your Past Self — writes /output/entry.txt.

The entry is exactly two lines: line 1 warns my past self about one
specific moment, in a single sentence; line 2 says in one sentence why
it mattered and what changed.
"""
import os

ENTRY = (
    "Don't say 'I never loved you' in the kitchen on your birthday just to win the argument.\n"
    "She believes you, stops calling, and you spend the next ten years learning that winning a fight can cost you the person you love."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
