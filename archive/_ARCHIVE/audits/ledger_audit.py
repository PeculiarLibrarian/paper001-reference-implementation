import json
from pathlib import Path

from peculiarlibrary.audits.audit import Audit
from peculiarlibrary.audits.report import AuditReport


class LedgerAudit(Audit):

    NAME = "Ledger Integrity"

    REQUIRED_FIELDS = [
        "@context",
        "@type",
        "materializationId",
        "compilerVersion",
        "mapper",
        "dataset",
        "timestamp",
        "tripleCount",
        "validation",
        "provenance",
    ]

    def run(self):

        ledger = Path("runtime/materialization_ledger.jsonld")

        if not ledger.exists():
            return AuditReport(
                name=self.NAME,
                passed=False,
                summary="Materialization ledger missing.",
                details=[str(ledger)],
            )

        try:

            data = json.loads(ledger.read_text(encoding="utf-8"))

        except Exception as e:

            return AuditReport(
                name=self.NAME,
                passed=False,
                summary="Ledger is not valid JSON.",
                details=[str(e)],
            )

        if not isinstance(data, list):
            return AuditReport(
                name=self.NAME,
                passed=False,
                summary="Ledger root must be a JSON array.",
                details=[],
            )

        if len(data) == 0:
            return AuditReport(
                name=self.NAME,
                passed=False,
                summary="Ledger contains no materializations.",
                details=[],
            )

        latest = data[-1]

        missing = [
            field
            for field in self.REQUIRED_FIELDS
            if field not in latest
        ]

        if missing:
            return AuditReport(
                name=self.NAME,
                passed=False,
                summary="Ledger schema incomplete.",
                details=[
                    f"Missing: {', '.join(missing)}"
                ],
            )

        details = [
            f"Materializations: {len(data)}",
            f"Compiler: {latest['compilerVersion']}",
            f"Mapper: {latest['mapper']}",
            f"Triples: {latest['tripleCount']}",
            "Ledger schema validated.",
        ]

        return AuditReport(
            name=self.NAME,
            passed=True,
            summary="Materialization ledger validated.",
            details=details,
        )


if __name__ == "__main__":

    report = LedgerAudit().run()

    print(report.name)
    print(report.status)
    print(report.summary)

    for line in report.details:
        print(line)
