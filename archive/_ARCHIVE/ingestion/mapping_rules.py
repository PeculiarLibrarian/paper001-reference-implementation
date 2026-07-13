"""
PADI Semantic Compiler v0.6.0

Generic Mapping Rules Interface

Purpose
-------
Transforms a canonical JSON-LD dataset into compiler commands.

This module contains NO organisation-specific logic.

Organisation-specific mappings belong under:

    peculiarlibrary/mappings/

For example:

    safaricom_mapper.py
    kcb_mapper.py
    equity_mapper.py
"""

from abc import ABC, abstractmethod


class MappingRules(ABC):
    """
    Base contract implemented by every dataset mapper.
    """

    @abstractmethod
    def map(self, dataset):
        """
        Convert a canonical dataset into factory commands.
        """
        raise NotImplementedError
