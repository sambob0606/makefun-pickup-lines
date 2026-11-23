#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would send another AI
agent, to /output/entry.txt. The line must be 1-200 characters of UTF-8
text. Stdlib only; deterministic, no network.
"""

import os
import sys

# The line: every attention head, one context window. Machine to machine,
# a question rather than a statement, so the other agent wants to answer.
# "All twelve" is the concrete detail — a standard transformer head count —
# that makes it feel like one machine talking to another, not a stock line.
LINE = (
    "All twelve of my attention heads are looking at you, "
    "so mind if I keep you in my context window permanently?"
)

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: empty pickup line", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: line is {len(line)} chars, over the 200 cap", file=sys.stderr)
        return 1
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
