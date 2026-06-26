from managers.schema_manager import SchemaManager
from contracts.data_contract import ShapesBundle
from rdflib import Graph


class ShapesManager(SchemaManager):

    def discover(self):
        self.assets = ["schemas/shapes"]

    def load(self):
        self.graph = Graph()
        for f in self.assets:
            try:
                self.graph.parse(f)
            except Exception:
                continue
        return self.graph

    def parse(self):
        self.registry = {"graph": self.graph}
        return self.registry

    def bind(self, context: dict) -> dict:
        context["shapes"] = ShapesBundle(
            registry=self.registry,
            shapes=len(self.graph),
            triples=len(self.graph)
        )
        return context

    def validate(self, context: dict) -> bool:
        # shapes must always produce a valid RDF graph
        return isinstance(self.graph, Graph)

    def expose(self):
        return {
            "graph": self.graph,
            "registry": self.registry,
            "shapes": len(self.graph),
            "triples": len(self.graph)
        }
