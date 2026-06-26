from abc import ABC, abstractmethod
from typing import Any, Dict


class ManagerContract(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def handshake(self) -> Dict[str, Any]:
        ...

    @abstractmethod
    def load(self) -> None:
        ...

    @abstractmethod
    def discover(self) -> Dict[str, Any]:
        ...

    @abstractmethod
    def validate(self, payload: Dict[str, Any]) -> bool:
        ...

    @abstractmethod
    def expose(self) -> Dict[str, Any]:
        ...

    # 🔥 NEW UNIFIED EXECUTION CONTRACT
    @abstractmethod
    def execute(self, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        All managers MUST accept semantic context.
        """
        ...
