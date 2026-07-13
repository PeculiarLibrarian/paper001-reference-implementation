#!/usr/bin/env bash
set -e

pandoc PAPER001.md \
  --citeproc \
  --bibliography=bibliography.bib \
  --metadata=lang=en \
  --standalone \
  -o PAPER001.html

sed -i \
  -e 's/>Https:\/\//>https:\/\//g' \
  -e 's/PROV-o/PROV-O/g' \
  PAPER001.html

echo "✓ PAPER001.html built successfully"
