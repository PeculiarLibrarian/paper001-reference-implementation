"""
SchemaAuditManager

Audits consistency between ontology schemas and SPARQL query library.
"""

from pathlib import Path
import re
from rdflib import Graph, RDF, RDFS, OWL

PL_NS = "https://peculiarlibrarian.org/ontology/"

class SchemaAuditManager:
    def __init__(self,
                 ontology_dir="schemas/ontology",
                 query_dir="schemas/queries"):
        self.ontology_dir = Path(ontology_dir)
        self.query_dir = Path(query_dir)

    def load_ontology(self):
        graph = Graph()

        for ttl in sorted(self.ontology_dir.glob("*.ttl")):
            graph.parse(ttl)

        return graph

    def defined_terms(self, graph):
        terms = set()

        for s, p, o in graph:
            if str(s).startswith(PL_NS):
                terms.add(str(s))

        return terms

    def referenced_terms(self):
        refs = set()

        pattern = re.compile(r'pl:([A-Za-z0-9_]+)')

        for query in sorted(self.query_dir.rglob("*.sparql")):
            text = query.read_text()

            for match in pattern.findall(text):
                refs.add(PL_NS + match)

        return refs

    def audit(self):
        graph = self.load_ontology()

        defined = self.defined_terms(graph)
        referenced = self.referenced_terms()

        return {
            "defined": sorted(defined),
            "referenced": sorted(referenced),
            "missing": sorted(referenced - defined),
            "unused": sorted(defined - referenced),
        }
