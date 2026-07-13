"""
PADI Canonical Mapper

Purpose
-------
Transform canonical JSON facts into immutable MODEL objects.

Boundary:
canonical_facts.json
        ↓
CanonicalFact
"""

from peculiarlibrary.MODEL import (
    CanonicalFact,
    Entity,
    Metric,
    Period,
    Unit,
    EvidenceSource,
)


class CanonicalMapper:

    VERSION = "1.0.1"

    def map_fact(self, payload: dict) -> CanonicalFact:

        source_payload = payload.get(
            "source",
            {}
        )

        return CanonicalFact(
            entity=Entity(
                payload["subject"]
            ),
            metric=Metric(
                payload["predicate"]
            ),
            value=payload["object"],
            unit=(
                Unit(payload["unit"])
                if payload.get("unit")
                else None
            ),
            period=Period(
                payload["period"]
            ),
            source=EvidenceSource(
                document=source_payload.get(
                    "document"
                ),
                page=source_payload.get(
                    "page"
                ),
                section=source_payload.get(
                    "section"
                ),
                context=source_payload.get(
                    "context"
                ),
            ),
            confidence=payload.get(
                "confidence",
                1.0
            ),
        )

    def map_facts(self, facts):

        return tuple(
            self.map_fact(fact)
            for fact in facts
        )
