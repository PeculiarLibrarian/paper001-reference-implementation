"""
PADI Execution Runtime
Version: 1.0.0

The runtime is the sole execution boundary.

Responsibilities:
- Execute one ExecutionStep.
- Dispatch to registered handlers.
- Return deterministic outputs.

No planning.
No orchestration.
"""

from peculiarlibrary.execution.execution_plan import ExecutionStep


class ExecutionRuntime:

    VERSION = "1.0.0"

    def __init__(self):

        self._handlers = {}

    def register(self, operation: str, handler):

        if operation in self._handlers:
            raise ValueError(f"Handler already registered: {operation}")

        self._handlers[operation] = handler

    def execute(self, step: ExecutionStep):

        if step.operation not in self._handlers:
            raise ValueError(
                f"No runtime handler registered for '{step.operation}'"
            )

        handler = self._handlers[step.operation]

        return handler(step.parameters)
