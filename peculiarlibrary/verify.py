"""
PADI System Verification Gate

Single command validation entry point.

Checks:
1. Architecture compliance
2. Runtime execution
3. Inference pipeline
4. MIS pipeline
5. Application pipeline
"""

import subprocess
import sys


CHECKS = [
    (
        "ARCHITECTURE",
        "peculiarlibrary.ARCHITECTURE.dependency_validator",
    ),
    (
        "SYSTEM",
        "peculiarlibrary.system_verification",
    ),
]


def run_check(name, module):

    print("=" * 60)
    print(name)
    print("=" * 60)

    result = subprocess.run(
        [sys.executable, "-m", module]
    )

    return result.returncode == 0


def main():

    results = {}

    for name, module in CHECKS:
        results[name] = run_check(name, module)

    print("\n" + "=" * 60)
    print("PADI RELEASE VERIFICATION")
    print("=" * 60)

    for name, status in results.items():
        print(
            f"{name:<20}",
            "PASS" if status else "FAIL"
        )

    if all(results.values()):
        print("\nSYSTEM STATUS : READY")
        return 0

    print("\nSYSTEM STATUS : FAILED")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
