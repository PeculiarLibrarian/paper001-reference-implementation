from kernel.semantic_model import SemanticModel


class DummyManager:
    pass


class SemanticRegistry:

    def __init__(self):

        self.ingestion = DummyManager()
        self.canonicalization = DummyManager()

        # ✔ FIX: inject fully compatible semantic model
        self.semantic_model = SemanticModel(
            ontology=DummyManager(),
            taxonomy=DummyManager(),
            shapes=DummyManager(),
            queries=DummyManager(),
            reasoning=DummyManager()
        )
