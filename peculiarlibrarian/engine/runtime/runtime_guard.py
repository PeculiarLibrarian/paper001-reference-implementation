"""
Runtime Guard (pure, dependency-free)
"""

class RuntimeGuard:

    def __init__(self, runtime):
        self.runtime = runtime

    def verify(self):

        if not hasattr(self.runtime, "registry"):
            raise RuntimeError("Registry not loaded")

        if not isinstance(self.runtime.context, dict):
            raise RuntimeError("Invalid runtime context")

        if self.runtime.registry is None:
            raise RuntimeError("Null registry")

        return True
