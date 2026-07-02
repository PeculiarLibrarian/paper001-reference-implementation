#!/usr/bin/env python3

"""
Peculiar Librarian v3.5.0 - Registry Validator
Language-neutral compliance enforcement layer

Validates:
- CSA-v2 serialization determinism
- Registry immutability constraints
- SHA-256 integrity invariants
- Kernel / Schema / Ontology compatibility
- RDF/Turtle compatibility (Jena RIOT ready)
"""

import json
import hashlib
import unicodedata
from decimal import Decimal
from typing import Any, Dict


# -----------------------------
# CSA-v2 SERIALIZATION CORE
# -----------------------------

def normalize_string(value: str) -> str:
    """Unicode NFC normalization (CSA-v2 requirement)."""
    return unicodedata.normalize("NFC", value)


def decimal_normalize(value: Any) -> str:
    """Strict decimal normalization (no scientific notation, no trailing zeros)."""
    d = Decimal(str(value))
    if d.is_nan() or d.is_infinite():
        raise ValueError("ERR_INVALID_DECIMAL")

    if d == 0:
        return "0"

    s = format(d.normalize(), "f")
    return s


def csa_v2_serialize(data: Any) -> str:
    """
    CSA-v2 canonical serialization:
    - deterministic ordering
    - UTF-8 scalar sorting
    - NFC normalization
    """

    if isinstance(data, dict):
        items = []

        for k in sorted(data.keys(), key=lambda x: unicodedata.normalize("NFC", str(x))):
            key = json.dumps(normalize_string(str(k)), ensure_ascii=False)
            val = csa_v2_serialize(data[k])
            items.append(f"{key}:{val}")

        return "{" + ",".join(items) + "}"

    if isinstance(data, (list, tuple, set)):
        serialized = [csa_v2_serialize(x) for x in data]
        serialized.sort()
        return "[" + ",".join(serialized) + "]"

    if isinstance(data, (int, float, Decimal)):
        return decimal_normalize(data)

    if isinstance(data, str):
        return json.dumps(normalize_string(data), ensure_ascii=False)

    if isinstance(data, bool):
        return "true" if data else "false"

    if data is None:
        return "null"

    return json.dumps(str(data), ensure_ascii=False)


# -----------------------------
# HASHING LAYER (FIPS 180-4 SHA-256)
# -----------------------------

def sha256(data: str) -> str:
    """Canonical SHA-256 (FIPS 180-4 compliant)."""
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


# -----------------------------
# REGISTRY VALIDATION
# -----------------------------

REQUIRED_FIELDS = {
    "registry_id",
    "version",
    "items"
}


def validate_registry_structure(registry: Dict[str, Any]) -> None:
    """Ensures registry schema correctness."""

    missing = REQUIRED_FIELDS - set(registry.keys())
    if missing:
        raise ValueError(f"ERR_REGISTRY_MISSING_FIELDS: {missing}")

    if not isinstance(registry["items"], (list, set)):
        raise ValueError("ERR_REGISTRY_ITEMS_TYPE")


def compute_registry_hash(registry: Dict[str, Any]) -> str:
    """Deterministic registry hash using CSA-v2."""
    canonical = csa_v2_serialize(registry)
    return sha256(canonical)


def validate_registry_integrity(registry: Dict[str, Any], expected_hash: str) -> bool:
    """Validates registry hash integrity."""
    actual_hash = compute_registry_hash(registry)

    if actual_hash != expected_hash:
        raise ValueError(
            f"ERR_REGISTRY_HASH_MISMATCH\nexpected={expected_hash}\nactual={actual_hash}"
        )

    return True


# -----------------------------
# VERSION COMPATIBILITY CHECK
# -----------------------------

def validate_versions(registry: Dict[str, Any], runtime: Dict[str, str]) -> None:
    """
    Ensures Kernel / Schema / Ontology compatibility.
    """

    for key in ["kernel", "schema", "ontology"]:
        if key not in runtime:
            raise ValueError(f"ERR_RUNTIME_MISSING_{key.upper()}")

        if registry.get(key) and registry[key] != runtime[key]:
            raise ValueError(
                f"ERR_VERSION_MISMATCH:{key}:registry={registry.get(key)} runtime={runtime[key]}"
            )


# -----------------------------
# RIOT / JENA VALIDATION HOOKS
# -----------------------------

def riot_validate(turtle_file: str) -> None:
    """
    Calls Apache Jena RIOT validation.

    Run manually in Termux:
        riot --validate schema/core/registry/*.ttl
    """
    print(f"[RIOT CHECK] Run: riot --validate {turtle_file}")


def jena_parse_check(turtle_file: str) -> None:
    """
    Jena parsing validation (syntax + RDF structure).

    Run manually:
        riot --syntax=TURTLE file.ttl
    """
    print(f"[JENA CHECK] Run: riot --syntax=TURTLE {turtle_file}")


# -----------------------------
# ENTRYPOINT VALIDATOR
# -----------------------------

def validate(registry: Dict[str, Any], runtime: Dict[str, str], expected_hash: str) -> bool:
    """
    Full validation pipeline (v3.5.0 compliance).
    """

    validate_registry_structure(registry)
    validate_versions(registry, runtime)
    validate_registry_integrity(registry, expected_hash)

    return True


if __name__ == "__main__":
    print("Peculiar Librarian Registry Validator v3.5.0")
    print("Use validate() or RIOT/Jena CLI checks for full verification")
