from collections import defaultdict

from contracts.manager_manifest import ManagerManifest
from contracts.manager_dependency_contract import ManagerDependencyContract


class ArchitectureValidator:
    """
    Validates the architectural integrity of the runtime.

    It never executes managers.

    It only validates contracts.
    """

    def validate(self):

        manifest = ManagerManifest.manifest()

        dependencies = ManagerDependencyContract.DEPENDENCIES

        #
        # 1. Every dependency manager exists
        #

        for manager in dependencies:

            if manager not in manifest:

                raise RuntimeError(
                    f"{manager} missing from ManagerManifest."
                )

        #
        # 2. Collect producers
        #

        producers = defaultdict(list)

        for manager, spec in dependencies.items():

            for output in spec["produces"]:

                producers[output].append(manager)

        #
        # 3. Every output has one producer
        #

        for output, owners in producers.items():

            if len(owners) > 1:

                raise RuntimeError(
                    f"Output '{output}' has multiple producers: {owners}"
                )

        #
        # 4. Every dependency is produced
        #

        for manager, spec in dependencies.items():

            for dependency in spec["depends_on"]:

                if dependency not in producers:

                    raise RuntimeError(
                        f"{manager} depends on unknown output '{dependency}'."
                    )

        return {
            "valid": True,
            "managers": len(manifest),
            "outputs": len(producers),
        }
