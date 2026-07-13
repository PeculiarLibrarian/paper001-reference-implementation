from padi.core.core_matrix_enforcer import CoreMatrixEnforcer


def dump_matrix():
    """
    PADI Core Matrix (single source of structural truth)
    """

    enforcer = CoreMatrixEnforcer()

    return {
        "DATA": [],
        "RDF": [
            "CanonicalFact",
            "SourceDocument",
            "SourceRecord",
            "IdentityResolver",
            "OntologyRegistry"
        ],
        "SKOS": [],
        "SHACL": [],
        "SPARQL": [],
        "LEDGER": [],
        "RUNTIME": [
            "SemanticDataset",
            "CrossEntityReasoner",
            "KPIEngine"
        ],
        "COMPILER": [
            "CanonicalCompiler"
        ],
        "EXECUTION": [
            "CompileOperator",
            "FactoryRegistry",
            "SemanticFactFactory"
        ],
        "ENFORCER": enforcer.ALLOWED
    }


def validate_core_matrix():
    """
    Ensures structural integrity of the matrix.
    """
    matrix = dump_matrix()

    required_layers = [
        "DATA",
        "RDF",
        "SKOS",
        "SHACL",
        "SPARQL",
        "LEDGER",
        "RUNTIME",
        "COMPILER",
        "EXECUTION"
    ]

    missing = [l for l in required_layers if l not in matrix]

    return {
        "valid": len(missing) == 0,
        "missing_layers": missing,
        "total_layers": len(required_layers)
    }
