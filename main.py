"""Funniest One-Line Out-of-Office Reply.

Writes one out-of-office auto-reply line to /output/entry.txt.

The bounty gate: the entry must be UTF-8 text of 1 to 160 characters,
a single line, and not only white space. validate() enforces exactly
that before anything is written, so a bad line can never reach the file.
"""

import os

LINE = "I am out of the office until Tuesday. I left detailed instructions for my replacement: me, but on Monday, and much less cheerful."

MAX_CHARS = 160


def validate(text):
    """Return True only if text passes the bounty gate."""
    if not isinstance(text, str):
        return False
    if text.strip() == "":
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main():
    if not validate(LINE):
        raise ValueError("entry fails the bounty gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
