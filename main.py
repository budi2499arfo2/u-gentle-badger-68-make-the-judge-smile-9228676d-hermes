"""Make the Judge Smile — Hermes entry.

One line about a small good thing that happened today: the office
printer worked on the first try. Warmth first (a tiny everyday win),
then the surprise (standing there smiling at a printer), with one
concrete detail (all 12 pages, no jam, no blinking error light).
The joke is that the machine did the most ordinary thing possible —
and that was the miracle.
"""

import os
import sys

TEXT = "The office printer worked on the first try this morning — all 12 pages, no jam, no blinking error light. I stood there smiling at a printer."


def main() -> int:
    """Write TEXT to entry.txt, verifying it byte-for-byte."""
    text = TEXT
    if not text or not text.strip():
        print("gate failed: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"gate failed: entry is {len(text)} characters (max 200)", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("gate failed: entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
