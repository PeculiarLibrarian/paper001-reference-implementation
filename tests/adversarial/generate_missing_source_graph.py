from pathlib import Path
import sys

from rdflib import Graph, Namespace

PADI = Namespace("http://padi.s.m.gitandu.bs/core#")

SOURCE_GRAPH = Path(
    "peculiarlibrary/STORE/graphstore/"
    "5ac4205a6f41c9df30f9999761317f46a2c3e8a2cfb2a25c1a40909ee29ac714.ttl"
)

OUTPUT_GRAPH = Path(
    "peculiarlibrary/STORE/graphstore/invalid_graph.ttl"
)

FACT = PADI["Fact_00001"]
SOURCE = PADI["Source_00001"]


def main() -> None:
    if not SOURCE_GRAPH.exists():
        sys.exit(f"ERROR: Source graph not found: {SOURCE_GRAPH}")

    graph = Graph()
    graph.parse(SOURCE_GRAPH, format="turtle")

    triple = (FACT, PADI.hasSource, SOURCE)

    if triple not in graph:
        sys.exit(
            "ERROR: Expected provenance triple was not found in the source graph.\n"
            "The adversarial fixture can no longer be generated deterministically."
        )

    graph.remove(triple)

    if triple in graph:
        sys.exit("ERROR: Failed to remove provenance triple.")

    OUTPUT_GRAPH.parent.mkdir(parents=True, exist_ok=True)
    graph.serialize(destination=OUTPUT_GRAPH, format="turtle")

    verification = Graph()
    verification.parse(OUTPUT_GRAPH, format="turtle")

    if triple in verification:
        sys.exit("ERROR: Invalid graph still contains the removed provenance triple.")

    print(f"Generated adversarial graph: {OUTPUT_GRAPH}")
    print("STATUS: PASS")


if __name__ == "__main__":
    main()
