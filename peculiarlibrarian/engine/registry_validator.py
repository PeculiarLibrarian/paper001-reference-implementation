"""
Operator Registry Validator
Version: 1.0.0

Validates the Operator Registry contract.
"""

from peculiarlibrarian.engine.registry_loader import OperatorRegistryLoader


class OperatorRegistryValidator:

    VERSION = "1.0.0"

    REQUIRED_FIELDS = (
        "class",
        "stage",
        "description",
    )

    def __init__(self):
        self.loader = OperatorRegistryLoader()

    def validate(self):

        registry = self.loader.load()

        if registry["registry"]["status"] != "locked":
            raise ValueError("Operator registry is not locked.")

        operators = registry["operators"]

        for name, definition in operators.items():

            for field in self.REQUIRED_FIELDS:

                if field not in definition:
                    raise ValueError(
                        f"{name}: missing '{field}'"
                    )

        return True
