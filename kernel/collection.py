from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Collection:

    name: str

    root: Path

    ontology: Path

    taxonomy: Path

    queries: Path

    shapes: Path

    instances: Path

    def identity(self):

        return {

            "collection": self.name,

            "root": str(self.root),

            "ontology": str(self.ontology),

            "taxonomy": str(self.taxonomy),

            "queries": str(self.queries),

            "shapes": str(self.shapes),

            "instances": str(self.instances),

        }

