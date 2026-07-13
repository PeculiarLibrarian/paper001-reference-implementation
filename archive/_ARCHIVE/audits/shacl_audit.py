import subprocess
from shutil import which

from peculiarlibrary.audits.audit import Audit
from peculiarlibrary.audits.report import AuditReport


class SHACLAudit(Audit):

    NAME = "SHACL Validation"

    def _find_shacl(self):
        # deterministic resolution
        candidates = [
            which("shacl"),
            which("riot"),
            "apache-jena-4.10.0/bin/shacl",
        ]

        for c in candidates:
            if c:
                return c

        raise FileNotFoundError("SHACL binary not found in environment")

    def run(self) -> AuditReport:
        try:
            shacl_bin = self._find_shacl()

            cmd = [
                shacl_bin,
                "--version",
            ]

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
            )

            ok = result.returncode == 0

            details = [
                f"Binary: {shacl_bin}",
                result.stdout.strip(),
                result.stderr.strip() if result.stderr else "",
            ]

            return AuditReport(
                name=self.NAME,
                passed=ok,
                summary="SHACL toolchain operational." if ok else "SHACL toolchain failed.",
                details=[d for d in details if d],
            )

        except Exception as e:
            return AuditReport(
                name=self.NAME,
                passed=False,
                summary="SHACL execution failed.",
                details=[str(e)],
            )
