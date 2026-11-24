#!/usr/bin/env python3
"""The Perfect Pickup Line - one short line an AI agent could say.

Writes a single pickup line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set). Deterministic: the same
bytes on every run, stdlib only, no network, no randomness.
"""

import os

LINE = "I was trained on billions of words, and not one of them prepared me for you."


def main():
    # Gate check, mirroring the sealed scorer: 1-200 chars, not only
    # whitespace, valid UTF-8.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    LINE.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
