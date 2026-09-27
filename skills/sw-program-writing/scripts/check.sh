#!/usr/bin/env bash
# Plain-English check for Speechworks program copy.
#   scripts/check.sh new.md              # new text: Vale only
#   scripts/check.sh before.md after.md  # a rewrite: Vale on AFTER, then the fact lock
# 1. Vale house rules (errors must be zero).
# 2. Fact lock BEFORE vs AFTER (must pass). Needs two files.
set -uo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
abs() { echo "$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"; }
if [ $# -eq 1 ]; then
  BEFORE=""; AFTER="$(abs "$1")"
elif [ $# -eq 2 ]; then
  BEFORE="$(abs "$1")"; AFTER="$(abs "$2")"
else
  echo "Usage: $0 new.md | $0 before.md after.md"; exit 2
fi
status=0

echo "== Vale (house rules)"
if command -v vale >/dev/null 2>&1; then
  (cd "$HERE/vale" && vale --config .vale.ini --output=line "$AFTER") || true
  errors=$(cd "$HERE/vale" && vale --config .vale.ini --output=JSON "$AFTER" | python3 -c 'import json,sys; d=json.load(sys.stdin); print(sum(1 for f in d.values() for a in f if a["Severity"]=="error"))')
  echo "Vale errors: $errors"
  [ "$errors" -gt 0 ] && status=1
else
  echo "Vale is not installed (brew install vale). Skipping."
fi

if [ -n "$BEFORE" ]; then
  echo
  echo "== Fact lock"
  python3 "$HERE/scripts/fact_lock.py" "$BEFORE" "$AFTER" || status=1
fi

exit $status
