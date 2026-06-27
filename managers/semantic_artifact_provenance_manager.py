from hashlib import sha256
from pathlib import Path

from kernel.semantic_artifact_loader import (
    SemanticArtifactLoader,
)


class SemanticArtifactProvenanceManager:

    @staticmethod
    def handshake():

        return {

            "manager": "SemanticArtifactProvenanceManager",

            "version": "1.0",

            "contract": "manager_contract",

            "capabilities": [

                "discover",

                "fingerprint",

                "verify",

                "execute",

            ],

        }

    def execute(self, context=None):

        provenance = []

        for artifact in SemanticArtifactLoader.load():

            path = Path(artifact["path"])

            exists = path.exists()

            digest = (

                sha256(path.read_bytes()).hexdigest()

                if exists

                else None

            )

            provenance.append(

                {

                    "artifact_id": artifact["name"],

                    "display_name": artifact["name"],

                    "artifact_kind": "semantic_artifact",

                    "semantic_role": artifact["artifact_type"],

                    "format": path.suffix.lstrip("."),

                    "path": str(path),

                    "hash": digest,

                    "version": "1.0",

                    "verified": exists,

                }

            )

        return {

            "semantic_artifact_provenance": provenance

        }

