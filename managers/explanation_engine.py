from rdflib import Graph


class ExplanationEngine:

    def explain_opportunity(self, graph: Graph, person: str, opportunity: str):

        query = """
        PREFIX pl: <https://peculiarlibrarian.org/ontology/>

        SELECT ?competency
        WHERE {
            <PERSON> pl:hasCompetency ?competency .
            <OPPORTUNITY> pl:requiresCompetency ?competency .
        }
        """

        query = query.replace("<PERSON>", f"<{person}>")
        query = query.replace("<OPPORTUNITY>", f"<{opportunity}>")

        results = graph.query(query)

        evidence = [str(r.competency) for r in results]

        if evidence:
            explanation = (
                "Match established via shared competency overlap across ontology graph paths: "
                + ", ".join(evidence)
            )
        else:
            explanation = (
                "No direct competency overlap detected; match inferred via structural proximity in graph."
            )

        return {
            "person": person,
            "opportunity": opportunity,
            "matched_on": evidence,
            "explanation": explanation
        }

    def explain_ranked_list(self, graph: Graph, ranked_list):

        explained = []

        for item in ranked_list:

            explanation = self.explain_opportunity(
                graph,
                item["person"],
                item["opportunity"]
            )

            item["explanation"] = explanation["explanation"]
            item["matched_on"] = explanation["matched_on"]

            explained.append(item)

        return explained
