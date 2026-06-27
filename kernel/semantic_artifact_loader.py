from pathlib import Path

from kernel.semantic_artifact_registry import (
    SemanticArtifactRegistry,
)


class SemanticArtifactLoader:

    @staticmethod
    def load():

        artifacts = []

        registry = SemanticArtifactRegistry.registry()

        for artifact_type, root in registry.items():

            if not root.exists():

                continue

            for path in sorted(root.rglob("*")):

                if not path.is_file():

                    continue

                artifacts.append(

                    {

                        "artifact_type": artifact_type,

                        "name": path.stem,

                        "path": str(path),

                    }

                )

        return artifacts

