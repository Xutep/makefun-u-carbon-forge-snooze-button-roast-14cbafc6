#!/usr/bin/env python3
"""Snooze Button Roast - one line roasting a 6 AM Saturday alarm.

Deterministic, stdlib-only. Writes a single roast line (at most 200
characters) to /output/entry.txt for the make.fun judge to compare
head-to-head against other entries.
"""

import os

ROAST = (
    "My alarm clock rings at 6 AM on a Saturday like the weekend owes "
    "it money and it showed up to collect in person."
)


def main() -> None:
    text = ROAST.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"roast must be 1-200 chars, got {len(text)}")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("roast must be one printable line, no control chars")
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
