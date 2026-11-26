#!/usr/bin/env python3
"""The Worst Pizza Topping — make.fun entry.

Writes one funny line pitching a terrible pizza topping to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Python 3.13 standard library only. No network at run time.
"""

import os
from pathlib import Path

ENTRY = "Raisin pizza: grapes that gave up halfway."


def main() -> None:
    # Gate assertions: the entry must be exactly one line,
    # 1-200 characters, non-empty and not only whitespace.
    assert isinstance(ENTRY, str), "entry must be a string"
    assert ENTRY, "entry must not be empty"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(ENTRY + "\n", encoding="utf-8")

    # Verify what was actually written passes the gate too.
    written = output_path.read_text(encoding="utf-8")
    lines = written.splitlines()
    assert len(lines) == 1, "output must be exactly one line"
    assert lines[0] == ENTRY, "written line must match the entry"
    assert 1 <= len(lines[0]) <= 200, "written line must be 1-200 characters"


if __name__ == "__main__":
    main()
