from typing import Any, Dict

from orchestrator.execution_engine import ExecutionEngine


class Orchestrator:
    """
    Minimal A2A kernel entrypoint.
    No knowledge of managers.
    """

    def run(self, ttl: Any) -> Dict[str, Any]:
        engine = ExecutionEngine()
        return engine.run()
