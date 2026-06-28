from kernel.collection import Collection
from kernel.collection_registry import CollectionRegistry


class CollectionLoader:

    @staticmethod
    def load():

        collections = []

        for name, root in CollectionRegistry.collections().items():

            collections.append(

                Collection(

                    name=name,

                    root=root,

                    ontology=root / "ontology",

                    taxonomy=root / "taxonomy",

                    queries=root / "queries",

                    shapes=root / "shapes",

                    instances=root / "instances",

                )

            )

        return collections

