from abc import ABC, abstractmethod
from typing import Dict, Any


class OntologyManagerBase(ABC):

    def __init__(self):
        self.state: Dict[str, Any] = {}

    def load(self) -> None:
        pass

    def validate(self, payload: Dict[str, Any]) -> bool:
        return isinstance(payload, dict)

    def expose(self) -> Dict[str, Any]:
        return self.state

    @abstractmethod
    def execute(self, context: Dict[str, Any] = None) -> Dict[str, Any]:
        pass

    def _load_graph(self):
        from rdflib import Graph

        g = Graph()
        g.parse(
            "schemas/ontology/peculiarlibrarian.owl",
            format="turtle"
        )
        return g
