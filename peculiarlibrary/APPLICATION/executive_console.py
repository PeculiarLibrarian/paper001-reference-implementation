"""
PADI Technical Standard

Executive Console

Purpose
-------
Human-facing entry point for organizational intelligence.

Delegates execution to ManagementService.
"""

from pprint import pprint

from peculiarlibrary.APPLICATION.management_service import (
    ManagementService,
)


class ExecutiveConsole:
    """
    Canonical executive interface.
    """

    def __init__(self):
        self.management = ManagementService()

    def run(self):

        context = self.management.execute()

        print("=" * 60)
        print("PADI EXECUTIVE CONSOLE")
        print("=" * 60)

        print("\nANALYTICS")
        print("-" * 60)
        pprint(context.analytics)

        print("\nREPORT")
        print("-" * 60)
        pprint(context.reports)

        print("\nDASHBOARD")
        print("-" * 60)
        pprint(context.dashboard)

        print("\nDECISION SUPPORT")
        print("-" * 60)
        pprint(context.recommendations)

        print("\n" + "=" * 60)
        print("EXECUTION COMPLETE")
        print("=" * 60)


if __name__ == "__main__":
    ExecutiveConsole().run()
