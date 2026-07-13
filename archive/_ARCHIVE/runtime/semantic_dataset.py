class SemanticDataset:
    """
    Runtime semantic projection layer.
    """

    def __init__(self, compiled_graph):
        self.graph = compiled_graph["graph"]

    def compare(self, metric):
        results = []
        for s, p, o in self.graph:
            if str(p).endswith(metric.split("/")[-1]):
                try:
                    results.append({
                        "entity": str(s),
                        "value": float(o)
                    })
                except:
                    continue
        return sorted(results, key=lambda x: x["value"], reverse=True)

    def rank(self, metric):
        return self.compare(metric)
