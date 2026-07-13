
from collections import defaultdict


class MultiEntityEngine:
    """
    Cross-entity financial reasoning engine.

    Supports:
    - comparison
    - ranking
    - dominance scoring
    - growth spread analysis
    """

    def __init__(self, graph):
        self.graph = graph

    def _extract(self, metric_uri):

        results = []

        for s, p, o in self.graph.triples((None, None, None)):

            if str(p).endswith(metric_uri.split("/")[-1]):

                results.append((s, o))

        return results

    def compare(self, metric_uri):

        data = self._extract(metric_uri)

        return [
            {
                "entity": str(entity),
                "value": float(value),
            }
            for entity, value in data
        ]

    def rank(self, metric_uri):

        data = self.compare(metric_uri)

        return sorted(data, key=lambda x: x["value"], reverse=True)

    def dominance(self, metric_uri):

        data = self.compare(metric_uri)

        total = sum(x["value"] for x in data) or 1

        return [
            {
                "entity": x["entity"],
                "share_pct": (x["value"] / total) * 100
            }
            for x in data
        ]

    def growth_spread(self, metric_uri):

        data = self.compare(metric_uri)

        values = [x["value"] for x in data]

        if len(values) < 2:
            return {"spread": 0}

        return {
            "min": min(values),
            "max": max(values),
            "spread": max(values) - min(values),
        }

