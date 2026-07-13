"""
PADI Technical Standard
Management Information System (MIS)

Module:
    Public Interface Contract

Purpose:
    Defines the stable entry point into the MIS layer.
    The MIS consumes validated knowledge from the completed
    Knowledge Organization Management (KOM) layer and never
    bypasses it.

Principles:
    - Read-only interaction with KOS/KOM.
    - No inference logic.
    - No validation logic.
    - No ontology mutation.
"""

from abc import ABC, abstractmethod


class MISInterface(ABC):
    """
    Abstract contract for all MIS implementations.
    """

    @abstractmethod
    def load(self):
        """Load validated organizational knowledge."""
        raise NotImplementedError

    @abstractmethod
    def analytics(self):
        """Return analytical summaries."""
        raise NotImplementedError

    @abstractmethod
    def reports(self):
        """Generate management reports."""
        raise NotImplementedError

    @abstractmethod
    def dashboard(self):
        """Return dashboard-ready information."""
        raise NotImplementedError

    @abstractmethod
    def recommendations(self):
        """Return decision-support recommendations."""
        raise NotImplementedError
