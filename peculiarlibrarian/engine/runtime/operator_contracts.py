class OperatorContract:
    """
    Defines deterministic execution contracts for operators.
    """

    CONTRACTS = {
        "compile": {
            "required": ["dataset"],
            "optional": [],
        },
        "reason": {
            "required": ["graph"],
            "optional": [],
        },
        "validate": {
            "required": ["graph"],
            "optional": [],
        },
        "audit": {
            "required": ["graph"],
            "optional": [],
        },
        "sparql": {
            "required": ["graph", "query"],
            "optional": [],
        },
    }

    @classmethod
    def validate(cls, name, payload):
        if name not in cls.CONTRACTS:
            raise ValueError(f"Unknown operator contract: {name}")

        contract = cls.CONTRACTS[name]

        for key in contract["required"]:
            if key not in payload:
                raise ValueError(
                    f"[{name}] Missing required field: {key}"
                )

        return True
