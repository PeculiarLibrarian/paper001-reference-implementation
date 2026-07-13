"""
PADI Execution Planner
Version: 1.0.0

Transforms execution requests into immutable execution plans.

The planner is pure:
- No graph access
- No compiler execution
- No reasoning
- No SPARQL
- No side effects
"""

from uuid import uuid4

from peculiarlibrary.execution.execution_plan import (
    ExecutionPlan,
    ExecutionStep,
)


class ExecutionPlanner:

    VERSION = "1.0.0"

    _PIPELINES = {
        "compile": (
            ExecutionStep(
                stage="compile",
                operation="semantic_compile",
            ),
        ),
        "reason": (
            ExecutionStep(
                stage="reason",
                operation="infer",
            ),
        ),
        "query": (
            ExecutionStep(
                stage="query",
                operation="sparql_query",
            ),
        ),
        "materialize": (
            ExecutionStep(
                stage="materialize",
                operation="serialize_graph",
            ),
        ),
        "compile_and_reason": (
            ExecutionStep(
                stage="compile",
                operation="semantic_compile",
            ),
            ExecutionStep(
                stage="reason",
                operation="infer",
            ),
        ),
    }

    def create_plan(self, request: dict) -> ExecutionPlan:

        action = request["action"]

        if action not in self._PIPELINES:
            raise ValueError(f"Unknown execution action: {action}")

        parameters = request.get("parameters", {})

        steps = []

        for step in self._PIPELINES[action]:
            steps.append(
                ExecutionStep(
                    stage=step.stage,
                    operation=step.operation,
                    parameters=parameters,
                )
            )

        return ExecutionPlan(
            version=self.VERSION,
            request_id=str(uuid4()),
            steps=tuple(steps),
        )
