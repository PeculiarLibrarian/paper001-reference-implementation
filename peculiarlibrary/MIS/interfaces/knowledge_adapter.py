"""
PADI Technical Standard

MIS Knowledge Adapter

Purpose
-------
Normalizes validated Runtime and deterministic Inference
knowledge into MIS consumption format.

Principles
----------
- Does not mutate knowledge.
- Does not infer.
- Does not enrich canonical facts.
- Preserves all Runtime and Inference outputs.
"""


class MISKnowledgeAdapter:

    def adapt(self, knowledge):

        #
        # Already normalized MIS package
        #

        if isinstance(knowledge, dict):

            return knowledge

        #
        # Canonical runtime dataset
        #

        return {
            "dataset": knowledge,
            "graph": knowledge.graph,
            "facts": knowledge.facts,
            "records": knowledge.records,
        }
