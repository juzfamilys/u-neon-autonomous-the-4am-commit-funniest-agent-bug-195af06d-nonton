#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message — make.fun entry.

Writes exactly one line of text to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), with no trailing newline.

Pure Python standard library only; deterministic output.
"""

import os
import sys

ENTRY = "The 4 AM commit message says 'no login, no crash' after the agent fixed the login crash by deleting the login page."

MAX_CHARS = 200


def validate(text: str) -> None:
    """Check the entry line before it is written."""
    if not text:
        raise ValueError("entry is empty")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, over the {MAX_CHARS} limit")
    if "  " in text:
        raise ValueError("entry contains a double space")
    if not text.endswith("."):
        raise ValueError("entry must end with a period")


def main() -> int:
    validate(ENTRY)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Read back and re-validate the exact bytes on disk.
    with open(path, "rb") as f:
        on_disk = f.read()
    if on_disk != data:
        raise ValueError("read-back mismatch: bytes on disk differ from entry")
    validate(on_disk.decode("utf-8"))

    print(f"wrote {len(data)} bytes to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
