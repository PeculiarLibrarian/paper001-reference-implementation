from collections import defaultdict, deque

from rdflib import URIRef

from contracts.graph_contract import GraphContract


class GraphTraversalManager:

    name = "GraphTraversalManager"

    def __init__(self):

        self.contract = GraphContract()

        self.graph = None

        self.adjacency = defaultdict(list)

        self.edge_count = 0

    def handshake(self):

        return {
            "manager": self.name,
            "contract": self.contract.handshake(),
        }

    def load(self, graph):

        self.graph = graph

        self.adjacency.clear()

        self.edge_count = 0

        for s, p, o in self.graph:

            if isinstance(s, URIRef) and isinstance(o, URIRef):

                self.adjacency[str(s)].append(
                    {
                        "predicate": str(p),
                        "object": str(o),
                    }
                )

                self.edge_count += 1

    def execute(self, context):

        graph = context["graph"]

        self.load(graph)

        return self.expose()

    def neighbors(self, uri):

        return self.adjacency.get(str(uri), [])

    def walk(self, start_uri, max_depth=2):

        visited = set()

        queue = deque([(str(start_uri), 0)])

        traversal = []

        while queue:

            current, depth = queue.popleft()

            if current in visited:
                continue

            visited.add(current)

            traversal.append(
                {
                    "uri": current,
                    "depth": depth,
                }
            )

            if depth >= max_depth:
                continue

            for edge in self.neighbors(current):

                queue.append(
                    (
                        edge["object"],
                        depth + 1,
                    )
                )

        return traversal

    def statistics(self):

        return {
            "nodes": len(self.adjacency),
            "edges": self.edge_count,
        }

    def expose(self):

        return {
            "graph": self.graph,
            "adjacency": self.adjacency,
            "statistics": self.statistics(),
        }

    def reachable(self, start_uri, target_uri, max_depth=3):

        target_uri = str(target_uri)

        for node in self.walk(start_uri, max_depth=max_depth):

            if node["uri"] == target_uri:
                return True

        return False

    def shortest_path(self, start_uri, target_uri):

        start_uri = str(start_uri)
        target_uri = str(target_uri)

        queue = deque([(start_uri, [start_uri])])

        visited = set()

        while queue:

            current, path = queue.popleft()

            if current == target_uri:
                return path

            if current in visited:
                continue

            visited.add(current)

            for edge in self.neighbors(current):

                queue.append(
                    (
                        edge["object"],
                        path + [edge["object"]],
                    )
                )

        return []


    def subgraph(self, start_uri, max_depth=2):

        nodes = {
            node["uri"]
            for node in self.walk(start_uri, max_depth)
        }

        edges = []

        for subject in nodes:

            for edge in self.neighbors(subject):

                if edge["object"] in nodes:

                    edges.append(
                        {
                            "subject": subject,
                            "predicate": edge["predicate"],
                            "object": edge["object"],
                        }
                    )

        return {
            "nodes": sorted(nodes),
            "edges": edges,
        }

