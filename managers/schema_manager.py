class SchemaManager:
    """
    Base contract for all schema managers in the Peculiar Librarian system.

    A SchemaManager is NOT a data processor.
    It is a semantic custodian of a single schema collection.

    Responsibilities:
        - Discover schema assets
        - Load schema artifacts
        - Parse schema into usable structure
        - Bind schema output into runtime context
        - Validate schema correctness within system context
        - Expose canonical representation

    This class enforces lifecycle discipline across all managers.
    """

    # ----------------------------
    # LIFECYCLE CONTRACT
    # ----------------------------

    def discover(self):
        """
        Locate schema assets (files, registry entries, or URIs).
        Must populate: self.assets
        """
        raise NotImplementedError("discover() must be implemented by SchemaManager subclass")

    def load(self):
        """
        Load raw schema content into internal representation.
        Must populate manager-specific structures.
        """
        raise NotImplementedError("load() must be implemented by SchemaManager subclass")

    def parse(self):
        """
        Transform loaded schema into structured, queryable form.
        """
        raise NotImplementedError("parse() must be implemented by SchemaManager subclass")

    def bind(self, context: dict) -> dict:
        """
        Inject schema output into runtime context.
        This is the ONLY way data leaves a manager.
        """
        raise NotImplementedError("bind() must be implemented by SchemaManager subclass")

    def validate(self, context: dict) -> bool:
        """
        Validate schema consistency against runtime context.

        Must be deterministic and side-effect free.
        """
        raise NotImplementedError("validate() must be implemented by SchemaManager subclass")

    def expose(self):
        """
        Return canonical external representation of schema state.
        Used for inspection, debugging, and orchestration reporting.
        """
        raise NotImplementedError("expose() must be implemented by SchemaManager subclass")

    # ----------------------------
    # OPTIONAL SYSTEM HOOKS
    # ----------------------------

    def contract(self):
        """
        Optional: declare expected schema behavior contract.

        Future use:
            - schema introspection
            - cross-manager validation
            - ontology consistency checks
        """
        return {}
