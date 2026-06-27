class GraphContract:
    """
    Canonical contract for graph operations.
    Every graph implementation must expose these operations.
    """

    VERSION = "1.0"

    OPERATIONS = [
        "neighbors",
        "walk",
        "reachable",
        "shortest_path",
        "subgraph",
    ]

    def handshake(self):
        return {
            "contract": "graph_contract",
            "version": self.VERSION,
            "operations": self.OPERATIONS,
        }
