"""
Peculiar Librarian
Registry Model
Normative Specification v3.6.0
"""

from dataclasses import dataclass, field
from typing import FrozenSet, Dict, Any
import hashlib
import json


@dataclass(frozen=True)
class RegistryModel:
    """
    Immutable in-memory representation of a protocol registry.

    Every registry is identified by:
      - registry_id
      - version
      - immutable item set
      - optional metadata
    """

    registry_id: str
    version: str
    items: FrozenSet[str]
    metadata: Dict[str, Any] = field(default_factory=dict)

    @property
    def canonical(self) -> dict:
        return {
            "id": self.registry_id,
            "version": self.version,
            "items": sorted(self.items),
            "metadata": self.metadata,
        }

    def compute_hash(self) -> str:
        """
        Registry Hash
        SHA-256(Canonical JSON)
        """

        payload = json.dumps(
            self.canonical,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        ).encode("utf-8")

        return hashlib.sha256(payload).hexdigest()

    def contains(self, item: str) -> bool:
        return item in self.items

    def __contains__(self, item: str):
        return item in self.items

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(sorted(self.items))

    def __repr__(self):
        return (
            f"RegistryModel("
            f"id={self.registry_id!r}, "
            f"version={self.version!r}, "
            f"items={len(self.items)})"
        )
