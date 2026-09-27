#!/usr/bin/env python3
"""Fact lock for plain-English rewrites.

Compares a BEFORE and AFTER text and fails if a fact moved:
  - numbers (digits and number words, compared as values, so "six" == "6")
  - percentages and years
  - study citations (Surname ... YEAR, "Surname and colleagues")
  - capitalised names that appear mid-sentence (authors, programs, places)
  - text inside double quotes (quoted wording must survive word for word)

Usage:
  python3 fact_lock.py before.md after.md
Exit code 0 = no fact moved, 1 = something was lost or added.

Added facts are reported too: a definition the rewrite introduced is a new
claim that someone has to check.
"""
import re
import sys
from collections import Counter

WORD_NUMS = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
    "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1000,
    "million": 1000000, "half": 0.5, "quarter": 0.25,
}
# Words that look like numbers in ordinary speech and would only add noise.
SKIP_WORDS = {"one"}

# Capitalised words that are not names: sentence openers, title words, months.
NOT_NAMES = {
    "in", "by", "from", "since", "until", "after", "before", "during", "of", "on",
    "at", "for", "to", "the", "a", "an", "and", "but", "or", "so", "if", "when",
    "your", "you", "yours", "our", "we", "they", "their", "this", "that", "these",
    "those", "it", "its", "he", "she", "his", "her", "day", "step", "what", "how",
    "why", "who", "where", "which", "with", "without", "about", "not", "no",
    "yes", "then", "now", "here", "there", "one", "some", "most", "many", "each",
    "every", "all", "any", "both", "try", "say", "tick", "write", "pick", "keep",
    "stop", "start", "done", "later", "today", "tomorrow", "yesterday",
}
SENTENCE_START = re.compile(r"(?:^|[.!?:]\s+|\n\s*[-*\d.]*\s*)([A-Z][a-z]+)")


def number_words(text):
    vals = []
    for m in re.finditer(r"\b([a-z]+)(?:-([a-z]+))?\b", text.lower()):
        a, b = m.group(1), m.group(2)
        if a in WORD_NUMS and a not in SKIP_WORDS:
            v = WORD_NUMS[a]
            if b and b in WORD_NUMS:
                v += WORD_NUMS[b]
            vals.append(v)
    return vals


def facts(text):
    out = Counter()
    for n in re.findall(r"\d+(?:[.,]\d+)?%?", text):
        n = n.replace(",", "")
        out[("number", n.rstrip("%"))] += 1
        if n.endswith("%"):
            out[("percent", n)] += 1
    for v in number_words(text):
        out[("number", str(int(v)) if float(v).is_integer() else str(v))] += 1
    for m in re.finditer(r"\b([A-Z][A-Za-z'\-]+)(?:,? (?:and|&) [A-Z][A-Za-z'\-]+| and colleagues| et al\.?)?,? (?:\(|reported in |in )?((?:19|20)\d\d)\b", text):
        if m.group(1).lower() in NOT_NAMES:
            continue
        out[("citation", f"{m.group(1)} {m.group(2)}")] += 1
    for m in re.finditer(r"(?<=[a-z,;] )([A-Z][A-Za-z'\-]{2,})", text):
        w = m.group(1)
        if w.lower() not in NOT_NAMES:
            out[("name", w)] += 1
    for q in re.findall(r"[\"“]([^\"”]{3,200})[\"”]", text):
        out[("quote", q.strip())] += 1
    return out


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    before = open(sys.argv[1], encoding="utf-8").read()
    after = open(sys.argv[2], encoding="utf-8").read()
    b, a = facts(before), facts(after)
    lost = b - a
    added = a - b
    ok = True
    for (kind, val), n in sorted(lost.items()):
        if kind == "number" and ("percent", val + "%") in lost:
            continue
        print(f"LOST   {kind:8} {val}  (x{n})")
        ok = False
    for (kind, val), n in sorted(added.items()):
        print(f"ADDED  {kind:8} {val}  (x{n})  <- new claim, check it")
        if kind in ("number", "percent", "citation"):
            ok = False
    print("FACT LOCK:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
