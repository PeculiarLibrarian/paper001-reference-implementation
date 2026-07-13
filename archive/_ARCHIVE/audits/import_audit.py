import pkgutil

import peculiarlibrary

from peculiarlibrary.audits.audit import Audit
from peculiarlibrary.audits.report import AuditReport


class ImportAudit(Audit):
    """
    Ensures every importable module loads successfully.
    """

    NAME = "Python Imports"

    def run(self):

        failures = []

        for module in pkgutil.walk_packages(
            peculiarlibrary.__path__,
            peculiarlibrary.__name__ + ".",
        ):
            try:
                __import__(module.name)
            except Exception as exc:
                failures.append(
                    f"{module.name} -> {exc}"
                )

        return AuditReport(
            name=self.NAME,
            passed=len(failures) == 0,
            summary=f"{len(failures)} import failures."
            if failures
            else "All modules import successfully.",
            details=failures,
        )
