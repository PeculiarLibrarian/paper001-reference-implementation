"""
PADI Execution Orchestrator
Version: 1.0.0

Coordinates execution plans.

Responsibilities:
- Accept an ExecutionPlan
- Execute each step in order
- Delegate all work to the runtime
- Aggregate execution results

No business logic.
No RDF logic.
No ontology logic.
"""

from dataclasses import dataclass, field
from typing import Any

from peculiarlibrary.execution.execution_plan import ExecutionPlan


@dataclass(frozen=True, slots=True)
class ExecutionResult:
    stage: str
    operation: str
    success: bool
    output: Any = None


@dataclass(frozen=True, slots=True)
class ExecutionReport:
    request_id: str
    results: tuple[ExecutionResult, ...]

    @property
    def successful(self) -> bool:
        return all(result.success for result in self.results)


class ExecutionOrchestrator:

    VERSION = "1.0.0"

    def __init__(self, runtime):
        self.runtime = runtime

    def execute(self, plan: ExecutionPlan) -> ExecutionReport:

        results = []

        for step in plan:

            output = self.runtime.execute(step)

            results.append(
                ExecutionResult(
                    stage=step.stage,
                    operation=step.operation,
                    success=True,
                    output=output,
                )
            )

        return ExecutionReport(
            request_id=plan.request_id,
            results=tuple(results),
        )
