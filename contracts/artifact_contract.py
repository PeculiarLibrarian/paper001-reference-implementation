class ArtifactContract:

    REQUIRED_FIELDS = [

        "artifact",
        "artifact_type",
        "path",
        "hash",
        "version",
        "contract",
        "verified",

    ]

    @classmethod
    def validate(cls, artifact):

        missing = [

            field
            for field in cls.REQUIRED_FIELDS
            if field not in artifact

        ]

        return {

            "valid": len(missing) == 0,

            "missing": missing,

        }
