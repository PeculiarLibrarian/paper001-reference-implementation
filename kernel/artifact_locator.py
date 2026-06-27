from pathlib import Path

from contracts.artifact_registry import ArtifactRegistry
from kernel.artifact_descriptor import ArtifactDescriptor


class ArtifactLocator:

    @staticmethod
    def locate():

        discovered = []

        for artifact_type, root in ArtifactRegistry.artifacts().items():

            if not root.exists():
                continue

            for file in sorted(root.iterdir()):

                if not file.is_file():
                    continue

                if file.name.startswith("__"):
                    continue

                discovered.append(

                    ArtifactDescriptor(

                        artifact_type=artifact_type,

                        name=file.stem,

                        path=file,

                    )

                )

        return discovered
