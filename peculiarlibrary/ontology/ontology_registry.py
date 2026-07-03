"""
Ontology Registry (RDF/SKOS Bootstrap Resolver)
Version: 2.0.0

Replaces manual predicate mapping with ontology-driven resolution.

Resolution order:
1. Core ontology TTL
2. Domain ontologies
3. SKOS prefLabel fallback
4. URI construction fallback
"""

from rdflib import Graph, URIRef, Namespace


class OntologyRegistry:

    VERSION = "2.0.0"

    def __init__(self):
        self.graph = Graph()

        # Load all ontology sources deterministically
        self._load_ontologies()

        self.PADI = Namespace("http://padi.s.m.gitandu.bs/ontology#")

    # -----------------------------
    # Bootstrap Layer
    # -----------------------------
    def _load_ontologies(self):

        ontology_files = [
            "peculiarlibrary/ontology/core_library.ttl",
            "peculiarlibrary/domains/finance/ontology.ttl",
            "peculiarlibrary/domains/governance/ontology.ttl",
            "peculiarlibrary/domains/organization/ontology.ttl",
            "peculiarlibrary/domains/telecommunications/ontology.ttl",
        ]

        for file in ontology_files:
            try:
                self.graph.parse(file, format="turtle")
            except Exception:
                # Do not hard-fail bootstrap; partial ontology still usable
                continue

    # -----------------------------
    # Resolution Layer
    # -----------------------------
    def resolve(self, term: str):

        if term is None:
            return None

        # 1. Direct match in ontology graph
        uri = self.PADI[term]
        if (uri, None, None) in self.graph or (None, None, uri) in self.graph:
            return uri

        # 2. Scan for SKOS labels
        for s, p, o in self.graph:
            if str(o).lower() == term.lower():
                return s

        # 3. Fallback deterministic URI construction
        return URIRef(str(self.PADI) + term)

    # -----------------------------
    # Debug helpers
    # -----------------------------
    def all_terms(self):
        return list(self.graph)
