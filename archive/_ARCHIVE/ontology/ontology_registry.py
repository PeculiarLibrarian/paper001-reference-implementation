from urllib.parse import quote


class OntologyRegistry:

    def __init__(self):
        self.PADI = "http://padi.s.m.gitandu.bs/ontology#"

    def _slug(self, value: str):
        return quote(str(value).strip().replace(" ", "_"), safe="_-")

    def resolve(self, term: str):
        """
        Deterministic ontology resolution.
        Always returns URI-safe identifier.
        """
        return self.PADI + self._slug(term)
