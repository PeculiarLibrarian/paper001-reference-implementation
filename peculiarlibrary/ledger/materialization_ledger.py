"""
PADI Semantic Materialization Ledger
Version: 0.3.1

Maintains immutable semantic materialization records.

Canonical representation:
    JSON-LD
"""

from datetime import datetime, timezone
from pathlib import Path
import json


class SemanticMaterializationLedger:

    VERSION = "0.3.1"

    CONTEXT = {
        "@vocab": "http://padi.s.m.gitandu.bs/core#",
        "materializationId": "materializationId",
        "compilerVersion": "compilerVersion",
        "mapper": "mapper",
        "dataset": "dataset",
        "timestamp": "timestamp",
        "tripleCount": "tripleCount",
        "validation": "validation",
        "provenance": "provenance",
    }

    def __init__(self):
        self.records = []

    def record(
        self,
        *,
        materialization_id,
        compiler_version,
        mapper,
        dataset,
        triple_count,
        validation=True,
        provenance=None,
    ):

        entry = {
            "@context": self.CONTEXT,
            "@type": "Materialization",
            "materializationId": materialization_id,
            "compilerVersion": compiler_version,
            "mapper": mapper,
            "dataset": dataset,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "tripleCount": triple_count,
            "validation": validation,
            "provenance": provenance or {},
        }

        self.records.append(entry)

        return entry

    def latest(self):
        return self.records[-1] if self.records else None

    def all(self):
        return list(self.records)

    def serialize(self, destination):

        path = Path(destination)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with path.open(
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(
                self.records,
                f,
                indent=2,
                ensure_ascii=False,
            )

        return str(path)
