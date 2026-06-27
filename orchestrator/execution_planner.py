from typing import List

from contracts.manager_dependency_contract import ManagerDependencyContract
from contracts.manager_manifest import ManagerManifest


class ExecutionPlanner:

    def plan(self) -> List[str]:

        graph = ManagerDependencyContract.DEPENDENCIES
        manifest = ManagerManifest.manifest()

        #
        # Architectural validation
        #

        for manager in graph:

            if manager not in manifest:
                raise RuntimeError(
                    f"{manager} missing from ManagerManifest."
                )

        resolved = []

        unresolved = set(graph.keys())

        available = set()

        while unresolved:

            progress = False

            for node in list(unresolved):

                deps = graph[node]["depends_on"]

                if all(dep in available for dep in deps):

                    resolved.append(node)

                    unresolved.remove(node)

                    #
                    # publish outputs
                    #

                    for output in graph[node]["produces"]:
                        available.add(output)

                    progress = True

            if not progress:

                raise RuntimeError(
                    f"Unresolvable dependency graph: {unresolved}"
                )

        return resolved
