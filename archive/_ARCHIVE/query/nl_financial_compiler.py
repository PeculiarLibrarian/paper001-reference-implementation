"""
PADI Natural Language Financial Compiler
Version: 1.2.0 (SIGNATURE AWARE)
"""

class NLFinancialCompiler:

    VERSION = "1.2.0"

    # ---------------------------------------
    # OPERATION SIGNATURE REGISTRY
    # ---------------------------------------

    SIGNATURES = {
        "growth_strength": ("entity", "metric"),
        "stability_index": ("entity", "metric"),
        "health_score": ("entity", "metric"),

        "rank_entities": ("metric",),
        "compare_metric": ("metric",),
        "time_series": ("entity", "metric"),

        "metric_query": ("entity", "metric"),
    }

    # ---------------------------------------
    # INTENT PARSER
    # ---------------------------------------

    def parse(self, query: str):

        q = query.lower()

        intent = {
            "type": None,
            "metric": None,
            "operation": None
        }

        if "compare" in q:

            intent["type"] = "comparison"

            if "stability" in q:
                intent["operation"] = "stability_index"

            elif "growth" in q:
                intent["operation"] = "growth_strength"

            elif "health" in q:
                intent["operation"] = "health_score"

            else:
                intent["operation"] = "compare_metric"

        elif "rank" in q:
            intent["type"] = "ranking"
            intent["operation"] = "rank_entities"

        elif "trend" in q:
            intent["type"] = "temporal"
            intent["operation"] = "time_series"

        else:
            intent["type"] = "metric"
            intent["operation"] = "metric_query"

        if "revenue" in q:
            intent["metric"] = "service_revenue"

        return intent

    # ---------------------------------------
    # EXECUTION COMPILER
    # ---------------------------------------

    def compile(self, query: str, runtime):

        intent = self.parse(query)

        reasoning = runtime["reasoning"]

        op = intent["operation"]

        signature = self.SIGNATURES.get(op, ("entity", "metric"))

        def executor(*args, **kwargs):

            # -----------------------------
            # ARGUMENT NORMALIZATION
            # -----------------------------

            if len(args) == 1 and isinstance(args[0], dict):
                args = args[0]

            # -----------------------------
            # DISPATCH LOGIC
            # -----------------------------

            if op == "stability_index":
                return reasoning["stability_index"](*args)

            if op == "growth_strength":
                return reasoning["growth_strength"](*args)

            if op == "health_score":
                return reasoning["health_score"](*args)

            if op == "rank_entities":
                return reasoning["rank_entities"](*args)

            if op == "compare_metric":
                return reasoning["compare_metric"](*args)

            if op == "time_series":
                return reasoning["time_series"](*args)

            return reasoning["metric_query"](*args)

        return {
            "intent": intent,
            "operation": op,
            "signature": signature,
            "executor": executor
        }
