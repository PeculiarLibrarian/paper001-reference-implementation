from kernel.semantic.field_resolver import FieldResolver

class Query10SemanticEngine:

    @staticmethod
    def transform(rows):

        enriched = []

        for r in rows:

            revenue = r.get("revenue")
            net_profit = FieldResolver.pick(r, "net_profit", "netProfit")
            eps = r.get("eps")
            fcf = r.get("fcf")

            net_margin = r.get("net_margin")
            fcf_conv = r.get("fcf_conversion")

            enriched.append({
                "year": r.get("year"),
                "revenue": revenue,
                "net_profit": net_profit,
                "eps": eps,
                "fcf": fcf,

                # preserve computed metrics ONLY if valid
                "net_margin": net_margin,
                "fcf_conversion": fcf_conv,

                "query_version": "query_10_v4"
            })

        return enriched
