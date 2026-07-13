#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "============================================================"
echo "Experiment 01"
echo "RIOT Syntax Validation"
echo "============================================================"

FILES=(
  peculiarlibrary/RDF/OWL/core_ontology.ttl
  peculiarlibrary/SHACL/core_shacl.ttl
  peculiarlibrary/SKOS/core_skos.ttl
  peculiarlibrary/SKOS/metric_vocabulary.ttl
  peculiarlibrary/SKOS/semantic_mapping.ttl
)

for file in "${FILES[@]}"; do
    echo "Validating: $file"
    riot --validate "$file"
done

echo
echo "RESULT: PASS"
