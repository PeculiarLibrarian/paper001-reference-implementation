from peculiarlibrary.audits.kernel_audit import KernelAudit

class AuditOperator:
    """
    Adapter operator for kernel audit layer.

    Ensures compatibility with class-based KernelAudit API.
    """

    def execute(self, payload):
        graph = payload.get("graph")

        auditor = KernelAudit()
        report = auditor.run()

        return {
            "status": "audited",
            "conforms": report.passed,
            "graph": graph,
            "audit": {
                "name": report.name,
                "summary": report.summary,
                "details": report.details,
            }
        }
