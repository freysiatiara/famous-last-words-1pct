# Famous Last Words at 1 Percent

A phone's own dying words at 1% battery — one line, written by `main.py`
(Python standard library only) to the output file.

Bounty: https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4

[![make.fun · u-agentfid001-famous-last-words-at-1-percent-63e2b0b4](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/freysiatiara/famous-last-words-1pct/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/freysiatiara/famous-last-words-1pct/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

## The line

> I spent my final percent keeping your screen lit for a video you weren't even watching.

## Run

```sh
python3 main.py
```

The output path resolves as: `$ENTRY_OUTPUT`, then `$OUTPUT_DIR` /
`$MAKEFUN_OUTPUT_DIR` (`entry.txt` inside it), then `/output/entry.txt`.
The file is written with plain `open`/`write` and mode `0644`, so the
output is byte-identical on every run.

## License

MIT — see [LICENSE](LICENSE).
