from rdflib import URIRef, Literal
from peculiarlibrary.factory.semantic_fact_factory import SemanticFactFactory


class FactoryRegistry:

    def __init__(self, graph):
        self.graph = graph
        self._registry = {
            "fin": SemanticFactFactory(self.graph),
        }

    def execute(self, command):
        factory = command["factory"]
        args = command["arguments"]

        subject = args["subject"]
        predicate = args["predicate"]
        obj = args["object"]

        if not hasattr(subject, "n3"):
            subject = URIRef(str(subject))

        if not hasattr(predicate, "n3"):
            predicate = URIRef(str(predicate))

        if isinstance(obj, (int, float)):
            obj = Literal(obj)

        elif isinstance(obj, str) and obj.startswith("http"):
            obj = URIRef(obj)

        elif not hasattr(obj, "n3"):
            obj = Literal(obj)

        return self._registry[factory].execute(
            {
                **command,
                "arguments": {
                    **args,
                    "subject": subject,
                    "predicate": predicate,
                    "object": obj,
                },
            },
            self.graph,
        )
