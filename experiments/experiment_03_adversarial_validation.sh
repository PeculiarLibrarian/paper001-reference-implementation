#!/data/data/com.termux/files/usr/bin/bash
set -e

SHACL="./apache-jena-6.1.0/bin/shacl"

python tests/adversarial/generate_missing_source_graph.py

GRAPH="peculiarlibrary/STORE/graphstore/invalid_graph.ttl"

echo "============================================================"
echo "Experiment 03"
echo "Adversarial SHACL Validation"
echo "============================================================"
echo "Generated adversarial graph: $GRAPH"
echo

OUTPUT=$("$SHACL" validate \
  --shapes peculiarlibrary/SHACL/core_shacl.ttl \
  --data "$GRAPH")

echo "$OUTPUT"

echo
echo "EXPECTED: sh:conforms false"

echo "$OUTPUT" | grep -q "sh:conforms  false"

echo
echo "STATUS: PASS"
