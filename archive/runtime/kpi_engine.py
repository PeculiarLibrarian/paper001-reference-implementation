from collections import defaultdict
from urllib.parse import urlparse


class KPIEngine:

    NUMERIC_PREDICATES = {
        "serviceRevenue",
        "ebitda",
        "mpesaRevenue",
        "mpesaCapacityTPS",
        "monetaryGainIAS29"
    }

    def __init__(self, dataset):
        self.graph = dataset.graph

    def _normalize(self, predicate):

        p = str(predicate)

        # handle fragment namespace (#)
        if "#" in p:
            return p.split("#")[-1]

        # handle slash namespace (/)
        if "/" in p:
            return p.split("/")[-1]

        # fallback: raw
        return p

    def compute(self):

        kpis = defaultdict(list)

        for s, p, o in self.graph:

            predicate = self._normalize(p)

            if predicate in self.NUMERIC_PREDICATES:

                try:
                    kpis[predicate].append(float(o))
                except Exception:
                    continue

        result = {}

        for k, v in kpis.items():
            if v:
                result[k] = {
                    "count": len(v),
                    "sum": sum(v),
                    "latest": v[-1],
                    "avg": sum(v) / len(v)
                }

        return result
