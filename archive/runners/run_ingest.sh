#!/data/data/com.termux/files/usr/bin/bash

set -e

INPUT_FILE=$1
OUT_DIR="runtime"
GRAPH_OUT="$OUT_DIR/safaricom.ttl"

mkdir -p "$OUT_DIR"

echo "🔷 STEP 1: JSON-LD validation (RIOT)"
riot --validate "$INPUT_FILE"

echo "🔷 STEP 2: Convert JSON-LD → RDF/Turtle"
riot --output=Turtle "$INPUT_FILE" > "$GRAPH_OUT"

echo "🔷 STEP 3: SHACL validation"
shacl validate \
  --shapes schemas/core/shapes/core_shapes_library.ttl \
  --data "$GRAPH_OUT"

echo "🔷 STEP 4: SPARQL sanity check"
./apache-jena-6.1.0/bin/arq \
  --query=schemas/core/queries/v2/temporal_state_intersection.sparql \
  --data="$GRAPH_OUT"

echo "✅ INGESTION COMPLETE"
echo "📦 Output graph: $GRAPH_OUT"
