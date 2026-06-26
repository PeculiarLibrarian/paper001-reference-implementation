from typing import Dict, List


class ManagerDependencyContract:

    DEPENDENCIES: Dict[str, Dict[str, List[str]]] = {

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

        "OpportunityEngine": {
            "depends_on": ["facts", "instances"],
            "produces": ["ranked_opportunities"]
        },

        "ExplanationEngine": {
            "depends_on": ["ranked_opportunities", "facts"],
            "produces": ["explanations"]
        },
    }
