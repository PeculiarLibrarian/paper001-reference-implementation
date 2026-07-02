from rdflib import Namespace

class OntologyMapper:
    """
    Central ontology resolution layer.
    This prevents namespace drift between finance/core/governance.
    """

    def __init__(self):
        self.FIN = Namespace("http://padi.s.m.gitandu.bs/finance#")
        self.GOV = Namespace("http://padi.s.m.gitandu.bs/governance#")
        self.CORE = Namespace("http://padi.s.m.gitandu.bs/core#")

        # Canonical predicate registry
        self.map = {
            "service_revenue": self.FIN.ServiceRevenue,
            "ebitda": self.FIN.EBITDA,
            "mpesa_revenue": self.FIN.MPesaRevenue,
            "mpesa_capacity_tps": self.FIN.MPesaCapacityTPS,
            "monetary_gain_ias29": self.FIN.MonetaryGainIAS29,

            "board_approval_date": self.GOV.BoardApprovalDate,
        }

    def resolve(self, predicate: str):
        """
        Always returns a stable rdflib URIRef.
        """
        if predicate in self.map:
            return self.map[predicate]

        # fallback (DO NOT silently drift into core#)
        return self.CORE[predicate]
