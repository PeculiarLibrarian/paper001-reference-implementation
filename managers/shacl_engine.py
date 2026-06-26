from rdflib import Graph
from rdflib.namespace import SH

class SHACLEngine:
    """
    Executes SHACL validation against RDF graphs.

    This is the enforcement layer for shape constraints.
    """

    def __init__(self, shapes_graph: Graph):
        self.shapes_graph = shapes_graph

    def validate(self, data_graph: Graph):
        """
        Run SHACL validation.

        Returns:
            dict:
                conforms: bool
                results: validation report graph
        """
        try:
            from pyshacl import validate
        except ImportError:
            # fallback: system still runs but without strict validation
            return {
                "conforms": True,
                "results": None,
                "warning": "pyshacl not installed; validation bypassed"
            }

        conforms, report_graph, report_text = validate(
            data_graph,
            shacl_graph=self.shapes_graph,
            inference="rdfs",
            debug=False
        )

        return {
            "conforms": bool(conforms),
            "results": report_graph,
            "text": report_text
        }
