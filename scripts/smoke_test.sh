#!/usr/bin/env bash
set -euo pipefail

output=$(python3 scripts/local_simulator.py --count 1)

if ! echo "$output" | grep -q "Pipeline complete"; then
  echo "Smoke test failed: expected pipeline completion message." >&2
  exit 1
fi

if ! echo "$output" | grep -q '"event_id": "evt-1"'; then
  echo "Smoke test failed: expected event payload." >&2
  exit 1
fi

echo "Smoke test passed."
