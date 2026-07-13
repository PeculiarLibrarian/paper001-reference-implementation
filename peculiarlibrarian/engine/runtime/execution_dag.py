class ExecutionDAG:
    """
    Hard invariant execution order enforcement.

    This is a deterministic state machine, not a scheduler.

    NOTE:
    - This DAG governs EXECUTION operators only.
    - QUERY operators (e.g., SPARQL) are outside lifecycle enforcement.
    """

    ORDER = ["compile", "reason", "validate", "audit"]
    QUERY_OPERATORS = {"sparql"}

    def __init__(self):
        self.completed = set()

    def validate_transition(self, operator_name: str):
        # Skip DAG validation for query operators (they are isolated)
        if operator_name in self.QUERY_OPERATORS:
            return  # no DAG enforcement for query operators

        # Validate lifecycle operators only
        if operator_name not in self.ORDER:
            raise ValueError(f"Unknown DAG node: {operator_name}")

        idx = self.ORDER.index(operator_name)

        # Must complete all previous steps first
        for prior in self.ORDER[:idx]:
            if prior not in self.completed:
                raise ValueError(
                    f"DAG violation: '{operator_name}' cannot run before '{prior}'"
                )

        self.completed.add(operator_name)

    def reset(self):
        self.completed = set()

    def snapshot(self):
        return {
            "completed": list(self.completed),
            "remaining": [
                o for o in self.ORDER if o not in self.completed
            ]
        }
