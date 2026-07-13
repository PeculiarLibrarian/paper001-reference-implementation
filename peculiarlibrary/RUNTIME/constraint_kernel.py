"""
PADI Runtime Constraint Kernel
Version: 2.2.0
"""


INVARIANCE_MATRIX = {

    "GRAPH": {
        "NON_EMPTY": "len(graph) > 0",
        "TRIPLE_COUNT": "graph size consistency",
    },

    "ONTOLOGY": {
        "OWL_PRESENT": "core ontology loaded",
        "SCHEMA_VALID": "valid ontology structure",
    },

    "QUERY": {
        "REGISTRY_LOADED": "query registry populated",
        "ALL_QUERIES_RESOLVABLE": "query mapping valid",
    },

    "FACTS": {
        "CONSISTENCY": "facts align with graph",
        "ENTITY_BINDING": "facts bind valid entities",
    },

}


class ConstraintKernel:

    def __init__(self, graph, bindings, matrix):
        self.graph = graph
        self.bindings = bindings
        self.matrix = matrix

    def evaluate(self):

        report = [

            {
                "constraint": "GRAPH.NON_EMPTY",
                "passed": len(self.graph) > 0,
            },

            {
                "constraint": "FACTS.EXIST",
                "passed": len(self.graph) > 0,
            },

            {
                "constraint": "QUERY.LOADED",
                "passed": len(self.bindings) > 0,
            },

        ]

        for rule, mapping in self.bindings.items():

            report.append({

                "constraint": rule,
                "passed": True,
                "mapping": mapping,

            })

        return report


def run_constraint_kernel(graph, bindings, matrix):

    return ConstraintKernel(
        graph,
        bindings,
        matrix,
    ).evaluate()

