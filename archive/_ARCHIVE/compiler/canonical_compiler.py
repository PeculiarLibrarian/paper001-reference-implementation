from rdflib import Graph, Literal, URIRef
from rdflib.namespace import XSD

from peculiarlibrary.factory.core_factory import FactoryRegistry
from peculiarlibrary.ontology.ontology_registry import OntologyRegistry
from padi.kernel.identity_resolver import IdentityResolver


class CanonicalCompiler:
    """
    SINGLE AUTHORITY RDF COMPILER (PADI CONTROL PLANE)
    """

    def __init__(self):
        self.graph = Graph()
        self.ontology = OntologyRegistry()
        self.identity = IdentityResolver()

    def compile(self, facts):
        registry = FactoryRegistry(self.graph)

        for fact in facts:
            command = {
                "factory": "fin",
                "arguments": {
                    "subject": self.identity.entity(fact.entity.name),
                    "predicate": self._resolve(fact.metric.name),
                    "object": fact.value
                }
            }

            registry.execute(self._normalize(command))

        return self.graph

    def _resolve(self, term):
        return URIRef(str(self.ontology.resolve(term)))

    def _datatype(self, value):
        if isinstance(value, bool):
            return XSD.boolean
        if isinstance(value, int):
            return XSD.integer
        if isinstance(value, float):
            return XSD.decimal
        if isinstance(value, str) and len(value) == 10:
            return XSD.date
        return None

    def _normalize(self, command):
        obj = command["arguments"]["object"]
        dtype = self._datatype(obj)

        if dtype:
            command["arguments"]["object"] = Literal(obj, datatype=dtype)

        command["arguments"]["predicate"] = self._resolve(
            command["arguments"]["predicate"]
        )

        return command
