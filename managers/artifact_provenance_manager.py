from hashlib import sha256
from pathlib import Path

from contracts.artifact_record_contract import ArtifactRecordContract

from kernel.artifact_descriptor import ArtifactDescriptor
from kernel.artifact_record import ArtifactRecord


class ArtifactProvenanceManager:

    @staticmethod
    def handshake():
        return {
            "manager": "ArtifactProvenanceManager",
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

        if context is None or "artifacts" not in context:
            raise RuntimeError(
                "ArtifactProvenanceManager requires discovered artifacts."
            )

        artifacts = []

        for discovered in context["artifacts"]:

            path = Path(discovered["path"])

            exists = path.exists()

            digest = (
                sha256(path.read_bytes()).hexdigest()
                if exists
                else None
            )

            descriptor = ArtifactDescriptor(
                artifact_type=discovered["runtime_role"],
                name=discovered["display_name"],
                path=path,
            )

            record = ArtifactRecord(
                descriptor=descriptor,
                hash=digest,
                version="1.0",
                implements_contract="manager_contract",
                verified=exists,
                contract_valid=False,
                missing_fields=[],
                layer=discovered.get("layer", "unknown"),
                produces=discovered.get("produces", []),
            )

            record_dict = record.provenance()

            validation = ArtifactRecordContract.validate(record_dict)

            record_dict["contract_valid"] = validation["valid"]
            record_dict["missing_fields"] = validation["missing"]

            artifacts.append(record_dict)

        return {

            "artifact_provenance": artifacts

        }