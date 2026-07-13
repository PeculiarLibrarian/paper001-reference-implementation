"""
PADI Identity Resolver
Version: 1.0.0

The Identity Resolver is the canonical authority for semantic
identity generation.

No other component may manufacture URIs.

Responsibilities

- Deterministic identity
- Namespace management
- URI construction

No RDF logic.
No ontology logic.
No reasoning.
"""

from hashlib import sha256
from urllib.parse import quote


class IdentityResolver:

    VERSION = "1.0.0"

    NAMESPACES = {
        "entity": "http://padi.s.m.gitandu.bs/entity/",
        "metric": "http://padi.s.m.gitandu.bs/finance/",
        "period": "http://padi.s.m.gitandu.bs/period/",
        "unit": "http://padi.s.m.gitandu.bs/unit/",
        "document": "http://padi.s.m.gitandu.bs/document/",
        "source": "http://padi.s.m.gitandu.bs/source/",
        "fact": "http://padi.s.m.gitandu.bs/fact/",
    }

    def _slug(self, value):

        return quote(
            str(value).strip().replace(" ", "_"),
            safe="_-"
        )

    def _hash(self, *parts):

        text = "|".join(str(x) for x in parts)

        return sha256(
            text.encode("utf-8")
        ).hexdigest()[:16]

    def entity(self, name):

        return (
            self.NAMESPACES["entity"]
            + self._slug(name)
        )

    def metric(self, name):

        return (
            self.NAMESPACES["metric"]
            + self._slug(name)
        )

    def period(self, period):

        return (
            self.NAMESPACES["period"]
            + self._slug(period)
        )

    def unit(self, unit):

        return (
            self.NAMESPACES["unit"]
            + self._slug(unit)
        )

    def document(self, document):

        return (
            self.NAMESPACES["document"]
            + self._slug(document)
        )

    def source(self, document, page):

        return (
            self.NAMESPACES["source"]
            + self._hash(document, page)
        )

    def fact(self,
             entity,
             metric,
             period,
             value):

        return (
            self.NAMESPACES["fact"]
            + self._hash(
                entity,
                metric,
                period,
                value,
            )
        )
