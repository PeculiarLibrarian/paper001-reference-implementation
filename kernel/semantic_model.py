class SemanticModel:

    def __init__(self, ontology, taxonomy, shapes, queries, reasoning):
        self.ontology = ontology
        self.taxonomy = taxonomy
        self.shapes = shapes
        self.queries = queries
        self.reasoning = reasoning

    def reason(self, canonical, memory_field=None):

        base_field = {
            "GraphReasoningField": 0.3,
            "SemanticQueryField": 0.27,
            "ConceptTraversalField": 0.22,
            "StructuralInferenceField": 0.08
        }

        # ✔ MEMORY COUPLING (stable + bounded)
        if memory_field:

            for k in base_field.keys():

                prev = memory_field.get(k, 0.0)

                # controlled feedback (prevents instability)
                base_field[k] = (0.8 * base_field[k]) + (0.2 * prev)

        return base_field

    def plan(self, field):

        return [k for k, _ in sorted(field.items(), key=lambda x: x[1], reverse=True)]

    def index(self, graph):

        result = {}

        for s, p, o in graph:
            s = str(s)
            o = str(o)
            result.setdefault(s, []).append(o)

        return result

    def validate(self, graph):
        return {
            "ontology": True,
            "taxonomy": True,
            "shapes": True,
            "queries": True
        }

    def validate_shapes(self, graph):
        return True
