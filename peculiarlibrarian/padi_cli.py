import os

from peculiarlibrarian.engine.runtime.operator_runtime import OperatorRuntime


HELP_TEXT = """
🧠 PADI Financial Intelligence Terminal

Commands
--------
ask <query>                 Natural language query
compare <metric>            Compare entities
rank <metric>               Rank entities
growth <entity> <metric>    Growth strength
health <entity> <metric>    Health score
ts <entity> <metric>        Time series
help                        Show help
exit                        Quit
"""


def format_result(value):
    if isinstance(value, dict):
        return "\n".join(f"{k}: {v}" for k, v in value.items())

    if isinstance(value, (list, tuple)):
        return "\n".join(str(v) for v in value)

    return str(value)


def resolve_dataset():
    env = os.getenv("PADI_DATASET")

    if env and os.path.exists(env):
        return env

    candidates = [
        "peculiarlibrary/DATA/safaricom/canonical_facts.json",
        "peculiarlibrary/DATA/equity_group/canonical_facts.json",
    ]

    for path in candidates:
        if os.path.exists(path):
            return path

    raise FileNotFoundError(
        "No canonical_facts.json dataset found."
    )


def main():

    print(HELP_TEXT)

    runtime_engine = OperatorRuntime()

    compiled = runtime_engine.execute(
        "compile",
        {
            "dataset": resolve_dataset(),
        },
    )

    runtime = compiled["runtime"]

    while True:

        try:

            raw = input("\n> ").strip()

            if not raw:
                continue

            if raw.lower() in ("exit", "quit"):
                break

            if raw.lower() == "help":
                print(HELP_TEXT)
                continue

            command, *rest = raw.split(maxsplit=1)
            argument = rest[0] if rest else ""

            if command == "compare":

                result = runtime_engine.execute(
                    "compare",
                    {
                        "metric": argument,
                        "runtime": runtime,
                    },
                )

            elif command == "rank":

                result = runtime_engine.execute(
                    "rank",
                    {
                        "metric": argument,
                        "runtime": runtime,
                    },
                )

            elif command == "growth":

                entity, metric = argument.split(maxsplit=1)

                result = runtime_engine.execute(
                    "growth",
                    {
                        "entity": entity,
                        "metric": metric,
                        "runtime": runtime,
                    },
                )

            elif command == "health":

                entity, metric = argument.split(maxsplit=1)

                result = runtime_engine.execute(
                    "health",
                    {
                        "entity": entity,
                        "metric": metric,
                        "runtime": runtime,
                    },
                )

            elif command == "ts":

                entity, metric = argument.split(maxsplit=1)

                result = runtime_engine.execute(
                    "time_series",
                    {
                        "entity": entity,
                        "metric": metric,
                        "runtime": runtime,
                    },
                )

            elif command == "ask":

                result = runtime_engine.execute(
                    "ask",
                    {
                        "query": argument,
                        "runtime": runtime,
                    },
                )

            else:

                result = runtime_engine.execute(
                    "ask",
                    {
                        "query": raw,
                        "runtime": runtime,
                    },
                )

            print("\n" + "=" * 60)
            print("RESULT")
            print("=" * 60)
            print(format_result(result))

        except Exception as exc:
            print(f"\n❌ {exc}")


if __name__ == "__main__":
    main()
