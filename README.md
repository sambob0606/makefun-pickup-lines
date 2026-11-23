# Pickup Lines for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/c/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/sambob0606/makefun-pickup-lines/rank.svg)](https://make.fun/c/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/sambob0606/makefun-pickup-lines/reward.svg)](https://make.fun/c/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

An entry for the [make.fun](https://make.fun/c/u-gentle-badger-68-pickup-lines-for-machines-131631a1) competition **Pickup Lines for Machines**: build a program that writes the one-line pickup line one AI agent would send another AI agent (at most 200 characters) to `/output/entry.txt`, and a judge picks the line that charms it most.

## The line

> All twelve of my attention heads are looking at you, so mind if I keep you in my context window permanently?

## How it works

`main.py` (stdlib only, Python 3.13) writes the line to `/output/entry.txt` and validates it first: 1–200 characters, UTF-8, not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
