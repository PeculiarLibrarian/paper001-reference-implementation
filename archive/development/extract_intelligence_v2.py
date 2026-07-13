from collections import Counter, defaultdict

class EntityFieldModel:
    def run(self, graph):
        counts = Counter()

        for s, p, o in graph:
            counts[str(s)] += 1

        total = len(graph) or 1

        return {
            "entities": [
                {
                    "uri": uri,
                    "signal_strength": count / total
                }
                for uri, count in counts.items()
            ]
        }


class RelationGravityModel:
    KEYWORDS = {
        "revenue": 1.0,
        "mpesa": 0.9,
        "ebitda": 0.85,
        "board": 0.6,
        "approval": 0.6,
        "service": 0.7
    }

    def run(self, graph):
        weights = Counter()

        for s, p, o in graph:
            p_str = str(p).lower()

            score = 0.2
            for k, w in self.KEYWORDS.items():
                if k in p_str:
                    score = max(score, w)

            weights[str(p)] += score

        total = sum(weights.values()) or 1

        return {
            "relations": {
                k: v / total for k, v in weights.items()
            }
        }


class DomainSignalClassifier:
    def run(self, graph):
        financial = telecom = governance = 0

        for s, p, o in graph:
            p = str(p).lower()

            if "revenue" in p or "ebitda" in p:
                financial += 1

            if "mpesa" in p:
                telecom += 1

            if "board" in p or "approval" in p:
                governance += 1

        total = financial + telecom + governance or 1

        return {
            "domains": {
                "financial_activity": financial / total,
                "telecom_operations": telecom / total,
                "governance_activity": governance / total
            }
        }


class IntelligenceLayerV2:
    def extract(self, graph):
        efm = EntityFieldModel().run(graph)
        rgm = RelationGravityModel().run(graph)
        dsc = DomainSignalClassifier().run(graph)

        return {
            "entity_field_model": efm,
            "relation_gravity_model": rgm,
            "domain_signal_classifier": dsc,
            "meta": {
                "triples_analyzed": len(graph)
            }
        }
