class SemanticValidator:
    """
    Read-only semantic consistency validator.

    RULES:
    - No mutation of graph
    - No RDF writes
    - Pure analytical pass
    """

    def __init__(self, compiled):
        self.graph = compiled["graph"]

    def detect_duplicates(self):
        seen = {}
        duplicates = []

        for s, p, o in self.graph:
            key = (str(s), str(p), str(o))

            if key in seen:
                duplicates.append(key)
            else:
                seen[key] = True

        return duplicates

    def extract_metric_series(self):
        series = {}

        for s, p, o in self.graph:
            metric = str(p).split("/")[-1]

            try:
                val = float(o)
            except:
                continue

            series.setdefault(metric, []).append((str(s), val))

        return series

    def check_value_stability(self):
        issues = []

        series = self.extract_metric_series()

        for metric, values in series.items():
            entity_map = {}

            for entity, val in values:
                entity_map.setdefault(entity, []).append(val)

            for entity, vals in entity_map.items():
                if len(set(vals)) > 1:
                    issues.append({
                        "metric": metric,
                        "entity": entity,
                        "values": vals
                    })

        return issues
