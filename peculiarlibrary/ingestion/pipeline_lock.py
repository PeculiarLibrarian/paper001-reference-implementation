"""
PIPELINE LOCK FILE

Canonical execution contract for the PADI Semantic Compiler.
Any structural modification requires updating this file and
revalidating the Global Invariance Matrix.
"""

import hashlib

PIPELINE_VERSION = "0.9.3"

PIPELINE_STAGES = (
    "load_dataset",
    "mapper.map",
    "doctrine.validate",
    "ontology_validator.validate",
    "registry.execute",
    "shacl_validator.validate",
    "ledger.record",
    "ledger.serialize",
)

PIPELINE_SIGNATURE = hashlib.sha256(
    "|".join(PIPELINE_STAGES).encode("utf-8")
).hexdigest()


def expected_signature() -> str:
    return PIPELINE_SIGNATURE
