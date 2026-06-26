from contracts.data_contract import (
    OntologyBundle,
    TaxonomyBundle,
    ShapesBundle,
    QueryBundle,
    FieldMemoryBundle
)

CONTRACT_MAP = {

    "OntologyManager": OntologyBundle,
    "TaxonomyManager": TaxonomyBundle,
    "ShapesManager": ShapesBundle,
    "QueryManager": QueryBundle,
    "FieldMemoryManager": FieldMemoryBundle,

    # derived / inference managers (consume multiple contracts)
    "OpportunityEngine": (OntologyBundle, TaxonomyBundle),
    "ReasoningManager": (OntologyBundle, QueryBundle),
    "SemanticCoreManager": (OntologyBundle, TaxonomyBundle, ShapesBundle),

}
