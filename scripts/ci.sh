#!/usr/bin/env bash

set -euo pipefail

echo
echo "======================================"
echo "PECULIAR LIBRARIAN SEMANTIC CI"
echo "======================================"

./scripts/bootstrap.sh

echo
echo "Running syntax validation..."
./scripts/validate.sh

echo
echo "======================================"
echo "SEMANTIC CI PASSED"
echo "READY FOR DEVELOPMENT"
echo "======================================"
