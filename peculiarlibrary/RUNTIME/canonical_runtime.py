"""
PADI Canonical Runtime

Purpose
-------
Construct the immutable canonical semantic runtime.

Responsibilities
----------------
- Discover canonical datasets.
- Load canonical JSON facts.
- Map facts into MODEL objects.
- Materialize RDF.
- Build evidence records.
- Produce deterministic semantic summaries.

Non-responsibilities
--------------------
- No querying.
- No reasoning.
- No inference execution.
"""

from collections import defaultdict
from pathlib import Path
import json

from peculiarlibrary.RUNTIME.semantic_dataset import SemanticDataset
from peculiarlibrary.RUNTIME.evidence_runtime import EvidenceRuntime
from peculiarlibrary.RUNTIME.canonical_mapper import CanonicalMapper
from peculiarlibrary.RDF.rdf_materializer import RDFMaterializer


def discover_canonical_datasets():
    datasets = sorted(
        Path("peculiarlibrary/DATA").rglob(
            "canonical_facts.json"
        )
    )

    if not datasets:
        raise RuntimeError(
            "No canonical_facts.json datasets found."
        )

    return datasets


class CanonicalRuntime:

    VERSION = "2.0.0"

    def __init__(self):
        self.materializer = RDFMaterializer()
        self.evidence_runtime = EvidenceRuntime()
        self.mapper = CanonicalMapper()

    def load_facts(self):

        facts = []

        print("\n=== Canonical Dataset Discovery ===")

        datasets = discover_canonical_datasets()

        for dataset in datasets:

            with open(dataset, "r", encoding="utf-8") as f:
                payload = json.load(f)

            mapped = self.mapper.map_facts(
                payload["facts"]
            )

            facts.extend(mapped)

            print(
                f"✓ {dataset.parent.name:<20}"
                f"{len(mapped):>4} facts"
            )

        print("-----------------------------------")
        print(
            f"Total datasets : {len(datasets)}"
        )
        print(
            f"Total facts    : {len(facts)}"
        )

        self.print_summary(facts)
        self.print_predicate_registry(facts)

        print()

        return tuple(facts)

    def print_summary(self, facts):

        subjects = defaultdict(list)

        for fact in facts:
            subjects[fact.entity.name].append(fact)

        print(
            "\n=== Canonical Knowledge Summary ==="
        )

        predicates = set()

        for subject in sorted(subjects):

            metric_counts = defaultdict(int)

            for fact in subjects[subject]:
                metric_counts[fact.metric.name] += 1

            predicates.update(metric_counts)

            print(subject)
            print(
                f"  Facts      : {len(subjects[subject])}"
            )
            print(
                f"  Predicates : {len(metric_counts)}"
            )

            for metric in sorted(metric_counts):
                print(
                    f"    • {metric}"
                    f" ({metric_counts[metric]})"
                )

            print()

        print("-----------------------------------")
        print(
            f"Subjects     : {len(subjects)}"
        )
        print(
            f"Predicates   : {len(predicates)}"
        )

    def print_predicate_registry(self, facts):

        registry = defaultdict(int)

        for fact in facts:
            registry[fact.metric.name] += 1

        print("\n=== Predicate Registry ===")

        width = max(
            len(name)
            for name in registry
        )

        for metric in sorted(registry):
            dots = "." * (
                width - len(metric) + 8
            )

            print(
                f"{metric} {dots} {registry[metric]}"
            )

        print("-----------------------------------")
        print(
            f"Total predicate types : {len(registry)}"
        )

    def build_dataset(self):

        facts = self.load_facts()

        graph = self.materializer.materialize(
            facts
        )

        records = self.evidence_runtime.build_records(
            facts
        )

        return SemanticDataset(
            graph=graph,
            facts=facts,
            records=records,
        )


def build_canonical_view():

    return CanonicalRuntime().build_dataset()
