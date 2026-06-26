from managers.ontology_manager import OntologyManager
from managers.instance_manager import InstanceManager
from managers.semantic_core_manager import SemanticCoreManager
from managers.reasoning_manager import ReasoningManager
from managers.opportunity_engine import OpportunityEngine
from managers.explanation_engine import ExplanationEngine


class ManagerRegistry:
    """
    Single source of truth for available agents.
    """

    @staticmethod
    def get():
        return {
            "OntologyManager": OntologyManager(),
            "InstanceManager": InstanceManager(),
            "SemanticCoreManager": SemanticCoreManager(),
            "ReasoningManager": ReasoningManager(),
            "OpportunityEngine": OpportunityEngine(),
            "ExplanationEngine": ExplanationEngine(),
        }
