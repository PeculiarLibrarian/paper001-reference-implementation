"""
Peculiar Librarian CLI
Version: 1.2.0
"""

import sys
import json

from peculiarlibrarian.engine.runtime.operator_runtime import OperatorRuntime
from peculiarlibrarian.cli.serializer import serialize


def main():

    if len(sys.argv) < 3:
        print("Usage: pc.py <operator> <payload_json>")
        sys.exit(1)

    operator = sys.argv[1]
    payload = json.loads(sys.argv[2])

    runtime = OperatorRuntime()
    result = runtime.execute(operator, payload)

    print(json.dumps(result, indent=2, default=serialize))


if __name__ == "__main__":
    main()
