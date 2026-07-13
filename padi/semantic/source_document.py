from dataclasses import dataclass

from .semantic_object import SemanticObject


@dataclass(frozen=True, slots=True)
class SourceDocument(SemanticObject):
    """
    Represents a logical source document.

    A document exists independently of any particular citation.
    """

    title: str
    filename: str
