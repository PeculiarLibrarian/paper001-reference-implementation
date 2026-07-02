from rdflib import Namespace


class OntologyRegistry:
    """
    Canonical namespace registry.

    Every component imports namespaces from here.
    No module should construct Namespace(...) directly.
    """

    CORE = Namespace("http://padi.s.m.gitandu.bs/core#")
    FIN = Namespace("http://padi.s.m.gitandu.bs/fin#")
    GOV = Namespace("http://padi.s.m.gitandu.bs/gov#")
    ORG = Namespace("http://padi.s.m.gitandu.bs/org#")
    ALIGN = Namespace("http://padi.s.m.gitandu.bs/align#")

    def __init__(self):

        self.namespaces = {
            "core": self.CORE,
            "fin": self.FIN,
            "gov": self.GOV,
            "org": self.ORG,
            "align": self.ALIGN,
        }

        self.predicates = {
            "service_revenue": self.FIN.service_revenue,
            "ebitda": self.FIN.ebitda,
            "mpesa_revenue": self.FIN.mpesa_revenue,
            "mpesa_capacity_tps": self.FIN.mpesa_capacity_tps,
            "monetary_gain_ias29": self.FIN.monetary_gain_ias29,
            "board_approval_date": self.FIN.board_approval_date,
            "period": self.CORE.period,
        }

    def resolve(self, predicate: str):
        return self.predicates.get(predicate)

    def namespace(self, prefix: str):
        return self.namespaces.get(prefix)
