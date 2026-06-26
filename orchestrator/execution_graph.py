from typing import Dict, List
from contracts.manager_dependency_contract import ManagerDependencyContract


class ExecutionGraph:
    """
    Builds a dependency graph from manager contracts.
    """

    def __init__(self):
        self.contracts = ManagerDependencyContract.DEPENDENCIES

    def build(self) -> Dict[str, List[str]]:
        """
        Returns adjacency list:
        {
            "InstanceManager": ["OntologyManager"]
        }
        """
        graph = {}

        for node, spec in self.contracts.items():
            graph[node] = spec.get("depends_on", [])

        return graph
