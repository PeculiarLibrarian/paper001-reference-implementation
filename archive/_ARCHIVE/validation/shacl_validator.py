from pyshacl import validate
from rdflib import Graph

class SHACLValidator:

    def validate(self, graph, shapes_path=None):
        shapes_graph = Graph()

        if shapes_path:
            shapes_graph.parse(shapes_path, format="turtle")

        conforms, report_graph, report_text = validate(
            data_graph=graph,
            shacl_graph=shapes_graph,
            inference="rdfs",
            abort_on_first=False
        )

        if not conforms:
            return {
                "conforms": False,
                "report": str(report_text)
            }

        return {
            "conforms": True,
            "report": "OK"
        }
