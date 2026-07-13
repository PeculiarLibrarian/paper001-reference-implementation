"""
PADI Semantic Mapping Runtime

Loads controlled semantic interpretations
without modifying canonical facts.
"""

from pathlib import Path
from rdflib import Graph


MAPPING_FILE = Path(
    "peculiarlibrary/SKOS/semantic_mapping.ttl"
)


class SemanticMappingRuntime:

    def __init__(self):
        self.graph = Graph()

    def load(self):

        if not MAPPING_FILE.exists():
            raise RuntimeError(
                "Semantic mapping vocabulary missing."
            )

        self.graph.parse(
            MAPPING_FILE,
            format="turtle"
        )

        return self.graph


def load_semantic_mapping():

    return SemanticMappingRuntime().load()
