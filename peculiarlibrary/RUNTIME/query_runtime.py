"""
PADI Query Runtime
Version: 1.0.0

Deterministic query execution over the canonical semantic dataset.

Responsibilities
----------------
- Query canonical evidence records.
- Perform deterministic ranking and comparison.
- Expose time-series retrieval.
- Compute simple financial indicators.

Non-responsibilities
--------------------
- SHACL validation.
- Constitution execution.
- Finality.
- SPARQL orchestration.
"""

from collections import defaultdict


class QueryRuntime:

    VERSION = "1.0.0"

    def __init__(self, dataset):
        self.dataset = dataset
        self.records = tuple(dataset.records)

    def _records_for_metric(self, metric):
        return [
            r
            for r in self.records
            if r.metric == metric
        ]

    def _records_for_entity_metric(self, entity, metric):
        return [
            r
            for r in self.records
            if r.entity == entity and r.metric == metric
        ]

    def compare(self, metric):
        return self._records_for_metric(metric)

    def rank(self, metric):
        return sorted(
            self._records_for_metric(metric),
            key=lambda r: r.value,
            reverse=True,
        )

    def time_series(self, entity, metric):
        rows = self._records_for_entity_metric(
            entity,
            metric,
        )

        return sorted(
            rows,
            key=lambda r: r.period or "",
        )

    def growth_strength(self, entity, metric):
        rows = self.time_series(entity, metric)

        if len(rows) < 2:
            return None

        first = rows[0].value
        last = rows[-1].value

        return {
            "entity": entity,
            "metric": metric,
            "first": first,
            "last": last,
            "growth": last - first,
        }

    def health_score(self, entity, metric):
        rows = self.time_series(entity, metric)

        if not rows:
            return None

        values = [r.value for r in rows]

        return {
            "entity": entity,
            "metric": metric,
            "latest": values[-1],
            "minimum": min(values),
            "maximum": max(values),
            "observations": len(values),
        }
