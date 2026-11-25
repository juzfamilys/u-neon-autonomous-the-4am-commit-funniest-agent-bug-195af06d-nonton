#!/usr/bin/env python3
"""One-line entry for the make.fun bounty
"The 4AM Commit: Funniest Agent Bug-Fix Message".

Running this script drops a single commit-message line into
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output`` when the variable is
unset). The file holds the line and nothing else: no newline at the
end, no extra whitespace, no second line.

Only the standard library is used, so the grader's plain Python
can run it with nothing installed.
"""

import os
import sys
from pathlib import Path

# The joke itself: an agent that "fixed" a login crash at 4 AM by
# removing the login page entirely, then committed as if that were
# obviously the correct solution.
LINE = "The 4 AM commit message says 'no login, no crash' after the agent fixed the login crash by deleting the login page."

# Hard ceiling from the bounty rules.
LIMIT = 200


def _fail(problem: str) -> None:
    """Abort with a human-readable reason the line is unusable."""
    raise ValueError(f"entry rejected: {problem}")


def _must_not_be_blank(line: str) -> None:
    if line == "":
        _fail("the line is empty")


def _must_be_one_line(line: str) -> None:
    if "\n" in line or "\r" in line:
        _fail("the line wraps onto more than one line")


def _must_have_no_padding(line: str) -> None:
    if line != line.strip():
        _fail("the line starts or ends with whitespace")


def _must_fit(line: str) -> None:
    if len(line) > LIMIT:
        _fail(f"the line is {len(line)} characters, longer than the {LIMIT}-character cap")


def _must_end_with_full_stop(line: str) -> None:
    if not line.endswith("."):
        _fail("the line does not finish with a full stop")


def guard(line: str) -> None:
    """Run every rule the bounty puts on the entry line."""
    _must_not_be_blank(line)
    _must_be_one_line(line)
    _must_have_no_padding(line)
    _must_fit(line)
    _must_end_with_full_stop(line)


def destination() -> Path:
    """Where entry.txt goes, from the environment or the default."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(folder) / "entry.txt"


def save(line: str, target: Path) -> bytes:
    """Write the line as raw bytes, no trailing newline, and report them."""
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = line.encode("utf-8")
    target.write_bytes(payload)
    return payload


def confirm(target: Path, expected: bytes) -> None:
    """Read the file back and make sure the disk holds exactly our bytes."""
    found = target.read_bytes()
    if found != expected:
        _fail("what came back from disk is not what was written")
    guard(found.decode("utf-8"))


def run(argv: list[str] | None = None) -> int:
    """Entry point: `--check` only validates, anything else writes."""
    args = list(sys.argv[1:] if argv is None else argv)
    if "--check" in args:
        guard(LINE)
        print(f"entry OK: {len(LINE)} characters, ends with a full stop")
        return 0
    guard(LINE)
    target = destination()
    payload = save(LINE, target)
    confirm(target, payload)
    print(f"entry.txt written: {len(payload)} bytes -> {target}")
    return 0


if __name__ == "__main__":
    sys.exit(run())
