"""
PADI RDF Materializer
Version: 1.0.2

Transforms CanonicalFact semantic objects into RDF.

This is the ONLY component responsible for emitting RDF.
"""

from rdflib import Graph, Literal, Namespace, RDF, URIRef
from rdflib.namespace import XSD

from padi.kernel.identity_resolver import IdentityResolver


class RDFMaterializer:

    VERSION = "1.0.2"

    def __init__(self):

        self.identity = IdentityResolver()

        self.graph = Graph()

        self.CORE = Namespace("http://padi.s.m.gitandu.bs/core#")

        self.graph.bind("core", self.CORE)

    # -----------------------------------------------------
    # PUBLIC API
    # -----------------------------------------------------

    def materialize(self, facts):

        for fact in facts:
            self._materialize_fact(fact)

        return self.graph

    # -----------------------------------------------------
    # INTERNAL MATERIALIZATION
    # -----------------------------------------------------

    def _materialize_fact(self, fact):

        fact_uri = URIRef(
            self.identity.fact(
                fact.entity,
                fact.metric,
                fact.period,
                fact.value,
            )
        )

        entity_uri = URIRef(self.identity.entity(fact.entity))
        metric_uri = URIRef(self.identity.metric(fact.metric))

        # -------------------------
        # CanonicalFact node
        # -------------------------

        self.graph.add((fact_uri, RDF.type, self.CORE.CanonicalFact))

        self.graph.add((fact_uri, self.CORE.aboutEntity, entity_uri))

        self.graph.add((fact_uri, self.CORE.hasMetric, metric_uri))

        self.graph.add(
            (
                fact_uri,
                self.CORE.factValue,
                self._to_decimal_literal(fact.value),
            )
        )

        self.graph.add(
            (
                fact_uri,
                self.CORE.reportingPeriod,
                Literal(fact.period),
            )
        )

        self.graph.add(
            (
                fact_uri,
                self.CORE.measurementUnit,
                Literal(fact.unit),
            )
        )

        self.graph.add(
            (
                fact_uri,
                self.CORE.confidence,
                self._to_decimal_literal(fact.confidence),
            )
        )

        # -------------------------
        # SourceRecord (OPTIONAL SAFE)
        # -------------------------

        if fact.source is not None:

            source_uri = URIRef(
                self.identity.source(
                    fact.source.document.filename,
                    fact.source.page,
                )
            )

            self.graph.add((fact_uri, self.CORE.hasSource, source_uri))

            self.graph.add((source_uri, RDF.type, self.CORE.SourceRecord))

            self.graph.add(
                (
                    source_uri,
                    self.CORE.sourceDocument,
                    Literal(fact.source.document.filename),
                )
            )

            self.graph.add(
                (
                    source_uri,
                    self.CORE.sourcePage,
                    Literal(fact.source.page, datatype=XSD.integer),
                )
            )

            self.graph.add(
                (
                    source_uri,
                    self.CORE.sourceSection,
                    Literal(fact.source.section),
                )
            )

            self.graph.add(
                (
                    source_uri,
                    self.CORE.sourceContext,
                    Literal(fact.source.context),
                )
            )

    # -----------------------------------------------------
    # SAFE NUMERIC NORMALIZATION (FIXED)
    # -----------------------------------------------------

    def _to_decimal_literal(self, value):

        from decimal import Decimal, InvalidOperation

        try:
            if value is None:
                return Literal("0", datatype=XSD.decimal)

            if isinstance(value, (int, float)):
                return Literal(str(value), datatype=XSD.decimal)

            if isinstance(value, str):
                cleaned = value.strip()
                return Literal(str(Decimal(cleaned)), datatype=XSD.decimal)

            return Literal(str(Decimal(str(value))), datatype=XSD.decimal)

        except (InvalidOperation, ValueError):
            return Literal("0", datatype=XSD.decimal)
