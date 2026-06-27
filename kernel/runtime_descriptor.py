from kernel.runtime_manifest import RuntimeManifest
from managers.runtime_health_manager import RuntimeHealthManager


class RuntimeDescriptor:
    """
    Canonical runtime descriptor.

    Single immutable object describing
    the runtime at execution time.
    """

    def build(self):

        manifest = RuntimeManifest().build()

        health = RuntimeHealthManager().execute()

        return {

            "manifest": manifest,

            "health": {

                "healthy": health["healthy"],

                "validated": health["validated"],

                "summary": health["summary"],

            }

        }
