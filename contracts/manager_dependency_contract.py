from typing import Dict, List


class ManagerDependencyContract:

    DEPENDENCIES: Dict[str, Dict[str, List[str]]] = {

        # -------------------------
        # CORE PIPELINE
        # -------------------------

        "OntologyManager": {
            "depends_on": [],
            "produces": ["graph"]
        },

        "InstanceManager": {
            "depends_on": ["graph"],
            "produces": ["instances"]
        },

        "SemanticCoreManager": {
            "depends_on": ["graph", "instances"],
            "produces": ["core"]
        },

        "ReasoningManager": {
            "depends_on": ["core"],
            "produces": ["facts"]
        },

        # -------------------------
        # NEW CRITICAL LAYER: PROVENANCE
        # -------------------------

        "ProvenanceManager": {
            "depends_on": ["facts"],
            "produces": ["provenance"]
        },

        # -------------------------
        # DECISION LAYER
        # -------------------------

        "OpportunityEngine": {
            "depends_on": ["provenance"],
            "produces": ["ranked_opportunities"]
        },

        "ExplanationEngine": {
            "depends_on": ["ranked_opportunities", "provenance"],
            "produces": ["explanations"]
        },

        # -------------------------
        # TAXONOMY LAYER
        # -------------------------

        "TaxonomyManager": {
            "depends_on": ["graph"],
            "produces": ["taxonomy", "concepts"]
        },

        # -------------------------
        # INFRASTRUCTURE LAYER (MISSING FIX)
        # -------------------------

        "GraphTraversalManager": {
            "depends_on": ["graph"],
            "produces": ["graph_services"]
        },

        "CanonicalizationManager": {
            "depends_on": [],
            "produces": ["canonical_values"]
        },

        "CanonicalizationRegistry": {
            "depends_on": ["canonical_values"],
            "produces": ["canonical_registry"]
        },

        "CompetencyInferenceManager": {
            "depends_on": ["core"],
            "produces": ["inferred_competencies"]
        },

        "CompetencyNormalizer": {
            "depends_on": ["inferred_competencies"],
            "produces": ["normalized_competencies"]
        },

        "ContractEnforcer": {
            "depends_on": ["core"],
            "produces": ["contract_validation"]
        },

        "FieldMemoryManager": {
            "depends_on": ["core"],
            "produces": ["memory_fields"]
        },

        "IngestionManager": {
            "depends_on": [],
            "produces": ["raw_inputs"]
        },

        "OrchestrationManager": {
            "depends_on": ["core"],
            "produces": ["execution_plan"]
        },

        "QueryManager": {
            "depends_on": ["core"],
            "produces": ["queries"]
        },

        "SchemaAuditManager": {
            "depends_on": ["taxonomy"],
            "produces": ["schema_audit"]
        },

        "SHACLEngine": {
            "depends_on": ["graph"],
            "produces": ["shacl_validation"]
        },

        "ShapesManager": {
            "depends_on": ["taxonomy"],
            "produces": ["shapes"]
        },

        "RuntimeHealthManager": {
            "depends_on": ["core"],
            "produces": ["health"]
        },

        "OntologyManagerBase": {
            "depends_on": [],
            "produces": ["ontology_base"]
        },

    }
