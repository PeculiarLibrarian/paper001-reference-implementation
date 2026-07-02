from rdflib import Graph
from pyshacl import validate


class SHACLEngine:

    def __init__(self, shapes_path="peculiarlibrary/shapes/financial_constraints.ttl"):
        self.shapes_path = shapes_path

    def validate(self, graph):

        shapes = Graph()
        shapes.parse(self.shapes_path, format="turtle")

        conforms, report_graph, report_text = validate(
            data_graph=graph,
            shacl_graph=shapes,
            inference="rdfs",
            abort_on_first=False,
            meta_shacl=False,
            debug=False
        )

        print("\n🔍 SHACL VALIDATION RESULT")
        print("Conforms:", conforms)

        if not conforms:
            print("\n⚠ CONSTRAINT VIOLATIONS:")
            print(report_text)

        return conforms, report_graph, report_text


# Backward compatibility alias (so nothing else breaks)
class SHACLValidator(SHACLEngine):
    pass
