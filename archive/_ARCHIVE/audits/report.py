from dataclasses import dataclass, field

@dataclass(slots=True)
class AuditReport:
    """
    Immutable result returned by every audit.
    """

    name: str
    passed: bool
    summary: str
    details: list[str] = field(default_factory=list)

    @property
    def status(self) -> str:
        return "PASS" if self.passed else "FAIL"
