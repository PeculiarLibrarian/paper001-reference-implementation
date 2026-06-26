from typing import Any, Dict

from orchestrator.manager_registry import ManagerRegistry
from orchestrator.execution_planner import ExecutionPlanner
from contracts.manager_dependency_contract import ManagerDependencyContract


class ExecutionEngine:

    def run(self) -> Dict[str, Any]:

        registry = ManagerRegistry.get()
        planner = ExecutionPlanner()

        order = planner.plan()

        context: Dict[str, Any] = {}
        outputs: Dict[str, Any] = {}

        dependencies = ManagerDependencyContract.DEPENDENCIES

        for name in order:

            manager = registry[name]

            manager.load()

            required = dependencies[name]["depends_on"]

            # 🔥 HARD GATE: enforce dependency satisfaction
            missing = [r for r in required if r not in context]

            if missing:
                raise RuntimeError(
                    f"{name} blocked. Missing dependencies: {missing}"
                )

            result = manager.execute(context)

            if not isinstance(result, dict):
                result = {}

            outputs[name] = result

            context.update(result)

        return {
            "execution_order": order,
            "outputs": outputs,
            "ready": True,
        }
