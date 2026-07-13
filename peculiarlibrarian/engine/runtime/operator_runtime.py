"""
PADI Operator Runtime

Version: 8.1.0

Canonical runtime façade.

Responsibilities
----------------
- Build the Canonical Runtime exactly once.
- Expose runtime services.
- Dispatch high-level operations.
- Never construct reasoning engines directly.
"""

from peculiarlibrary.RUNTIME.canonical_runtime import build_canonical_view
from peculiarlibrary.RUNTIME.runtime_executor import RuntimeExecutor
from peculiarlibrary.query.nl_financial_compiler import NLFinancialCompiler


class OperatorRuntime:

    VERSION = "8.1.0"

    def __init__(self):
        self._compiler = NLFinancialCompiler()

    def execute(self, operation, payload=None):

        payload = payload or {}

        if operation == "compile":

            dataset = build_canonical_view()

            executor = RuntimeExecutor(dataset)

            runtime = {
                "dataset": dataset,
                "executor": executor,
            }

            return {
                "runtime": runtime,
                "dataset": dataset,
                "integrity": {
                    "facts": len(dataset.facts),
                    "records": len(dataset.records),
                    "triples": len(dataset.graph),
                },
            }

        runtime = payload["runtime"]
        executor = runtime["executor"]

        if operation == "query":

            compiled = self._compiler.compile(
                payload["query"],
                runtime,
            )

            op = compiled["operation"]

            if op == "rank":
                return executor.rank(
                    payload["metric"]
                )

            if op == "compare":
                return executor.compare(
                    payload["metric"]
                )

            if op == "time_series":
                return executor.time_series(
                    payload["entity"],
                    payload["metric"],
                )

            if op == "growth":
                return executor.growth_strength(
                    payload["entity"],
                    payload["metric"],
                )

            if op == "health":
                return executor.health_score(
                    payload["entity"],
                    payload["metric"],
                )

            return compiled

        if operation == "rank":
            return executor.rank(
                payload["metric"]
            )

        if operation == "compare":
            return executor.compare(
                payload["metric"]
            )

        if operation == "time_series":
            return executor.time_series(
                payload["entity"],
                payload["metric"],
            )

        if operation == "growth":
            return executor.growth_strength(
                payload["entity"],
                payload["metric"],
            )

        if operation == "health":
            return executor.health_score(
                payload["entity"],
                payload["metric"],
            )

        raise ValueError(
            f"Unknown operation: {operation}"
        )
