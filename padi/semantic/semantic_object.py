from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SemanticObject:
    """
    Root semantic object.

    Every semantic concept in PADI derives from this class.

    No RDF.
    No URI.
    No Graph.
    """
    pass
