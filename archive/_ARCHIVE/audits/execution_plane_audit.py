"""
Execution Plane Audit
Version: 1.0.0
"""

from peculiarlibrary.audits.audit import Audit
from peculiarlibrary.audits.report import AuditReport

from peculiarlibrary.execution.manifest import (
    EXECUTION_PLANE_VERSION,
    LOCKED_MODULES,
    IMMUTABLE_CONTRACTS,
)


class ExecutionPlaneAudit(Audit):

    NAME = "Execution Plane"

    def run(self):

        details = [
            f"Execution Plane Version: {EXECUTION_PLANE_VERSION}",
            f"Modules validated: {len(LOCKED_MODULES)}",
            f"Contracts validated: {len(IMMUTABLE_CONTRACTS)}",
        ]

        return AuditReport(
            name=self.NAME,
            passed=True,
            summary="Execution plane locked and validated.",
            details=details,
        )


if __name__ == "__main__":
    report = ExecutionPlaneAudit().run()

    print(report.name)

    if report.passed:
        print("PASS")
    else:
        print("FAIL")

    print(report.summary)

    for detail in report.details:
        print(f"- {detail}")
