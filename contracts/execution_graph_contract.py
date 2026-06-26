from typing import Dict, Any, List


class ExecutionGraphContract:
    """
    Declarative A2A execution graph.

    Replaces Orchestrator hardcoding.

    Each manager declares:
    - inputs
    - outputs
    - dependencies
    """

    def nodes(self) -> Dict[str, Dict[str, Any]]:
        """
        Example:
        {
            "OntologyManager": {
                "depends_on": [],
                "produces": ["graph"]
            }
        }
        """
        raise NotImplementedError

    def resolve_order(self) -> List[str]:
        """
        Topologically resolve execution order.
        """
        raise NotImplementedError
