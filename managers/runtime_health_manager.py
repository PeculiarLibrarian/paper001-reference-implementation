from kernel.runtime_manifest import RuntimeManifest
from contracts.architecture_validator import ArchitectureValidator


class RuntimeHealthManager:
    """
    Canonical runtime health observer.

    Owns:

        runtime health

    Never:

        executes managers
        mutates runtime
        performs reasoning
    """

    def handshake(self):

        return {
            "manager": "RuntimeHealthManager",
            "version": "1.0",
            "contract": "manager_contract",
            "capabilities": [
                "inspect",
                "health",
                "manifest",
            ],
        }

    def execute(self):

        architecture = ArchitectureValidator().validate()

        manifest = RuntimeManifest().build()

        return {

            "healthy": architecture["valid"],

            "validated": architecture["valid"],

            "runtime_manifest": manifest,

            "summary": {

                "manager_count":
                    manifest["manager_count"],

                "dependency_count":
                    manifest["dependency_count"],

                "output_count":
                    len(manifest["outputs"]),

            }

        }
