from pathlib import Path

from peculiarlibrary.audits.audit import Audit
from peculiarlibrary.audits.report import AuditReport


class StructureAudit(Audit):

    NAME = "Repository Structure"

    REQUIRED = [
        "peculiarlibrary/ontology/core_library.ttl",
        "peculiarlibrary/taxonomy/core_skos_library.ttl",
        "peculiarlibrary/shapes/core_shacl_library.ttl",
        "peculiarlibrary/context/core.context.jsonld",
        "peculiarlibrary/align/padi-align.ttl",
        "peculiarlibrary/ingestion",
        "peculiarlibrary/factory",
        "peculiarlibrary/ledger",
        "peculiarlibrary/api",
        "peculiarlibrary/reasoning",
        "peculiarlibrary/queries",
    ]

    def run(self):

        missing = []

        for item in self.REQUIRED:
            if not Path(item).exists():
                missing.append(item)

        return AuditReport(
            name=self.NAME,
            passed=len(missing) == 0,
            summary=f"{len(self.REQUIRED) - len(missing)}/{len(self.REQUIRED)} required artifacts present.",
            details=missing,
        )
