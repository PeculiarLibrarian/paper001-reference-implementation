from pathlib import Path

from peculiarlibrary.audits.audit import Audit
from peculiarlibrary.audits.report import AuditReport


class DependencyAudit(Audit):
    """
    Ensures the execution plane never depends on the operator plane.

    Allowed:

        PADI
            ↓
        peculiarlibrary
            ↓
        peculiarlibrarian

    Forbidden:

        peculiarlibrary -> peculiarlibrarian
    """

    NAME = "Dependency Rule"

    ROOT = Path("peculiarlibrary")

    FORBIDDEN = (
        "import peculiarlibrarian",
        "from peculiarlibrarian",
    )

    def run(self):

        violations = []

        for file in self.ROOT.rglob("*.py"):

            # Skip this audit implementation itself.
            if file.name == "dependency_audit.py":
                continue

            source = file.read_text(encoding="utf-8")

            for forbidden in self.FORBIDDEN:
                if forbidden in source:
                    violations.append(
                        f"{file}: {forbidden}"
                    )

        return AuditReport(
            name=self.NAME,
            passed=not violations,
            summary=(
                "Layer boundary respected."
                if not violations
                else f"{len(violations)} dependency violation(s) found."
            ),
            details=violations,
        )
