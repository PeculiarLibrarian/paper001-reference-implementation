#!/data/data/com.termux/files/usr/bin/bash
set -e

SHACL="./apache-jena-6.1.0/bin/shacl"

GRAPH="peculiarlibrary/STORE/graphstore/5ac4205a6f41c9df30f9999761317f46a2c3e8a2cfb2a25c1a40909ee29ac714.ttl"

echo "============================================================"
echo "Experiment 02"
echo "Positive SHACL Validation"
echo "============================================================"
echo "Graph:"
echo "$GRAPH"
echo

OUTPUT=$("$SHACL" validate \
  --shapes peculiarlibrary/SHACL/core_shacl.ttl \
  --data "$GRAPH")

echo "$OUTPUT"

echo
echo "EXPECTED: sh:conforms true"

echo "$OUTPUT" | grep -q "sh:conforms  true"

echo
echo "STATUS: PASS"
