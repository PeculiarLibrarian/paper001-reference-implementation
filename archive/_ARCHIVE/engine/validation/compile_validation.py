from rdflib import Graph, URIRef


class CompileValidation:

    def validate(self, result):
        errors = []

        # =========================
        # 1. INTEGRITY CHECKS
        # =========================
        integrity = result.get("integrity", {})

        if integrity.get("fact_triples", 0) == 0:
            errors.append("FACT_TRIPLES_EMPTY")

        if integrity.get("semantic_triples", 0) == 0:
            errors.append("SEMANTIC_TRIPLES_EMPTY")

        # =========================
        # 2. GRAPH CHECKS
        # =========================
        graph = result.get("graph")

        if graph is None:
            errors.append("GRAPH_MISSING")
        else:
            try:
                size = len(list(graph))
                if size == 0:
                    errors.append("GRAPH_EMPTY")
            except Exception:
                errors.append("GRAPH_INVALID_ITERABLE")

        # =========================
        # 3. RUNTIME CONTRACT CHECKS
        # =========================
        runtime = result.get("runtime", {})

        required_runtime_keys = [
            "graph",
            "reasoning",
            "multi_entity",
            "compiled_source"
        ]

        for k in required_runtime_keys:
            if k not in runtime:
                errors.append(f"RUNTIME_MISSING_{k.upper()}")

        # =========================
        # 4. REASONING LAYER CHECK
        # =========================
        reasoning = runtime.get("reasoning", {})

        required_reasoning = [
            "time_series",
            "sum_metric",
            "growth",
            "health_score"
        ]

        for k in required_reasoning:
            if k not in reasoning:
                errors.append(f"REASONING_MISSING_{k.upper()}")

        # =========================
        # FINAL RESULT
        # =========================
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "graph_size": len(list(graph)) if graph else 0,
            "fact_triples": integrity.get("fact_triples"),
            "semantic_triples": integrity.get("semantic_triples"),
        }
