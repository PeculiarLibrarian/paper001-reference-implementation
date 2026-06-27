class ManagerManifest:

    @staticmethod
    def manifest(profile: str = "default"):

        base = {

            "OntologyManager": {
                "layer": "schema",
                "produces": ["graph"],
                "active": True
            },

            "InstanceManager": {
                "layer": "semantic",
                "produces": ["instances"],
                "active": True
            },

            "SemanticCoreManager": {
                "layer": "semantic",
                "produces": ["core"],
                "active": True
            },

            "ReasoningManager": {
                "layer": "decision",
                "produces": ["facts"],
                "active": True
            },

            "ProvenanceManager": {
                "layer": "semantic",
                "produces": ["provenance"],
                "active": True
            },

            "OpportunityEngine": {
                "layer": "decision",
                "produces": ["ranked_opportunities"],
                "active": True
            },

            "ExplanationEngine": {
                "layer": "decision",
                "produces": ["explanations"],
                "active": True
            },

            "TaxonomyManager": {
                "layer": "schema",
                "produces": ["taxonomy", "concepts"],
                "active": True
            },

            "GraphTraversalManager": {
                "layer": "infrastructure",
                "produces": ["graph_services"],
                "active": True
            },

            "CanonicalizationManager": {
                "layer": "infrastructure",
                "produces": ["canonical_values"],
                "active": True
            },

            "CompetencyInferenceManager": {
                "layer": "semantic",
                "produces": ["inferred_competencies"],
                "active": True
            },

            # Optional / extended runtime components

            "CompetencyNormalizer": {
                "layer": "semantic",
                "produces": ["normalized_competencies"],
                "active": False
            },

            "ContractEnforcer": {
                "layer": "infrastructure",
                "produces": ["contract_validation"],
                "active": False
            },

            "FieldMemoryManager": {
                "layer": "infrastructure",
                "produces": ["memory_fields"],
                "active": False
            },

            "IngestionManager": {
                "layer": "infrastructure",
                "produces": ["raw_inputs"],
                "active": False
            },

            "OrchestrationManager": {
                "layer": "decision",
                "produces": ["execution_plan"],
                "active": False
            },

            "QueryManager": {
                "layer": "decision",
                "produces": ["queries"],
                "active": False
            },

            "SchemaAuditManager": {
                "layer": "infrastructure",
                "produces": ["schema_audit"],
                "active": False
            },

            "SHACLEngine": {
                "layer": "infrastructure",
                "produces": ["shacl_validation"],
                "active": False
            },

            "ShapesManager": {
                "layer": "infrastructure",
                "produces": ["shapes"],
                "active": False
            },

            "RuntimeHealthManager": {
                "layer": "infrastructure",
                "produces": ["health"],
                "active": True
            },

            "OntologyManagerBase": {
                "layer": "infrastructure",
                "produces": ["ontology_base"],
                "active": False
            },

            "CanonicalizationRegistry": {
                "layer": "infrastructure",
                "produces": ["canonical_registry"],
                "active": False
            },

        }

        # -------------------------
        # PROFILE FILTERING
        # -------------------------

        if profile == "minimal":

            return {

                "OntologyManager":
                    base["OntologyManager"],

                "TaxonomyManager":
                    base["TaxonomyManager"],

                "InstanceManager":
                    base["InstanceManager"],

                "SemanticCoreManager":
                    base["SemanticCoreManager"],

                "CompetencyInferenceManager":
                    base["CompetencyInferenceManager"],

                "ReasoningManager":
                    base["ReasoningManager"],

                "ProvenanceManager":
                    base["ProvenanceManager"],

            }

        if profile == "debug":

            return base  # everything visible

        if profile == "observability":

            return {
                k: v for k, v in base.items()
                if v.get("active", False)
                or v["layer"] == "infrastructure"
            }

        # default production runtime

        return {
            k: v for k, v in base.items()
            if v.get("active", False)
        }
