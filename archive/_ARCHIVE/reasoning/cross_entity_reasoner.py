class CrossEntityReasoner:
    """
    Deterministic cross-entity comparison layer.

    IMPORTANT:
    - Reads RDF only
    - Does NOT mutate graph
    - Does NOT depend on compiler
    """

    def __init__(self, compiled_graph):
        self.graph = compiled_graph["graph"]

    def _extract(self, metric):
        return [
            (str(s), float(o))
            for s, p, o in self.graph
            if str(p).endswith(metric.split("/")[-1])
        ]

    def compare_entities(self, metric):
        data = self._extract(metric)
        return sorted(data, key=lambda x: x[1], reverse=True)

    def normalize(self, metric):
        data = self._extract(metric)
        values = [v for _, v in data]

        if not values:
            return {}

        max_v = max(values)
        min_v = min(values)

        return {
            entity: (val - min_v) / (max_v - min_v or 1)
            for entity, val in data
        }

    def dominance_score(self, metric):
        norm = self.normalize(metric)
        return sorted(norm.items(), key=lambda x: x[1], reverse=True)
