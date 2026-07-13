"""
Natural Language Financial Compiler

Version: 2.1.0

Compiles natural-language requests into canonical runtime
operations.

No reasoning implementations live here.
"""


class NLFinancialCompiler:

    VERSION = "2.1.0"

    def compile(self, query: str, runtime=None):

        q = query.lower().strip()

        if q.startswith("compare"):
            return {
                "operation": "compare",
                "signature": "compare",
            }

        if q.startswith("rank"):
            return {
                "operation": "rank",
                "signature": "rank",
            }

        if q.startswith("growth"):
            return {
                "operation": "growth",
                "signature": "growth",
            }

        if q.startswith("health"):
            return {
                "operation": "health",
                "signature": "health",
            }

        if q.startswith("ts") or q.startswith("time"):
            return {
                "operation": "time_series",
                "signature": "time_series",
            }

        return {
            "operation": "ask",
            "signature": "ask",
        }
