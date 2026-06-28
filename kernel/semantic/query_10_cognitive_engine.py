class Query10CognitiveEngine:

    def __init__(self, timeline):
        self.data = timeline

    def compute(self):

        enriched = []

        for i, row in enumerate(self.data):

            revenue = row["revenue"]
            net_profit = row["net_profit"]
            eps = row["eps"]
            fcf = row["free_cash_flow"]

            margin = row["net_margin"]
            fcf_conv = row["fcf_conversion"]

            # -----------------------------
            # CAUSAL SIGNALS
            # -----------------------------

            margin_drop_signal = None
            eps_stagnation = None
            fcf_shock = None

            if i > 0:

                prev = self.data[i - 1]

                margin_drop_signal = margin < prev["net_margin"]

                eps_stagnation = abs(eps - prev["eps"]) < 0.05

                fcf_shock = fcf < prev["free_cash_flow"] * 0.6

            # -----------------------------
            # STRUCTURAL DECOMPOSITION FLAGS
            # -----------------------------

            structural_distortion = (
                margin < 0.15 and revenue > 300000
            )

            enriched.append({
                "year": row["year"],

                # core metrics
                "revenue": revenue,
                "net_profit": net_profit,
                "eps": eps,
                "fcf": fcf,

                # structural ratios
                "net_margin": margin,
                "fcf_conversion": fcf_conv,

                # causal layer
                "margin_drop": margin_drop_signal,
                "eps_stagnation": eps_stagnation,
                "fcf_shock": fcf_shock,

                # structural system state
                "structural_distortion": structural_distortion,
            })

        return enriched
