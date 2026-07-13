from dataclasses import dataclass

from .semantic_object import SemanticObject


@dataclass(frozen=True, slots=True)
class Entity(SemanticObject):
    name: str
