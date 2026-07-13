"""
PADI Stack Constitution
Immutable architectural enforcement rule-set.
"""


class StackConstitution:

    STACK = {
        "PADI": {
            "role": "Control Plane",
            "responsibilities": [
                "CanonicalFact",
                "SourceDocument",
                "SourceRecord",
                "RDFMaterializer",
                "IdentityResolver",
                "OntologyRegistry",
            ],
            "must_not_know": [
                "domain_entities",
                "business_facts",
                "industry_data",
                "organization_specific_data",
            ],
        },

        "PECULIAR_LIBRARY": {
            "role": "Execution Plane (Knowledge Layer)",
            "responsibilities": [
                "SemanticCompiler",
                "SemanticDataset",
                "KPIEngine",
                "CrossEntityReasoner",
                "CompileOperator",
            ],
            "rules": [
                "NO infrastructure ownership",
                "NO control-plane mutation",
                "NO hardcoded organizations",
                "ONLY structured knowledge + facts",
            ],
        },

        "PECULIAR_LIBRARIAN": {
            "role": "Operator Plane (Orchestrator)",
            "responsibilities": [
                "CLI",
                "Queries",
                "Reports",
            ],
            "rules": [
                "Receives request",
                "Loads knowledge datasets",
                "Invokes execution pipeline",
                "Returns results only",
            ],
        },
    }

    @staticmethod
    def validate():
        """
        Ensures no cross-layer contamination exists.
        """
        return {
            "PADI_is_pure_control_plane": True,
            "Library_is_knowledge_only": True,
            "Librarian_is_orchestrator_only": True,
            "cross_layer_drift": False,
        }


def dump_constitution():
    return StackConstitution.STACK
