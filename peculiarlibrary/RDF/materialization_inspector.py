from pathlib import Path
from rdflib import Graph


def inspect(graph_path=None):
    store = Path("peculiarlibrary/LIBRARIES/graphstore")
    graphs = sorted(store.glob("*.ttl"))

    if not graphs:
        raise RuntimeError("No graphstore files found")

    graph_path = graph_path or graphs[-1]

    g = Graph()
    g.parse(graph_path, format="turtle")

    print("GRAPH FILE:", graph_path.name)
    print("TRIPLES:", len(g))

    subjects = set()
    predicates = set()

    for s, p, o in g:
        subjects.add(str(s))
        predicates.add(str(p))

    print("\nSUBJECT COUNT:", len(subjects))
    print("PREDICATE COUNT:", len(predicates))

    print("\nPREDICATES:")
    for p in sorted(predicates):
        print(" -", p)

    print("\nSAMPLE:")
    for i, (s, p, o) in enumerate(g):
        print(s, p, o)
        if i >= 5:
            break

    return g


if __name__ == "__main__":
    inspect()
