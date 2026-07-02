#!/usr/bin/env bash

set -euo pipefail

echo "[Phase 5] Finance Domain"

./scripts/ci.sh

echo
echo "Environment validated."
echo "Proceed with finance ontology development."
