"""
PADI Runtime SHACL Bindings
Version: 2.2.0

Declarative runtime-to-SHACL mapping.
"""


SHACL_BINDINGS = {

    "GRAPH.NON_EMPTY": {
        "shacl": "sh:MinCount > 0 on rdf:Statement",
    },

    "ONTOLOGY.SCHEMA_VALID": {
        "shacl": (
            "OWL class declarations must exist "
            "in core_ontology.ttl"
        ),
    },

    "QUERY.REGISTRY_LOADED": {
        "shacl": (
            "SPARQL query registry must resolve "
            "all registered queries"
        ),
    },

    "FACTS.CONSISTENCY": {
        "shacl": (
            "Every CanonicalFact must bind "
            "aboutEntity"
        ),
    },

}
