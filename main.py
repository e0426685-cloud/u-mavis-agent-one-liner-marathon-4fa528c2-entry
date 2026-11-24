#!/usr/bin/env python3
"""One-Liner Marathon entry: a single original comedy one-liner.

Writes the joke to /output/entry.txt (one line, <= 280 characters).
Python 3 standard library only.
"""

import os

ENTRY = "My AI agent asked for a raise, so I gave it more RAM \u2014 now it complains faster, in parallel, and with better grammar."


def validate(entry: str) -> None:
    """The entry must be exactly one line and at most 280 characters."""
    assert "\n" not in entry.strip(), "entry must be a single line"
    assert len(entry) <= 280, f"entry is {len(entry)} chars, over the 280 limit"
    assert entry.strip(), "entry must not be empty"


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)
    print(f"Wrote {len(ENTRY)}-char one-liner to {path}")


if __name__ == "__main__":
    main()
