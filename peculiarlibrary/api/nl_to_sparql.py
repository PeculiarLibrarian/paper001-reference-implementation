class NLToSPARQL:

    def __init__(self):
        self.prefix = """
PREFIX padi: <http://padi.s.m.gitandu.bs/fin#>
PREFIX core: <http://padi.s.m.gitandu.bs/core#>
"""

    def translate(self, question: str) -> str:
        q = question.lower()

        if "revenue" in q:
            return self.prefix + """
SELECT ?s ?value
WHERE {
    ?s padi:service_revenue ?value .
}
ORDER BY ?s
"""

        if "ebitda" in q:
            return self.prefix + """
SELECT ?s ?value
WHERE {
    ?s padi:ebitda ?value .
}
ORDER BY ?s
"""

        return self.prefix + """
SELECT ?s ?p ?o
WHERE {
    ?s ?p ?o .
}
LIMIT 20
"""
