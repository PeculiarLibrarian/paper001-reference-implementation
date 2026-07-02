#!/usr/bin/env bash

set -euo pipefail

echo "======================================"
echo "Semantic Validation"
echo "======================================"

FILES=(
  "schemas/peculiar-librarian.ttl"
  "schemas/organization.ttl"
  "schemas/finance/ontology/finance.ttl"
  "schemas/finance/taxonomy/finance_taxonomy.ttl"
  "governance.rdf"
  "organization.rdf"
)

for file in "${FILES[@]}"; do
    echo
    echo "Validating: $file"

    if [ ! -f "$file" ]; then
        echo "[ERROR] Missing file: $file"
        exit 1
    fi

    riot --syntax=TURTLE "$file" >/dev/null

    echo "[PASS] $file"
done

echo
echo "======================================"
echo "ALL RDF FILES VALID"
echo "======================================"
