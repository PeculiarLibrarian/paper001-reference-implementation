"""
PADI RDF Materializer

Purpose
-------
Materialize canonical semantic objects into RDF.

Input
-----
CanonicalFact tuple

Output
------
RDFLib Graph
"""

from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, XSD


PADI = Namespace(
    "http://padi.s.m.gitandu.bs/core#"
)


class RDFMaterializer:

    VERSION = "2.0.0"

    def materialize(self, facts):

        graph = Graph()

        graph.bind(
            "padi",
            PADI
        )

        for i, fact in enumerate(
            facts,
            start=1
        ):

            fact_uri = URIRef(
                PADI[f"Fact_{i:05d}"]
            )

            entity_uri = URIRef(
                PADI[
                    self._entity(
                        fact.entity.name
                    )
                ]
            )

            source_uri = URIRef(
                PADI[f"Source_{i:05d}"]
            )

            graph.add(
                (
                    fact_uri,
                    RDF.type,
                    PADI.CanonicalFact
                )
            )

            graph.add(
                (
                    entity_uri,
                    RDF.type,
                    PADI.Entity
                )
            )

            graph.add(
                (
                    source_uri,
                    RDF.type,
                    PADI.SourceRecord
                )
            )

            graph.add(
                (
                    fact_uri,
                    PADI.aboutEntity,
                    entity_uri
                )
            )

            graph.add(
                (
                    fact_uri,
                    PADI.metric,
                    Literal(
                        fact.metric.name
                    )
                )
            )

            graph.add(
                (
                    fact_uri,
                    PADI.value,
                    self._literal(
                        fact.value
                    )
                )
            )

            if fact.unit:
                graph.add(
                    (
                        fact_uri,
                        PADI.unit,
                        Literal(
                            fact.unit.name
                        )
                    )
                )

            if fact.period:
                graph.add(
                    (
                        fact_uri,
                        PADI.period,
                        Literal(
                            fact.period.label
                        )
                    )
                )

            if fact.confidence is not None:
                graph.add(
                    (
                        fact_uri,
                        PADI.confidence,
                        Literal(
                            fact.confidence,
                            datatype=XSD.decimal
                        )
                    )
                )

            graph.add(
                (
                    fact_uri,
                    PADI.hasSource,
                    source_uri
                )
            )

            source = fact.source

            if source.document:
                graph.add(
                    (
                        source_uri,
                        PADI.document,
                        Literal(
                            source.document
                        )
                    )
                )

            if source.page:
                graph.add(
                    (
                        source_uri,
                        PADI.page,
                        Literal(
                            source.page,
                            datatype=XSD.integer
                        )
                    )
                )

            if source.section:
                graph.add(
                    (
                        source_uri,
                        PADI.section,
                        Literal(
                            source.section
                        )
                    )
                )

            if source.context:
                graph.add(
                    (
                        source_uri,
                        PADI.context,
                        Literal(
                            source.context
                        )
                    )
                )

        return graph


    @staticmethod
    def _entity(name):

        return (
            name
            .replace(" ", "")
            .replace(",", "")
            .replace("(", "")
            .replace(")", "")
        )


    @staticmethod
    def _literal(value):

        if isinstance(value, int):
            return Literal(
                value,
                datatype=XSD.integer
            )

        if isinstance(value, float):
            return Literal(
                value,
                datatype=XSD.double
            )

        return Literal(value)
