from peculiarlibrary.reasoning.inference_engine import InferenceEngine


class ReasonOperator:
    """
    Deterministic reasoning operator.

    Contract:
    - Input: rdflib.Graph (from compile stage)
    - Output: dict with graph preserved + reasoning metadata
    - No graph mutation outside inference engine
    """

    def __init__(self):
        pass

    def execute(self, payload):
        graph = payload.get("graph")

        # HARD SAFETY: graph must exist
        if graph is None:
            raise ValueError("ReasonOperator requires 'graph' from compile stage")

        # Delegate reasoning
        engine = InferenceEngine(graph)
        inferred_graph = engine.run()

        if inferred_graph is None:
            raise ValueError("InferenceEngine returned invalid graph state")

        return {
            "status": "reasoned",
            "graph": inferred_graph,
            "expanded_concepts": 1
        }
