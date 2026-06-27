from kernel.runtime_introspector import RuntimeIntrospector


class RuntimeManifest:
    """
    Canonical runtime descriptor.

    Generated from the runtime itself.
    """

    NAME = "PeculiarLibrarian"

    VERSION = "1.0"

    def build(self):

        runtime = RuntimeIntrospector().inspect()

        return {

            "runtime": self.NAME,

            "version": self.VERSION,

            "ready": True,

            "manager_count": runtime["manager_count"],

            "dependency_count": runtime["dependency_count"],

            "layers": runtime["layers"],

            "managers": runtime["managers"],

            "outputs": runtime["outputs"],

        }
