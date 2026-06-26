"""
CanonicalizationRegistry (MECE Identity Layer)

Purpose:
- Extract canonical namespaces from schema folders
- Provide deterministic prefix resolution rules
- Replace hardcoded mappings in CanonicalizationManager

This is NOT reasoning logic.
This is NOT ontology interpretation.
It is deterministic schema indexing only.
"""

import os
from rdflib import Graph


class CanonicalizationRegistry:
    def __init__(self, schema_root="schemas"):
        self.schema_root = schema_root
        self.prefix_map = self._build_prefix_map()

    def _build_prefix_map(self):
        """
        Deterministically scan ontology + taxonomy schemas
        for namespace declarations.
        """

        prefix_map = {}

        ontology_path = os.path.join(self.schema_root, "ontology")
        taxonomy_path = os.path.join(self.schema_root, "taxonomy")

        for path in [ontology_path, taxonomy_path]:
            if not os.path.exists(path):
                continue

            for file in os.listdir(path):
                if file.endswith(".ttl") or file.endswith(".owl"):
                    full_path = os.path.join(path, file)

                    g = Graph()
                    try:
                        g.parse(full_path, format="turtle")
                    except Exception:
                        continue

                    for prefix, namespace in g.namespaces():
                        ns = str(namespace)
                        if ns not in prefix_map:
                            prefix_map[ns] = f"{prefix}:"

        return prefix_map

    def get_prefix_map(self):
        """
        Return deterministic prefix map.
        """
        return self.prefix_map

    def resolve(self, uri: str) -> str:
        """
        Convert full URIs into canonical prefixed forms.
        """

        if uri is None:
            return uri

        uri = str(uri)

        for ns, prefix in self.prefix_map.items():
            if uri.startswith(ns):
                return uri.replace(ns, prefix)

        return uri

    def debug(self):
        return {
            "prefix_count": len(self.prefix_map),
            "prefixes": self.prefix_map
        }
