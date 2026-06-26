from managers.schema_manager import SchemaManager
from contracts.data_contract import QueryBundle
from rdflib import Graph


class QueryManager(SchemaManager):

    def discover(self):
        self.assets = [
            "schemas/queries/core/competency_coverage.sparql",
            "schemas/queries/core/competency_inventory.sparql",
            "schemas/queries/core/competency_taxonomy_mapping.sparql",
            "schemas/queries/core/opportunity_matching.sparql"
        ]

    def load(self):
        """
        Load SPARQL queries into a catalog.
        """
        self.catalog = {}

        for path in self.assets:
            try:
                with open(path, "r") as f:
                    query_text = f.read()
                    name = path.split("/")[-1].replace(".sparql", "")
                    self.catalog[name] = query_text
            except Exception:
                continue

        return self.catalog

    def parse(self):
        """
        Build executable registry.
        """
        self.registry = {
            name: {
                "file": name + ".sparql",
                "query": query
            }
            for name, query in self.catalog.items()
        }
        return self.registry

    def execute(self, graph: Graph, query_name: str):
        """
        Execute SPARQL query against ontology graph.
        """
        if query_name not in self.catalog:
            raise ValueError(f"Unknown query: {query_name}")

        return graph.query(self.catalog[query_name])

    def bind(self, context: dict) -> dict:
        context["queries"] = QueryBundle(
            catalog=self.catalog,
            registry=self.registry,
            queries=len(self.catalog)
        )
        return context

    def validate(self, context: dict) -> bool:
        return isinstance(self.catalog, dict)

    def expose(self):
        return {
            "catalog": self.catalog,
            "registry": self.registry,
            "queries": len(self.catalog)
        }
