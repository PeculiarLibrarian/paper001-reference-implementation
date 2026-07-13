"""
PADI Evidence Runtime
Version: 1.3.0

Construct immutable inference-ready evidence records from
either CanonicalFact semantic objects or legacy dictionaries.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class EvidenceRecord:
    fact_id: str
    entity: str
    metric: str
    value: object
    unit: str | None
    period: str | None
    confidence: float
    source: dict


class EvidenceRuntime:

    def build_records(
        self,
        facts: Iterable,
    ) -> tuple[EvidenceRecord, ...]:

        records = []

        for index, fact in enumerate(facts, start=1):

            # CanonicalFact semantic object
            if hasattr(fact, "entity"):
                entity = fact.entity.name
                metric = fact.metric.name
                value = fact.value
                period = fact.period.label if fact.period is not None else None
                unit = fact.unit.name if fact.unit is not None else None
                confidence = fact.confidence
                source = (
                    fact.source.__dict__
                    if fact.source is not None
                    else {}
                )

            # Legacy dictionary
            else:
                entity = fact["subject"]
                metric = fact["predicate"]
                value = fact["object"]
                period = fact.get("period")
                unit = fact.get("unit")
                confidence = fact.get("confidence", 1.0)
                source = fact.get("source", {})

            records.append(
                EvidenceRecord(
                    fact_id=f"Fact_{index:05d}",
                    entity=entity,
                    metric=metric,
                    value=value,
                    unit=unit,
                    period=period,
                    confidence=confidence,
                    source=source,
                )
            )

        return tuple(records)
