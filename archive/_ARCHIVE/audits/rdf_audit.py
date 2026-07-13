from pathlib import Path

from rdflib import Graph

from peculiarlibrary.audits.audit import Audit
from peculiarlibrary.audits.report import AuditReport


class RDFAudit(Audit):
    """
    Verifies that every RDF artifact in the repository
    parses successfully.
    """

    NAME = "RDF Integrity"

    ROOT = Path("peculiarlibrary")
    EXTENSIONS = (".ttl", ".jsonld")

    def run(self) -> AuditReport:

        rdf_files = sorted(
            p
            for ext in self.EXTENSIONS
            for p in self.ROOT.rglob(f"*{ext}")
        )

        failures = []

        for rdf_file in rdf_files:

            graph = Graph()

            try:
                graph.parse(
                    rdf_file,
                    format="turtle"
                    if rdf_file.suffix == ".ttl"
                    else "json-ld",
                )

            except Exception as exc:
                failures.append(
                    f"{rdf_file}: {exc}"
                )

        total = len(rdf_files)

        if failures:
            return AuditReport(
                name=self.NAME,
                passed=False,
                summary=f"{len(failures)}/{total} RDF artifacts failed parsing.",
                details=failures,
            )

        return AuditReport(
            name=self.NAME,
            passed=True,
            summary=f"All {total} RDF artifacts parsed successfully.",
        )
