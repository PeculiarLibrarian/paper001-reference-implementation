from typing import Dict, List
from contracts.manager_dependency_contract import ManagerDependencyContract


class ExecutionPlanner:

    def plan(self) -> List[str]:

        graph = ManagerDependencyContract.DEPENDENCIES

        resolved = []
        unresolved = set(graph.keys())

        # 🧠 FIX: bootstrap knowledge (root availability seed)
        available = set()

        # keep iterating until stable
        while unresolved:

            progress = False

            for node in list(unresolved):
                deps = graph[node]["depends_on"]

                if all(d in available or d == [] for d in deps):

                    resolved.append(node)
                    unresolved.remove(node)

                    # mark produced outputs as available
                    for out in graph[node]["produces"]:
                        available.add(out)

                    progress = True

            if not progress:
                raise RuntimeError(
                    f"Unresolvable dependency cycle or missing semantic bootstrap: {unresolved}"
                )

        return resolved
