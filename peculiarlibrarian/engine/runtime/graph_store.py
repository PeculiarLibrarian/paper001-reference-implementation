"""
Graph Store
Version: 1.0.0

Central RDF graph registry for the PADI runtime.

Responsibilities
----------------
- Store graphs by stage.
- Retrieve graphs by stage.
- Report availability.
- Clear runtime state.

The store is intentionally ignorant of operators,
replay, SPARQL, provenance and execution logic.
"""

from rdflib import Graph


class GraphStore:

    VERSION = "1.0.0"

    def __init__(self):
        self._graphs = {}

    def put(self, stage: str, graph: Graph) -> Graph:
        if not isinstance(graph, Graph):
            raise TypeError(
                f"Expected rdflib.Graph for stage '{stage}', "
                f"got {type(graph).__name__}"
            )

        self._graphs[stage] = graph
        return graph

    def get(self, stage: str):
        return self._graphs.get(stage)

    def has(self, stage: str) -> bool:
        return stage in self._graphs

    def remove(self, stage: str):
        return self._graphs.pop(stage, None)

    def stages(self):
        return list(self._graphs.keys())

    def size(self):
        return len(self._graphs)

    def summary(self):
        report = {}

        for stage, graph in self._graphs.items():
            report[stage] = {
                "triples": len(graph)
            }

        return report

    def clear(self):
        self._graphs.clear()

    def __contains__(self, stage):
        return self.has(stage)

    def __len__(self):
        return len(self._graphs)
