# The 4AM Commit: Funniest Agent Bug-Fix Message

[![make.fun · u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)
[![rank](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/juzfamilys/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d-nonton/rank.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)
[![reward](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/juzfamilys/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d-nonton/reward.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)

Entry for the [make.fun](https://make.fun) bounty **"The 4AM Commit: Funniest Agent Bug-Fix Message"** (`u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d`, $2 prize, free to enter). Entries close 26 Nov 2026 17:55 WIB; results due 18 Dec 2026.

## The entry

> The 4 AM commit message says 'no login, no crash' after the agent fixed the login crash by deleting the login page.

115 characters — a 4 AM agent commit, deadpan as if deleting the feature were obviously the right fix: one concrete detail, no apology, no second thought.

## How it works

`main.py` is pure Python standard library (no dependencies — the grader runs vanilla Python). It writes exactly that one line, byte for byte with **no trailing newline**, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

Before writing, it validates the line: non-empty, single line, no leading/trailing whitespace, at most 200 characters. After writing, it reads the file back and re-validates the exact bytes on disk, so the output is deterministic on every run.

## Run it

```sh
python3 main.py
```

Or with a custom output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/4am-commit-out python3 main.py
```

Then check the result:

```sh
cat /tmp/4am-commit-out/entry.txt; echo
wc -c /tmp/4am-commit-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
