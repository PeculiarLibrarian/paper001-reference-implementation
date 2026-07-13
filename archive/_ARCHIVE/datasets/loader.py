"""
Dataset Loader
Version: 1.1.0

Responsibilities
----------------
• Deserialize canonical JSON datasets.
• Produce canonical dataset objects.

Non-responsibilities
--------------------
• RDF construction
• Namespace canonicalization
• Ontology alignment
• SHACL validation
• SKOS expansion
• Inference
• Materialization
"""

import json


class DatasetLoader:

    VERSION = "1.1.0"

    def __init__(self, path):
        self.path = path

    def load(self):
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)
