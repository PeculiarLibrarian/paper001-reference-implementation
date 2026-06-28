from pathlib import Path


class CollectionRegistry:

    ROOT = Path("schemas")

    @classmethod
    def collections(cls):

        collections = {}

        for child in sorted(cls.ROOT.iterdir()):

            if not child.is_dir():

                continue

            if child.name in {

                "ontology",

                "taxonomy",

                "queries",

                "shapes",

            }:

                continue

            collections[child.name] = child

        return collections

