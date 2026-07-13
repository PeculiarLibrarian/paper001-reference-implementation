"""
PADI Constitution Audit
Version: 1.0.0

Validates the machine-readable PADI Constitution.
"""

from pathlib import Path
import yaml

from peculiarlibrary.audits.audit import Audit
from peculiarlibrary.audits.report import AuditReport


class ConstitutionAudit(Audit):

    NAME = "Constitution"

    REQUIRED_INVARIANTS = 5

    REQUIRED_CONTROL_CONTRACTS = 6

    REQUIRED_EXECUTION_CONTRACTS = 5

    REQUIRED_AUDITS = 13

    def run(self):

        constitution = Path(
            "peculiarlibrary/constitution/constitution.yaml"
        )

        if not constitution.exists():
            return AuditReport(
                self.NAME,
                False,
                "Constitution missing.",
                [],
            )

        doc = yaml.safe_load(constitution.read_text(encoding="utf-8"))

        details = []

        try:

            assert doc["constitution"]["status"] == "locked"

            assert (
                len(doc["constitutional_invariants"])
                == self.REQUIRED_INVARIANTS
            )

            assert (
                len(doc["immutable_contracts"]["control_plane"])
                == self.REQUIRED_CONTROL_CONTRACTS
            )

            assert (
                len(doc["immutable_contracts"]["execution_plane"])
                == self.REQUIRED_EXECUTION_CONTRACTS
            )

            assert (
                len(doc["audit"]["required_audits"])
                == self.REQUIRED_AUDITS
            )

        except Exception as e:

            return AuditReport(
                self.NAME,
                False,
                "Constitution validation failed.",
                [str(e)],
            )

        details.append(
            f"Version: {doc['constitution']['version']}"
        )

        details.append(
            f"Invariants: {len(doc['constitutional_invariants'])}"
        )

        details.append(
            f"Control contracts: {len(doc['immutable_contracts']['control_plane'])}"
        )

        details.append(
            f"Execution contracts: {len(doc['immutable_contracts']['execution_plane'])}"
        )

        details.append(
            f"Required audits: {len(doc['audit']['required_audits'])}"
        )

        return AuditReport(
            self.NAME,
            True,
            "Constitution validated.",
            details,
        )

if __name__ == "__main__":
    report = ConstitutionAudit().run()

    print(report.name)

    if report.passed:
        print("PASS")
    else:
        print("FAIL")

    print(report.summary)

    for detail in report.details:
        print(f"- {detail}")
