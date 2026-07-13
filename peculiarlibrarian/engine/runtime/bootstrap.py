"""
Runtime Bootstrap
Validates registry integrity BEFORE execution begins.
"""

import importlib


class BootstrapFailure(Exception):
    pass


class RuntimeBootstrap:

    def __init__(self, registry):
        self.registry = registry

    def verify(self):
        self._verify_operators()

    def _verify_operators(self):

        for name, meta in self.registry["operators"].items():

            module_path = meta.get("module")
            class_name = meta.get("class")

            if not module_path or not class_name:
                raise BootstrapFailure(
                    f"Missing module/class for operator: {name}"
                )

            try:
                module = importlib.import_module(module_path)
                getattr(module, class_name)

            except Exception as e:
                raise BootstrapFailure(
                    f"Bootstrap failed for {name}: {str(e)}"
                )
