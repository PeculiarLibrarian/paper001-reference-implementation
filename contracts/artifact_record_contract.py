from typing import Dict, Any


class ArtifactRecordContract:

    REQUIRED_FIELDS = {
        "artifact_id",
        "display_name",
        "artifact_kind",
        "runtime_role",
        "path",
        "exists",
        "extension",
        "hash",
        "version",
        "implements_contract",
        "verified",
        "contract_valid",
        "missing_fields",
    }

    @staticmethod
    def validate(record: Dict[str, Any]):

        missing = [
            f for f in ArtifactRecordContract.REQUIRED_FIELDS
            if f not in record
        ]

        return {
            "valid": len(missing) == 0,
            "missing": missing,
        }
