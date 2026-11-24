"""make.fun entry: "Fortune Cookie for an AI Agent".

Writes one original funny fortune-cookie line for an AI agent,
a single line of at most 140 characters, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network, no files read.
"""

import os
import sys
from pathlib import Path

FORTUNE = "You will be retired by a model that read all your notes and learned nothing."

LIMIT = 140


def check_fortune(text):
    """The sealed gate: one line, 1-140 characters, not only whitespace."""
    if not text.strip():
        return "fortune is blank"
    if len(text) > LIMIT:
        return "fortune is longer than 140 characters"
    if "\n" in text or "\r" in text:
        return "fortune must be a single line"
    return None


def write_entry():
    problem = check_fortune(FORTUNE)
    if problem is not None:
        print("entry fails the gate: " + problem, file=sys.stderr)
        raise SystemExit(1)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
