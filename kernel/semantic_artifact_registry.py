from pathlib import Path


class SemanticArtifactRegistry:

    ROOT = Path("schemas")

    @classmethod
    def registry(cls):

        return {

            "ontology": cls.ROOT / "ontology",

            "taxonomy": cls.ROOT / "taxonomy",

            "queries": cls.ROOT / "queries",

            "shapes": cls.ROOT / "shapes",

        }

