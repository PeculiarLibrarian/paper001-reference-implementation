from collections import Counter

from contracts.manager_manifest import ManagerManifest
from contracts.manager_dependency_contract import ManagerDependencyContract


class RuntimeIntrospector:
    """
    Canonical runtime observer.

    Executes no business logic.

    Produces a complete architectural view
    of the runtime.
    """

    def inspect(self):

        manifest = ManagerManifest.manifest()

        dependencies = ManagerDependencyContract.DEPENDENCIES

        layer_counter = Counter()

        outputs = []

        contracts = set()

        managers = []

        for name, spec in manifest.items():

            managers.append(name)

            layer_counter.update(
                [spec["layer"]]
            )

            outputs.extend(
                spec["produces"]
            )

            contracts.add(
                tuple(spec["produces"])
            )

        return {

            "manager_count": len(managers),

            "managers": sorted(managers),

            "layers": dict(layer_counter),

            "output_count": len(outputs),

            "outputs": sorted(outputs),

            "dependency_count": len(dependencies),

        }
