from typing import Any, Dict


class ArtifactRelationshipContract:

    REQUIRED_FIELDS = {

        "source",
        "relationship",
        "target",
        "verified",

    }

    @staticmethod
    def validate(record: Dict[str, Any]):

        missing = [
            field
            for field in ArtifactRelationshipContract.REQUIRED_FIELDS
            if field not in record
        ]

        return {

            "valid": len(missing) == 0,
            "missing": missing,

        }
