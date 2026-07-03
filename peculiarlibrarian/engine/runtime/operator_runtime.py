"""
Operator Runtime
Version: 1.4.0

Stateful semantic execution bus with full pipeline awareness.
"""

from peculiarlibrarian.engine.registry_loader import OperatorRegistryLoader
from peculiarlibrarian.engine.registry_validator import OperatorRegistryValidator


class OperatorRuntime:

    VERSION = "1.4.0"

    def __init__(self):

        OperatorRegistryValidator().validate()

        self.loader = OperatorRegistryLoader()
        self.registry = self.loader.load()

        self.context = {}

    def resolve(self, name: str):

        op_meta = self.registry["operators"][name]

        module_path = f"peculiarlibrarian.engine.operators.{name}_operator"
        class_name = op_meta["class"]

        try:
            module = __import__(module_path, fromlist=[class_name])
            return getattr(module, class_name)()

        except Exception as e:
            raise RuntimeError(
                f"Operator resolution failed for '{name}' | "
                f"module={module_path} class={class_name} | "
                f"cause={repr(e)}"
            ) from e

    def execute(self, name: str, payload=None):

        payload = payload or {}

        # ---- CONTEXT INJECTION ----
        if name == "reason" and "graph" not in payload:
            payload["graph"] = self.context.get("compile_graph")

        if name == "validate" and "graph" not in payload:
            payload["graph"] = self.context.get("reason_graph")

        # ---- EXECUTION ----
        operator = self.resolve(name)
        result = operator.execute(payload)

        # ---- CONTEXT CAPTURE ----
        if name == "compile":
            self.context["compile_graph"] = result.get("graph")

        if name == "reason":
            self.context["reason_graph"] = result.get("graph")

        self.context[name] = result

        return {
            "operator": name,
            "stage": self.registry["operators"][name]["stage"],
            "result": result,
        }
