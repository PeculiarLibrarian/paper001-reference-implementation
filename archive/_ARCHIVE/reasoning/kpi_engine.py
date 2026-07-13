from peculiarlibrary.reasoning.temporal_normalizer import TemporalNormalizer

class KPIEngine:
    """
    Extended semantic KPI engine with temporal awareness.
    """

    def __init__(self, compiled_graph):
        self.graph = compiled_graph["graph"]
        self.temporal = TemporalNormalizer()

    def _filter_metric(self, metric):
        return [
            (str(s), str(p), float(o), str(s).split("/")[-1])
            for s, p, o in self.graph
            if str(p).endswith(metric.split("/")[-1])
        ]

    def time_series(self, entity, metric):
        data = [
            {
                "entity": s,
                "value": o,
                "period": p
            }
            for s, p, o, _ in self._filter_metric(metric)
            if entity in s
        ]

        return self.temporal.normalize(data)

    def growth(self, entity, metric):
        series = self.time_series(entity, metric)

        if len(series) < 2:
            return 0

        newest = series[-1]["value"]
        oldest = series[0]["value"]

        return (newest - oldest) / (oldest or 1)

    def health_score(self, entity, metric):
        series = self.time_series(entity, metric)

        if not series:
            return 0.0

        values = [s["value"] for s in series]

        stability = 1 / (1 + (max(values) - min(values)))
        trend = self.growth(entity, metric)

        return round((stability + abs(trend)) / 2, 4)
