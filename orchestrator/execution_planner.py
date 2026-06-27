from contracts.manager_manifest import ManagerManifest
from contracts.manager_dependency_contract import ManagerDependencyContract


class ExecutionPlanner:

    def plan(self, profile="default"):

        manifest = ManagerManifest.manifest(profile)

        dependency_graph = ManagerDependencyContract.DEPENDENCIES

        active_managers = set(manifest.keys())

        dependency_graph = {
            manager: spec
            for manager, spec in dependency_graph.items()
            if manager in active_managers
        }

        resolved = []

        unresolved = set(dependency_graph.keys())

        available_outputs = set()

        while unresolved:

            progress = False

            for manager in list(unresolved):

                dependencies = dependency_graph[manager]["depends_on"]

                if all(
                    dependency in available_outputs
                    for dependency in dependencies
                ):

                    resolved.append(manager)

                    unresolved.remove(manager)

                    for produced in dependency_graph[manager]["produces"]:
                        available_outputs.add(produced)

                    progress = True

            if not progress:

                raise RuntimeError(
                    "Unable to resolve execution profile "
                    f"'{profile}'. Remaining managers: "
                    f"{sorted(unresolved)}"
                )

        return resolved
