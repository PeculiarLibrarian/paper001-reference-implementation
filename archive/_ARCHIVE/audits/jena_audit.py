import subprocess
from shutil import which

from peculiarlibrary.audits.audit import Audit
from peculiarlibrary.audits.report import AuditReport


class JenaAudit(Audit):

    NAME = "Apache Jena"

    def _resolve(self, name):
        return which(name) or f"apache-jena-4.10.0/bin/{name}"

    def run(self) -> AuditReport:
        try:
            shacl = self._resolve("shacl")
            riot = self._resolve("riot")

            results = []

            for cmd in [
                [shacl, "--version"],
                [riot, "--version"],
            ]:
                p = subprocess.run(cmd, capture_output=True, text=True)
                results.append((cmd[0], p.returncode, p.stdout.strip(), p.stderr.strip()))

            passed = all(r[1] == 0 for r in results)

            details = []
            for r in results:
                details.append(f"{r[0]} -> {'OK' if r[1]==0 else 'FAIL'}")
                if r[2]:
                    details.append(r[2])
                if r[3]:
                    details.append(r[3])

            return AuditReport(
                name=self.NAME,
                passed=passed,
                summary="Apache Jena toolchain operational." if passed else "Apache Jena toolchain unstable.",
                details=details,
            )

        except Exception as e:
            return AuditReport(
                name=self.NAME,
                passed=False,
                summary="Jena audit execution failed.",
                details=[str(e)],
            )
