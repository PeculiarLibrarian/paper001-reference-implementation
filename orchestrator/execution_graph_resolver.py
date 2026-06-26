from typing import Dict, List
from contracts.manager_dependency_contract import ManagerDependencyContract


class ExecutionGraphResolver:
    """
    Converts manager contracts into execution order.
    """

    def __init__(self, managers: Dict[str, object]):
        self.managers = managers
        self.contracts = ManagerDependencyContract.DEPENDENCIES

    def resolve(self) -> List[str]:
        resolved = []
        unresolved = set(self.contracts.keys())

        while unresolved:
            progress = False

            for node in list(unresolved):
                deps = self.contracts[node]["depends_on"]

                if all(dep in resolved_outputs for dep in deps):
                    resolved.append(node)
                    unresolved.remove(node)
                    progress = True

            if not progress:
                # fallback safety (cycle detection)
                resolved.extend(list(unresolved))
                break

        return resolved
