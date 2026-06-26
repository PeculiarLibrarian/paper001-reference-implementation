class CanonicalizationManager:

    def __init__(self):
        pass

    def normalize(self, graph):
        """
        Deterministic canonicalization:
        converts RDF triples into sorted, stable representation.
        """

        if not graph:
            return []

        normalized = []

        for triple in graph:
            try:
                s, p, o = triple
            except Exception:
                continue

            normalized.append((str(s), str(p), str(o)))

        # deterministic ordering
        return sorted(normalized, key=lambda x: (x[0], x[1], x[2]))
