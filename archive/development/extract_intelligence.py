from pathlib import Path

from rdflib import Graph

GRAPHSTORE = Path("peculiarlibrary/LIBRARIES/graphstore")


def main():
    if not GRAPHSTORE.exists():
        print(f"ERROR: {GRAPHSTORE} does not exist.")
        return

    ttl_files = sorted(GRAPHSTORE.glob("*.ttl"))

    if not ttl_files:
        print("ERROR: No materialized graphs found.")
        return

    graph_path = ttl_files[0]

    g = Graph()
    g.parse(graph_path, format="turtle")

    print("=" * 60)
    print("PADI MATERIALIZATION INSPECTOR")
    print("=" * 60)
    print(f"Graph   : {graph_path.name}")
    print(f"Triples : {len(g)}")
    print()

    for i, (s, p, o) in enumerate(g, start=1):
        print(f"[{i}]")
        print(f"  Subject   : {s}")
        print(f"  Predicate : {p}")
        print(f"  Object    : {o}")
        print()

    print("=" * 60)
    print(f"TOTAL TRIPLES: {len(g)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
