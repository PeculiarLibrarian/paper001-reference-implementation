from peculiarlibrary.reasoning.inference_engine import InferenceEngine
from peculiarlibrary.reasoning.skos_expander import SKOSExpander


class ReasonOperator:

    VERSION = "1.0.0"

    def execute(self, payload: dict):

        graph = payload.get("graph")

        engine = InferenceEngine()
        expander = SKOSExpander()

        graph = engine.infer(graph)
        graph = expander.expand(graph)

        return {
            "status": "reasoned",
            "graph": graph,
            "expanded_concepts": 1,
            "triples": len(graph),
        }
