from pathlib import Path
import json

from extract_intelligence_v2 import IntelligenceLayerV2


class IntelligenceFusionV3:

    def fuse(self, graph):

        intelligence = IntelligenceLayerV2().extract(graph)

        entity_model = intelligence["entity_field_model"]["entities"]
        relation_model = intelligence["relation_gravity_model"]["relations"]
        domain_model = intelligence["domain_signal_classifier"]["domains"]

        entity_strength = (
            max(e["signal_strength"] for e in entity_model)
            if entity_model else 0.0
        )

        relation_strength = (
            max(relation_model.values())
            if relation_model else 0.0
        )

        domain_strength = (
            max(domain_model.values())
            if domain_model else 0.0
        )

        intelligence_index = round(
            (
                entity_strength +
                relation_strength +
                domain_strength
            ) / 3.0,
            6
        )

        dominant_entity = max(
            entity_model,
            key=lambda e: e["signal_strength"]
        )["uri"]

        dominant_relation = max(
            relation_model,
            key=relation_model.get
        )

        dominant_domain = max(
            domain_model,
            key=domain_model.get
        )

        return {
            "intelligence": intelligence,
            "fusion": {
                "dominant_entity": dominant_entity,
                "dominant_relation": dominant_relation,
                "dominant_domain": dominant_domain,
                "graph_intelligence_index": intelligence_index,
                "graph_signature": {
                    "entity_strength": round(entity_strength, 6),
                    "relation_strength": round(relation_strength, 6),
                    "domain_strength": round(domain_strength, 6)
                }
            }
        }


if __name__ == "__main__":

    from peculiarlibrarian.engine.runtime.operator_runtime import OperatorRuntime

    rt = OperatorRuntime()

    result = rt.execute(
        "compile",
        {
            "dataset": "peculiarlibrary/datasets/safaricom/canonical_facts.json"
        }
    )

    fused = IntelligenceFusionV3().fuse(result["graph"])

    output_dir = Path("peculiarlibrary/intelligence")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "latest_intelligence.json"

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(fused, f, indent=2)

    print("\n🧠 INTELLIGENCE FUSION V3\n")
    print("Graph Intelligence Index:", fused["fusion"]["graph_intelligence_index"])
    print("Dominant Entity:", fused["fusion"]["dominant_entity"])
    print("Dominant Relation:", fused["fusion"]["dominant_relation"])
    print("Dominant Domain:", fused["fusion"]["dominant_domain"])
    print()
    print("Saved:", output_file)
