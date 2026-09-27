#!/usr/bin/env python3
"""Find copy that repeats between programs, or too often inside one.

The 2026-09-05 content audit found whole paragraphs copied between programs
and the same positioning line ("this program never ...") dozens of times.
This scan finds both. It reads the folders that extract_program.cjs writes,
one folder per program.

Usage:
  python3 shared_runs.py /tmp/programs            # every program folder in it
  python3 shared_runs.py /tmp/programs/word_swap /tmp/programs/bouncing_back
  python3 shared_runs.py /tmp/programs --n=8 --inside=3

Reports:
  ACROSS  an N-word run found in two or more programs (default N = 8)
  INSIDE  an N-word run found INSIDE times or more in one program (default 3)
Shared promises marked [SHARED:...] by the extractor are skipped. They are
meant to be identical.

Exit code 0 = nothing found, 1 = something to look at. Not every hit is a
fault: a quoted study line or a technique name can repeat for a reason. Each
hit needs a reason or a rewrite.
"""
import os
import re
import sys
from collections import defaultdict


def words(text):
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"\[SHARED:[A-Z_]+\]", " | ", text)
    text = re.sub(r"\*\*[a-z]+_d\d+_[rc]\d+\*\*", " | ", text)
    return re.findall(r"[a-z0-9']+|\|", text.lower())


def runs(tokens, n):
    for i in range(len(tokens) - n + 1):
        chunk = tokens[i : i + n]
        if "|" not in chunk:
            yield " ".join(chunk)


def main():
    opts = {a.split("=")[0]: a.split("=")[1] for a in sys.argv[1:] if a.startswith("--")}
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    n = int(opts.get("--n", 8))
    inside = int(opts.get("--inside", 3))
    if not paths:
        print(__doc__)
        return 2
    folders = []
    for p in paths:
        subs = [os.path.join(p, d) for d in sorted(os.listdir(p)) if os.path.isdir(os.path.join(p, d))]
        folders.extend(subs if subs else [p])

    texts = {}
    for folder in folders:
        prog = os.path.basename(folder.rstrip("/"))
        toks = []
        for name in sorted(os.listdir(folder)):
            if name.endswith(".md"):
                with open(os.path.join(folder, name), encoding="utf-8") as f:
                    toks += words(f.read()) + ["|"]
        texts[prog] = toks

    where = defaultdict(set)
    count = defaultdict(lambda: defaultdict(int))
    for prog, toks in texts.items():
        for r in runs(toks, n):
            where[r].add(prog)
            count[prog][r] += 1

    def passages(prog, keep):
        """Join overlapping runs that pass `keep` into whole passages."""
        toks, out, i = texts[prog], [], 0
        while i <= len(toks) - n:
            r = " ".join(toks[i : i + n])
            if "|" not in toks[i : i + n] and keep(r):
                j = i
                while j + 1 <= len(toks) - n and "|" not in toks[j + 1 : j + 1 + n] and keep(" ".join(toks[j + 1 : j + 1 + n])):
                    j += 1
                out.append((r, " ".join(toks[i : j + n])))
                i = j + n
            else:
                i += 1
        return out

    found = False
    seen = set()
    for prog in sorted(texts):
        for first, passage in passages(prog, lambda r: len(where[r]) > 1):
            progs = tuple(sorted(where[first]))
            if (passage, progs) in seen:
                continue
            seen.add((passage, progs))
            print(f"ACROSS  {', '.join(progs)}\n        \"{passage}\"")
            found = True
    for prog in sorted(texts):
        shown = set()
        for first, passage in passages(prog, lambda r, p=prog: count[p][r] >= inside):
            if passage in shown:
                continue
            shown.add(passage)
            print(f"INSIDE  {prog} x{count[prog][first]}\n        \"{passage}\"")
            found = True
    print("SHARED RUNS:", "some found, give each a reason or rewrite it" if found else "none")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
