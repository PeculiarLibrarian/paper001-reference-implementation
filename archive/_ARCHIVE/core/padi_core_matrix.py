"""
PADI CORE MATRIX
Version: 1.0.0

GLOBAL SYSTEM OF INVARIANCE

This file is the SINGLE SOURCE OF TRUTH for:
- layer boundaries
- execution permissions
- compiler constraints
- ontology safety rules
"""

CORE_MATRIX = {
    "semantic_layer": {
        "CanonicalFact",
        "Entity",
        "Metric",
        "ReportingPeriod",
        "MeasurementUnit",
        "OntologyRegistry",
        "IdentityResolver",
    },

    "compiler_layer": {
        "SemanticCompiler",
        "CanonicalCompiler",
    },

    "execution_layer": {
        "CompileOperator",
        "FactoryRegistry",
        "SemanticFactFactory",
    },

    "materialization_layer": {
        "RDFMaterializer",
    },

    "runtime_layer": {
        "SemanticDataset",
        "KPIEngine",
        "CrossEntityReasoner",
    },
}


def validate(layer: str, component: str) -> bool:
    if layer not in CORE_MATRIX:
        raise ValueError(f"[PADI CORE MATRIX] Unknown layer: {layer}")

    if component not in CORE_MATRIX[layer]:
        raise PermissionError(
            f"[PADI CORE MATRIX VIOLATION] {component} not allowed in {layer}"
        )

    return True


def get_layer(layer: str):
    return CORE_MATRIX.get(layer, set())


def dump_matrix():
    return CORE_MATRIX
