from dataclasses import dataclass

from .semantic_object import SemanticObject
from .source_document import SourceDocument


@dataclass(frozen=True, slots=True)
class SourceRecord(SemanticObject):
    """
    Represents a precise citation inside a document.
    """

    document: SourceDocument

    page: int | None = None

    section: str | None = None

    context: str | None = None
