from pathlib import Path

from contracts.artifact_registry import ArtifactRegistry


class ArtifactDiscoveryManager:

    @staticmethod
    def handshake():

        return {

            "manager": "ArtifactDiscoveryManager",

            "version": "1.0",

            "contract": "manager_contract",

            "capabilities": [

                "discover",

                "enumerate",

                "execute",

            ],

        }

    def execute(self, context=None):

        artifacts = []

        registry = ArtifactRegistry.artifacts()

        for artifact_type, root in registry.items():

            if not root.exists():

                continue

            for file in sorted(root.glob("*.py")):

                artifacts.append(

                    {
                        "artifact_id": file.stem,

                        "display_name": file.stem,

                        "artifact_kind": "python_module",

                        "runtime_role": artifact_type,

                        "path": str(file),

                    }

                )

        return {

            "artifacts": artifacts

        }
