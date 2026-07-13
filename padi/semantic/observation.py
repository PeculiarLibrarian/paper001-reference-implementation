from dataclasses import dataclass

from .semantic_object import SemanticObject


@dataclass(frozen=True, slots=True)
class Observation(SemanticObject):
    """
    Base class for semantic observations.

    Intentionally contains no instance fields.

    Concrete observation types define their own structure.
    """
    pass
