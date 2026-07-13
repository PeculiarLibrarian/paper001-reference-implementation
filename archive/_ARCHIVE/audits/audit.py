from abc import ABC, abstractmethod

class Audit(ABC):
    """
    Base class for all repository audits.
    """

    NAME = ""

    @abstractmethod
    def run(self):
        """
        Returns an AuditReport.
        """
        raise NotImplementedError
