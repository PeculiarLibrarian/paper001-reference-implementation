from pathlib import Path

from peculiarlibrary.audits.audit import Audit
from peculiarlibrary.audits.report import AuditReport


class DomainAudit(Audit):
    """
    Ensures all required domain modules exist and are structurally complete.
    """

    NAME = "Domain Integrity"

    REQUIRED_DOMAINS = [
        "organization",
        "finance",
        "governance",
        "telecommunications",
    ]

    REQUIRED_ARTIFACTS = [
        "ontology.ttl",
        "taxonomy.ttl",
        "shapes.ttl",
        "padi-*.ttl",
        "context.jsonld",
    ]

    def run(self) -> AuditReport:

        base = Path("peculiarlibrary/domains")

        missing = []
        present_domains = 0

        for domain in self.REQUIRED_DOMAINS:

            domain_path = base / domain

            if not domain_path.is_dir():
                missing.append(f"{domain}: missing directory")
                continue

            present_domains += 1

            for artifact in self.REQUIRED_ARTIFACTS:

                if "*" in artifact:
                    ok = any(domain_path.glob(artifact))
                else:
                    ok = (domain_path / artifact).is_file()

                if not ok:
                    missing.append(f"{domain}: missing {artifact}")

        passed = not missing

        summary = (
            "All domain modules validated."
            if passed
            else f"{len(missing)} domain integrity issues detected."
        )

        details = [
            f"{present_domains}/{len(self.REQUIRED_DOMAINS)} domains present"
        ] + missing

        return AuditReport(
            name=self.NAME,
            passed=passed,
            summary=summary,
            details=details,
        )


if __name__ == "__main__":

    report = DomainAudit().run()

    print(report.name)
    print(report.status)
    print(report.summary)

    for line in report.details:
        print(line)
