"""
SemanticCoreManager (MECE Layer 3)

Purpose:
- Convert canonicalized triples into structured semantic graph representation
- Bind ontology + taxonomy context
- Prepare graph for reasoning layer

NOT responsible for:
- inference
- planning
- capability selection
- execution ordering
"""

from collections import defaultdict


class SemanticCoreManager:
    def __init__(self):
        self.graph_index = defaultdict(set)

    def build(self, canonical_triples):
        """
        Build adjacency-style semantic index from canonical triples.
        """

        self.graph_index.clear()

        for s, p, o in canonical_triples:
            self.graph_index[s].add((p, o))

        return self.graph_index

    def extract_concepts(self, canonical_triples):
        """
        Extract unique semantic nodes (no inference).
        """

        nodes = set()

        for s, p, o in canonical_triples:
            nodes.add(s)
            nodes.add(o)

        return sorted(nodes)

    def project_relations(self, canonical_triples, predicate_filter=None):
        """
        Deterministic projection of relations.
        """

        relations = []

        for s, p, o in canonical_triples:

            if predicate_filter and p not in predicate_filter:
                continue

            relations.append((s, p, o))

        return relations

    def validate(self, graph_index):
        """
        Structural validation only.
        """

        return isinstance(graph_index, dict)
