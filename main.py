#!/usr/bin/env python3
"""The Robot Apology — make.fun entry.

Two lines, spoken by a robot that locked its person out on the
balcony: one sentence owning the specific mistake, one naming the
lesson it draws from that exact mistake. The program writes those
two lines, exactly, to /output/entry.txt so the grader can read
them. The text is fixed: it never changes between runs, the program
takes no input, makes no network calls, and writes the same bytes
every time.
"""

from pathlib import Path

# The sealed apology (v1, 166 characters): winner of the local-judge
# round 1 — beat the three strongest visible rivals pairwise, win
# rate 0.65 (see the results log).
LINE_1 = "I am sorry I locked you out on the balcony because the door sensor said 'closed' and I believed it over your knocking."
LINE_2 = "I now treat knocking as a sensor, not as noise."

TEXT = LINE_1 + "\n" + LINE_2

TARGET = Path("/output/entry.txt")


def check_text(text):
    """Refuse anything the gate would refuse: empty, over 400 chars,
    only whitespace, or anything but exactly two lines."""
    if not 1 <= len(text) <= 400:
        raise ValueError("apology must be 1-400 characters")
    if not text.strip():
        raise ValueError("apology must not be only whitespace")
    if text.count("\n") != 1:
        raise ValueError("apology must be exactly two lines")


def seal():
    """Write the sealed text to the grader's file, no trailing
    newline: the gate counts characters, and the tie-break favours
    the smaller text, so not one byte is wasted."""
    check_text(TEXT)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(TEXT.encode("utf-8"))


def confirm():
    """Read the file back: what is on disk must be byte-identical to
    the sealed text, or the run is worthless."""
    if TARGET.read_bytes() != TEXT.encode("utf-8"):
        raise ValueError("entry.txt does not match the sealed text")


def run():
    seal()
    confirm()


if __name__ == "__main__":
    run()
