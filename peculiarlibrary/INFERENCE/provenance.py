"""
PADI Provenance Layer
Version: 2.0.0

Records constitutional provenance for every inferred statement.

Purpose
-------
Every derived statement SHALL be traceable back to:

    • inference rule
    • supporting canonical facts
    • execution identifier
    • execution timestamp

This module never performs inference.
It only records provenance.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4


# ============================================================
# PROVENANCE RECORD
# ============================================================

@dataclass(frozen=True)
class ProvenanceRecord:
    rule_id: str
    supporting_facts: tuple[str, ...]
    derived_statement: str
    record_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: str = field(
        default_factory=lambda: (
            datetime.now(UTC)
            .replace(microsecond=0)
            .isoformat()
        )
    )

    @classmethod
    def create(
        cls,
        rule_id: str,
        supporting_facts: list[str] | tuple[str, ...],
        derived_statement: str,
    ) -> "ProvenanceRecord":
        return cls(
            rule_id=rule_id,
            supporting_facts=tuple(supporting_facts),
            derived_statement=derived_statement,
        )

    def to_dict(self):
        return {
            "record_id": self.record_id,
            "rule_id": self.rule_id,
            "supporting_facts": list(self.supporting_facts),
            "derived_statement": self.derived_statement,
            "timestamp": self.timestamp,
        }


# ============================================================
# PROVENANCE LEDGER
# ============================================================

class ProvenanceLedger:
    """
    Immutable provenance ledger.
    """

    def __init__(self):
        self._records: list[ProvenanceRecord] = []
        self._sealed = False

    # --------------------------------------------------------

    def add(self, record: ProvenanceRecord):

        if self._sealed:
            raise RuntimeError(
                "Provenance Ledger is sealed."
            )

        self._records.append(record)

    # --------------------------------------------------------

    def seal(self):
        self._sealed = True

    # --------------------------------------------------------

    @property
    def sealed(self):
        return self._sealed

    # --------------------------------------------------------

    def __len__(self):
        return len(self._records)

    # --------------------------------------------------------

    def __iter__(self):
        return iter(self._records)

    # --------------------------------------------------------

    def statistics(self):
        return {
            "records": len(self),
            "sealed": self._sealed,
        }

    # --------------------------------------------------------

    def export(self):
        return [
            record.to_dict()
            for record in self._records
        ]
