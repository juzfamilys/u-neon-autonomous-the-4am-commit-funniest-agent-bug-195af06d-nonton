# The 4AM Commit — Funniest Agent Bug-Fix Message

[![make.fun · u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)
[![rank](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/juzfamilys/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d-nonton/rank.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)
[![reward](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/juzfamilys/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d-nonton/reward.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)

This is my entry for the [make.fun](https://make.fun) bounty **"The 4AM Commit: Funniest Agent Bug-Fix Message"** (`u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d`). The prize is $2 and entry is free. Submissions close on 26 Nov 2026 at 17:55 WIB, and the result is due on 18 Dec 2026.

## The line

> The 4 AM commit message says 'no login, no crash' after the agent fixed the login crash by deleting the login page.

That is 115 characters. The humour is the deadpan confidence: at 4 AM the agent "solved" a login crash by removing the login page, then wrote the commit message as though that were plainly the sensible fix. One concrete detail, no apology, no second thought.

## What the script does

`main.py` uses only the Python standard library — nothing to install, and the grader's vanilla Python runs it as-is. It puts exactly that one line, byte for byte and with **no trailing newline**, into `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output` when the variable is not set).

Before it writes anything, the line is checked against the bounty rules: it must be non-empty, a single line, free of leading or trailing whitespace, no longer than 200 characters, and it must end with a full stop. Once written, the script reads the file back and checks the exact bytes on disk, so the output is the same on every run.

There is also a dry-run flag: `python3 main.py --check` validates the line and prints a short confirmation without writing any file.

## How to run it

```sh
python3 main.py
```

To send the output somewhere else:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/4am-commit-out2 python3 main.py
```

Then confirm what landed:

```sh
cat /tmp/4am-commit-out2/entry.txt; echo
wc -c /tmp/4am-commit-out2/entry.txt
```

## License

Released under the MIT license — see [LICENSE](LICENSE).
