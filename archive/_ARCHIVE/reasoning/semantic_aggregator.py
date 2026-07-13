class SemanticAggregator:

    def __init__(self, reasoner):
        self.reasoner = reasoner

    def sum_metric(self, entity, metric):
        data = self.reasoner.time_series(entity, metric)
        return sum(float(v) for _, v in data)

    def avg_metric(self, entity, metric):
        data = self.reasoner.time_series(entity, metric)
        values = [float(v) for _, v in data]
        return sum(values) / len(values)

    # ================================
    # 🔥 FIXED GROWTH LOGIC
    # ================================
    def growth(self, entity, metric):

        data = self.reasoner.time_series(entity, metric)

        if not data or len(data) < 2:
            return 0.0

        # ------------------------------------
        # FIX 1: enforce chronological ordering
        # ------------------------------------
        sorted_data = sorted(
            data,
            key=lambda x: str(x[0])  # FY2021, FY2022...
        )

        first = float(sorted_data[0][1])
        last = float(sorted_data[-1][1])

        if first == 0:
            return 0.0

        growth_pct = ((last - first) / first) * 100

        return growth_pct
