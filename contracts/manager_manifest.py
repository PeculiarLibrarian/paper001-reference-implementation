from typing import Dict


class ManagerManifest:
    """
    Canonical architectural registry.

    Every manager must declare:

    - layer
    - owns
    - consumes
    - produces

    The execution planner and validators consume this registry.
    """

    REGISTRY: Dict[str, Dict] = {

        "OntologyManager": {
            "layer": "schema",
            "owns": ["ontology"],
            "consumes": [],
            "produces": ["graph"],
        },

        "InstanceManager": {
            "layer": "semantic",
            "owns": ["instances"],
            "consumes": ["graph"],
            "produces": ["instances"],
        },

        "SemanticCoreManager": {
            "layer": "semantic",
            "owns": ["semantic_core"],
            "consumes": [
                "graph",
                "instances",
            ],
            "produces": ["core"],
        },

        "ReasoningManager": {
            "layer": "decision",
            "owns": ["reasoning"],
            "consumes": ["core"],
            "produces": ["facts"],
        },

        "OpportunityEngine": {
            "layer": "decision",
            "owns": ["opportunity_ranking"],
            "consumes": [
                "instances",
                "facts",
            ],
            "produces": [
                "ranked_opportunities",
            ],
        },

        "ExplanationEngine": {
            "layer": "decision",
            "owns": ["explanations"],
            "consumes": [
                "ranked_opportunities",
            ],
            "produces": [
                "explanations",
            ],
        },

        "TaxonomyManager": {
            "layer": "schema",
            "owns": ["taxonomy"],
            "consumes": [],
            "produces": [
                "taxonomy",
                "concepts",
            ],
        },

        "GraphTraversalManager": {
            "layer": "infrastructure",
            "owns": [
                "graph_traversal",
            ],
            "consumes": [
                "graph",
            ],
            "produces": [
                "graph_services",
            ],
        },

        "CanonicalizationManager": {
            "layer": "infrastructure",
            "owns": [
                "canonicalization",
            ],
            "consumes": [],
            "produces": [
                "canonical_values",
            ],
        },

        "CompetencyInferenceManager": {
            "layer": "semantic",
            "owns": [
                "competency_inference",
            ],
            "consumes": [
                "core",
            ],
            "produces": [
                "inferred_competencies",
            ],
        },
    }

    @classmethod
    def manifest(cls):
        return cls.REGISTRY
