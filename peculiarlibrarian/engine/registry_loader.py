"""
Operator Registry Loader
Version: 1.0.0

Loads the machine-readable operator registry.
"""

from pathlib import Path
import yaml


class OperatorRegistryLoader:

    VERSION = "1.0.0"

    def __init__(self):
        self.path = Path("peculiarlibrarian/registry/operators.yaml")

    def load(self):
        return yaml.safe_load(self.path.read_text())

    def operators(self):
        return self.load()["operators"]

    def defaults(self):
        return self.load()["defaults"]

    def operator(self, name):
        return self.operators()[name]
