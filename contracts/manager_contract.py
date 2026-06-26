from abc import ABC, abstractmethod
from typing import Any, Dict


class ManagerContract(ABC):
    """
    Global A2A protocol.

    Every manager is an autonomous semantic agent.
    """

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

    @abstractmethod
    def execute(self) -> Dict[str, Any]:
        """
        Canonical A2A entrypoint.

        Internally:

            load()
            discover()
            validate()
            expose()

        Returns the exposed semantic bundle.
        """
        ...
