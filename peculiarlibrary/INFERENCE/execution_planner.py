"""
PADI Execution Planner
Version: 3.0.0

Builds deterministic inference execution plans from RDF rules.

Responsibilities
----------------
- Resolve institution execution order.
- Resolve associated execution stages.
- Preserve deterministic ordering.

Non-responsibilities
--------------------
- Execute rules.
- Build assertions.
- Validate inference.
- Persist results.
"""

from __future__ import annotations

from dataclasses import dataclass

from rdflib import Graph, URIRef


PADI = "http://padi.s.m.gitandu.bs/core#"


@dataclass(frozen=True)
class ExecutionStep:

    institution: str
    stage: str


class ExecutionPlanner:

    def __init__(self):

        self.institution_name = URIRef(
            PADI + "institutionName"
        )

        self.executes_stage = URIRef(
            PADI + "executesStage"
        )

        self.next_institution = URIRef(
            PADI + "nextInstitution"
        )

    def build_plan(
        self,
        graph: Graph,
    ) -> tuple[ExecutionStep, ...]:

        institutions = {}

        for subject in graph.subjects(
            self.institution_name,
            None,
        ):

            name = graph.value(
                subject,
                self.institution_name,
            )

            stage = graph.value(
                subject,
                self.executes_stage,
            )

            nxt = graph.value(
                subject,
                self.next_institution,
            )

            institutions[str(subject)] = {
                "name": str(name),
                "stage": str(stage) if stage else None,
                "next": str(nxt) if nxt else None,
            }

        if not institutions:
            raise RuntimeError(
                "No inference institutions found."
            )

        referenced = {
            item["next"]
            for item in institutions.values()
            if item["next"]
        }

        roots = [
            key
            for key in institutions
            if key not in referenced
        ]

        if len(roots) != 1:
            raise RuntimeError(
                f"Expected one root institution, found {len(roots)}"
            )

        plan = []

        current = roots[0]

        visited = set()

        while current:

            if current in visited:
                raise RuntimeError(
                    "Cycle detected in inference chain."
                )

            visited.add(current)

            item = institutions[current]

            plan.append(
                ExecutionStep(
                    institution=item["name"],
                    stage=item["stage"],
                )
            )

            current = item["next"]

        if len(plan) != len(institutions):
            raise RuntimeError(
                "Disconnected institution graph."
            )

        return tuple(plan)
