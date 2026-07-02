"""
PADI Semantic Factory
Version: 0.7.0

The Semantic Factory is the only component allowed to emit RDF.

Responsibilities
----------------
• Receive canonical compiler commands.
• Materialize RDF triples.
• Inject alignment relations.
• Invoke SHACL validation.
• Return semantic entities.

Non-responsibilities
--------------------
• Dataset parsing
• JSON-LD loading
• Predicate canonicalization
• Ontology resolution
• Reasoning
• SPARQL
"""

from abc import ABC, abstractmethod

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import RDF, XSD

from peculiarlibrary.ontology.ontology_registry import OntologyRegistry


class AlignmentAutoInjector:

    def __init__(self):
        self.registry = OntologyRegistry()

    def reports_for(self, graph, statement, organization):
        graph.add(
            (
                statement,
                self.registry.resolve("reportsFor"),
                organization,
            )
        )

    def governs(self, graph, body, organization):
        graph.add(
            (
                body,
                self.registry.resolve("governs"),
                organization,
            )
        )

    def role_within(self, graph, role, organization):
        graph.add(
            (
                role,
                self.registry.resolve("isRoleWithin"),
                organization,
            )
        )


class BaseFactory(ABC):

    def __init__(self, graph, validator=None):

        self.graph = graph
        self.validator = validator
        self.registry = OntologyRegistry()
        self.align = AlignmentAutoInjector()

    def emit(self, s, p, o):

        self.graph.add((s, p, o))

    def validate(self):

        if self.validator:
            self.validator.validate(self.graph)

    @abstractmethod
    def create(self, **kwargs):
        pass


class OrganizationFactory(BaseFactory):

    def create(self, **kwargs):

        subject = URIRef(kwargs["subject"])

        self.emit(
            subject,
            RDF.type,
            self.registry.resolve("Organization"),
        )

        self.validate()

        return subject


class FinancialStatementFactory(BaseFactory):

    def create(self, **kwargs):

        subject = URIRef(kwargs["subject"])

        self.emit(
            subject,
            kwargs["predicate"],
            Literal(kwargs["object"]),
        )

        self.validate()

        return subject


class GovernanceBodyFactory(BaseFactory):

    def create(self, **kwargs):

        subject = URIRef(kwargs["subject"])

        self.emit(
            subject,
            kwargs["predicate"],
            Literal(kwargs["object"]),
        )

        self.validate()

        return subject


class FactoryRegistry:
    """
    Generic semantic dispatch layer.
    """

    def __init__(self, graph, validator=None):

        self.factories = {
            "org": OrganizationFactory(graph, validator),
            "fin": FinancialStatementFactory(graph, validator),
            "gov": GovernanceBodyFactory(graph, validator),
        }

    def execute(self, command):

        factory = command["factory"]

        if factory not in self.factories:
            raise ValueError(
                f"Unknown factory '{factory}'"
            )

        return self.factories[factory].create(
            **command["arguments"]
        )
