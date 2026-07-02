"""
Dataset loader.

Responsibilities
----------------
• Deserialize JSON-LD.
• Produce an RDF Graph.

Non-responsibilities
--------------------
• Namespace canonicalization
• Ontology alignment
• SHACL validation
• SKOS expansion
• Inference
• Materialization

Those belong to the Semantic Compiler.
"""

from rdflib import Graph


class SafaricomDatasetLoader:

    def __init__(self, path):
        self.path = path

    def load(self):
        g = Graph()
        g.parse(self.path, format="json-ld")

        # Pure deserialization only.
        # No mutation, normalization, inference, or validation.
        return g
