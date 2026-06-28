class Query10Reasoner:

    def __init__(self, enriched_rows):
        self.rows = sorted(enriched_rows, key=lambda x: x["year"])

    def compute(self):

        results = []

        prev = None

        for row in self.rows:

            revenue = row["revenue"]
            net_profit = row["net_profit"]
            eps = row["eps"]
            fcf = row["free_cash_flow"]

            # -----------------------------
            # Core structural metrics
            # -----------------------------
            net_margin = row["net_margin"]
            fcf_conversion = row["fcf_conversion"]

            # -----------------------------
            # Temporal deltas (YoY logic)
            # -----------------------------
            if prev:

                revenue_growth = (
                    (revenue - prev["revenue"]) / prev["revenue"]
                    if prev["revenue"] else None
                )

                eps_growth = (
                    (eps - prev["eps"]) / prev["eps"]
                    if prev["eps"] else None
                )

                fcf_growth = (
                    (fcf - prev["free_cash_flow"]) / prev["free_cash_flow"]
                    if prev["free_cash_flow"] else None
                )

            else:
                revenue_growth = None
                eps_growth = None
                fcf_growth = None

            # -----------------------------
            # Structural stress indicators
            # -----------------------------
            margin_pressure = (
                prev["net_margin"] - net_margin
                if prev and prev["net_margin"] else None
            )

            results.append({
                "year": row["year"],
                "revenue": revenue,
                "net_profit": net_profit,
                "eps": eps,
                "free_cash_flow": fcf,
                "net_margin": net_margin,
                "fcf_conversion": fcf_conversion,

                # temporal intelligence
                "revenue_growth": revenue_growth,
                "eps_growth": eps_growth,
                "fcf_growth": fcf_growth,

                # structural dynamics
                "margin_pressure": margin_pressure,
            })

            prev = row

        return results
