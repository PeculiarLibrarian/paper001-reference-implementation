"""
CLI Serialization Utilities
Version: 1.1.0

Deterministic recursive serialization for all operator outputs.
"""

from rdflib import Graph


def serialize(obj):

    # RDF Graph handling
    if isinstance(obj, Graph):
        return {
            "type": "rdf_graph",
            "triples": len(obj),
            "repr": obj.serialize(format="turtle")[:500]
        }

    # dictionaries (recursive safety)
    if isinstance(obj, dict):
        return {k: serialize(v) for k, v in obj.items()}

    # lists / tuples
    if isinstance(obj, (list, tuple)):
        return [serialize(x) for x in obj]

    # fallback primitives
    if isinstance(obj, (str, int, float, bool)) or obj is None:
        return obj

    # last-resort stable representation
    return {
        "type": obj.__class__.__name__,
        "repr": str(obj)
    }
