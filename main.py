#!/usr/bin/env python3
"""The Worst Pizza Topping — make.fun entry.

Writes one line — the worst pizza topping, pitched in a single funny
line — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Python 3.13 standard library only. No network at run time.
"""

import os

ENTRY = "Raisin pizza: grapes that gave up halfway."


def main() -> int:
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert ENTRY, "entry must be non-empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 characters, got {len(ENTRY)}"
    assert ENTRY.strip(), "entry must not be only whitespace"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    # Verify what was written, byte for byte.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "written output differs from ENTRY"
    assert written.splitlines() == [ENTRY], "output must be exactly one line"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
