from peculiarlibrary.audits.audit import Audit
from peculiarlibrary.audits.report import AuditReport


class MappingAudit(Audit):

    NAME = "Mapping Integrity"

    def run(self) -> AuditReport:
        try:
            from peculiarlibrary.mappings.mapper import Mapper
            from peculiarlibrary.ingestion.doctrine_enforcer import DoctrineEnforcer

            mapper = Mapper()
            doctrine = DoctrineEnforcer()

            # Canonical mapping contract
            test_dataset = {
                "facts": [
                    {
                        "subject": "audit",
                        "predicate": "validates",
                        "object": "mapping",
                        "period": "2026",
                    }
                ]
            }

            commands = mapper.map(test_dataset)

            if not isinstance(commands, list):
                return AuditReport(
                    self.NAME,
                    False,
                    "Mapper output invalid.",
                    ["Mapper did not return a list."],
                )

            if len(commands) != 1:
                return AuditReport(
                    self.NAME,
                    False,
                    "Unexpected command count.",
                    [f"Expected 1 command, received {len(commands)}."],
                )

            validated = doctrine.validate(commands)

            return AuditReport(
                name=self.NAME,
                passed=True,
                summary="Mapping contract stable.",
                details=[
                    f"Commands: {len(validated)}",
                    "Mapper → Doctrine contract consistent.",
                ],
            )

        except Exception as e:
            return AuditReport(
                name=self.NAME,
                passed=False,
                summary="Mapping audit execution failed.",
                details=[str(e)],
            )


if __name__ == "__main__":
    report = MappingAudit().run()

    print(report.name)
    print(report.status)
    print(report.summary)

    for line in report.details:
        print(line)
