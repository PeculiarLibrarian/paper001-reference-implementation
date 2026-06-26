from typing import Dict, Any


class SemanticCoreManager:

    def load(self):
        pass

    def execute(self, context: Dict[str, Any] = None):

        graph = None
        instances = None

        if isinstance(context, dict):
            graph = context.get("graph")
            instances = context.get("instances")

        # 🔥 FIX: NO direct manager calls allowed
        if graph is None or instances is None:
            raise ValueError(
                "SemanticCoreManager requires 'graph' and 'instances' in context"
            )

        core = {
            "core_index": len(list(graph)) + len(instances.get("opportunities", []))
        }

        return {
            "core": core
        }
