"""
PADI Semantic Doctrine
Version: 0.7.0

Generic compiler doctrine.

Responsibilities
----------------
• Validate compiler command structure.
• Enforce deterministic compiler contracts.
• Reject malformed commands before factory execution.

Non-responsibilities
--------------------
• Domain semantics
• Ontology logic
• Namespace resolution
• RDF construction
• SHACL validation
• SKOS reasoning
• Inference

The doctrine validates compiler contracts only.
"""


class DoctrineEnforcer:
    """
    Generic structural validation layer.

    Accepts only canonical compiler commands.
    """

    VERSION = "0.7.0"

    def validate(self, commands):
        """
        Validate an iterable of compiler commands.
        """

        if not isinstance(commands, list):
            raise TypeError(
                "DoctrineEnforcer: commands must be a list."
            )

        validated = []

        for index, command in enumerate(commands):
            self._validate_command(command, index)
            validated.append(command)

        return validated

    def _validate_command(self, command, index):
        """
        Validate one compiler command.
        """

        if not isinstance(command, dict):
            raise TypeError(
                f"Doctrine error [{index}]: command must be a dictionary."
            )

        if "factory" not in command:
            raise ValueError(
                f"Doctrine error [{index}]: missing 'factory'."
            )

        if "arguments" not in command:
            raise ValueError(
                f"Doctrine error [{index}]: missing 'arguments'."
            )

        if not isinstance(command["arguments"], dict):
            raise TypeError(
                f"Doctrine error [{index}]: 'arguments' must be a dictionary."
            )

        return True
