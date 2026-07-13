from peculiarlibrary.audits.registry import AUDITS


def main():

    print("=" * 70)
    print("GLOBAL INVARIANCE MATRIX v4")
    print("=" * 70)

    reports = []

    for audit in AUDITS:
        report = audit.run()
        reports.append(report)

        print(f"\n{report.name}")
        print("-" * len(report.name))
        print(f"{report.status:<5} : {report.summary}")

        if report.details:
            for item in report.details:
                print(f"  - {item}")

    passed = sum(r.passed for r in reports)
    total = len(reports)

    print("\n" + "=" * 70)
    print(f"RESULT: {passed}/{total} audits passed")

    if passed == total:
        print("OVERALL STATUS: PASS")
    else:
        print("OVERALL STATUS: FAIL")

    print("=" * 70)


if __name__ == "__main__":
    main()
