"""
PADI Technical Standard

System Verification

Runs complete platform validation.

Layers
------
1. Runtime
2. Inference
3. MIS
4. Application
"""

import subprocess
import sys


TESTS = [
    (
        "RUNTIME",
        "peculiarlibrary.RUNTIME.runtime_executor",
    ),
    (
        "INFERENCE",
        "peculiarlibrary.tests.test_inference",
    ),
    (
        "MIS",
        "peculiarlibrary.tests.test_mis",
    ),
    (
        "APPLICATION",
        "peculiarlibrary.tests.test_application",
    ),
]


def run_test(name, module):

    print("=" * 60)
    print(name)
    print("=" * 60)

    result = subprocess.run(
        [sys.executable, "-m", module],
        capture_output=False,
    )

    return result.returncode == 0


def main():

    results = {}

    for name, module in TESTS:
        results[name] = run_test(name, module)

    print("\n" + "=" * 60)
    print("SYSTEM VERIFICATION")
    print("=" * 60)

    for layer, status in results.items():
        print(
            f"{layer:<15}",
            "PASS" if status else "FAIL"
        )

    if all(results.values()):
        print("\nSYSTEM STATUS : PASS")
    else:
        print("\nSYSTEM STATUS : FAIL")


if __name__ == "__main__":
    main()
