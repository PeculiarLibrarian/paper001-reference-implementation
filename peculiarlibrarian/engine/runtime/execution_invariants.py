"""
Execution Invariants
Hard constraints for operator execution ordering.
"""

class ExecutionInvariants:

    # Canonical pipeline order (immutable)
    PIPELINE_ORDER = [
        "compile",
        "reason",
        "validate",
        "audit"
    ]

    # Allowed forward transitions only
    ALLOWED_TRANSITIONS = {
        "compile": {"reason"},
        "reason": {"validate"},
        "validate": {"audit"},
        "audit": set()
    }

    @staticmethod
    def validate_transition(current: str, next_op: str):
        allowed = ExecutionInvariants.ALLOWED_TRANSITIONS.get(current, set())

        if next_op not in allowed:
            raise RuntimeError(
                f"Invalid transition: {current} → {next_op}. "
                f"Allowed: {allowed}"
            )

        return True

    @staticmethod
    def is_valid_pipeline(executed_ops: list):
        """
        Ensures full execution sequence respects ordering.
        """

        for i in range(len(executed_ops) - 1):
            current = executed_ops[i]
            next_op = executed_ops[i + 1]

            ExecutionInvariants.validate_transition(current, next_op)

        return True
