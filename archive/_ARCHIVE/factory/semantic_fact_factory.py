class SemanticFactFactory:

    VERSION = "2.0.0"

    def __init__(self, graph):
        self.graph = graph

    def execute(self, command, graph):

        args = command["arguments"]

        graph.add(
            (
                args["subject"],
                args["predicate"],
                args["object"],
            )
        )

        return graph
