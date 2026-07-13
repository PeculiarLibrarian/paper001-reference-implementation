import sys
from peculiarlibrarian.engine.runtime.system_validator import SystemValidator
from peculiarlibrarian.engine.runtime.operator_runtime import OperatorRuntime


def main():

    if len(sys.argv) < 2:
        print("Usage: validate <dataset>")
        sys.exit(1)

    dataset = sys.argv[1]

    validator = SystemValidator(lambda: OperatorRuntime())
    report = validator.validate_pipeline(dataset)

    print("\n=== PIPELINE VALIDATION REPORT ===\n")

    for k, v in report.items():
        print(f"{k.upper():<10} : {v}")

    print("\n=== END REPORT ===")


if __name__ == "__main__":
    main()
