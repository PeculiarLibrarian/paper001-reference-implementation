from contracts.artifact_registry import ArtifactRegistry

from kernel.semantic_artifact_registry import (
    SemanticArtifactRegistry,
)


class ArtifactCatalog:

    @staticmethod
    def registry():

        return {

            "infrastructure":
                ArtifactRegistry.artifacts(),

            "semantic":
                SemanticArtifactRegistry.registry(),

        }

