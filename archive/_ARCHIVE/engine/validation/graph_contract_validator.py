from rdflib import URIRef, Literal


class GraphContractValidator:

    """
    Lightweight structural validator.
    Does NOT transform graph.
    Only asserts integrity constraints.
    """

    def validate(self, graph):

        issues = []

        for s, p, o in graph:

            # 1. Predicate sanity (critical for your current bug class)
            if not isinstance(p, URIRef):
                issues.append(("INVALID_PREDICATE", str(p)))

            # 2. Subject sanity
            if not isinstance(s, URIRef):
                issues.append(("INVALID_SUBJECT", str(s)))

            # 3. Object sanity (allow literals + URIs only)
            if not isinstance(o, (URIRef, Literal)):
                issues.append(("INVALID_OBJECT", str(o)))

            # 4. Detect malformed ontology duplication (your real bug pattern)
            if "ontology#http" in str(p):
                issues.append(("DOUBLE_PREFIX_DETECTED", str(p)))

        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "triple_count": len(graph)
        }
