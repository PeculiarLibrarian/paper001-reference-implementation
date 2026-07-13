from rdflib import Graph

from peculiarlibrary.audits.audit import Audit
from peculiarlibrary.audits.report import AuditReport
from peculiarlibrary.reasoning.inference_engine import InferenceEngine


class ReasonerAudit(Audit):

    NAME = "Reasoner Integrity"

    def run(self) -> AuditReport:

        try:

            graph = Graph()

            before = id(graph)

            engine = InferenceEngine(graph)

            result = engine.run()

            details = []

            if not isinstance(result, Graph):
                return AuditReport(
                    name=self.NAME,
                    passed=False,
                    summary="Inference engine returned an invalid object.",
                    details=[
                        f"Returned type: {type(result).__name__}",
                    ],
                )

            if id(result) != before:
                return AuditReport(
                    name=self.NAME,
                    passed=False,
                    summary="Inference engine replaced the graph instance.",
                    details=[
                        "Expected in-place inference.",
                    ],
                )

            details.append("Inference engine imported.")
            details.append("Graph accepted.")
            details.append("Graph returned.")
            details.append(f"Triples after inference: {len(result)}")

            return AuditReport(
                name=self.NAME,
                passed=True,
                summary="Inference engine contract validated.",
                details=details,
            )

        except Exception as e:

            return AuditReport(
                name=self.NAME,
                passed=False,
                summary="Reasoner audit execution failed.",
                details=[str(e)],
            )


if __name__ == "__main__":

    report = ReasonerAudit().run()

    print(report.name)
    print(report.status)
    print(report.summary)

    for line in report.details:
        print(line)
