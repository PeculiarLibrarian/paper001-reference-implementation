from managers.ontology_manager_base import OntologyManagerBase


class OntologyManager(OntologyManagerBase):
    """
    Ontology ingestion + graph construction.
    """

    def execute(self, context=None):

        g = self._load_graph()

        return {
            "graph": g
        }
