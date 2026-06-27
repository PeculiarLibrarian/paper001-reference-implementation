from rdflib import Graph

from contracts.data_contract import QueryBundle

from kernel.query_loader import QueryLoader
from kernel.query_registry import QueryRegistry


class QueryManager:

    @staticmethod
    def handshake():

        return {

            "manager": "QueryManager",

            "version": "2.0",

            "contract": "manager_contract",

            "capabilities": [

                "load_query",

                "execute_query",

            ],

        }

    def discover(self):

        self.assets = {

            "pipeline_stages": QueryRegistry.core("pipeline_stages"),

            "pipelines": QueryRegistry.core("pipelines"),

            "stages": QueryRegistry.core("stages"),

            "artifacts": QueryRegistry.core("artifacts"),

        }

        return self.assets

    def load(self):

        self.catalog = {

            name: QueryLoader.load(name)

            for name in self.assets

        }

        return self.catalog

    def execute(self, graph: Graph, query_name: str):

        if query_name not in self.catalog:

            raise ValueError(f"Unknown query: {query_name}")

        return graph.query(self.catalog[query_name])

    def bind(self, context):

        context["queries"] = QueryBundle(

            catalog=self.catalog,

            registry=self.assets,

            queries=len(self.catalog),

        )

        return context

    def validate(self, context):

        return isinstance(self.catalog, dict)

    def expose(self):

        return {

            "catalog": self.catalog,

            "registry": self.assets,

            "queries": len(self.catalog),

        }

