# Canonical Facts Contract (L0)

## Purpose

The `canonical_facts.json` artifact represents the **Canonical Observation Ledger (L0)** of the architecture.

It is the immutable genesis dataset produced from source documents through explicit extraction. Its purpose is to preserve source-faithful observations with complete provenance before any semantic interpretation, inference, normalization, or knowledge synthesis occurs.

L0 establishes the epistemic foundation of the system.

The contract prioritizes:

- lexical faithfulness,
- explicit observation,
- verifiable provenance,
- reproducibility,
- separation of factual records from derived knowledge.

---

# Canonical Facts Schema

Each `canonical_facts.json` file SHALL conform to the following structure:

```json
{
  "facts": [
    {
      "subject": "Exact name of the entity as identified in the source document",
      "predicate": "canonical_reporting_term",
      "object": "Literal extracted value",
      "unit": "Explicit unit of measure or null",
      "period": "Reporting period (example: FY2025)",
      "confidence": 1.0,
      "source": {
        "document": "filename.pdf",
        "page": 0,
        "section": "Verbatim source section title",
        "context": "Original lexical snippet containing the extracted fact"
      }
    }
  ]
}
L0 Contract Rules
1. Immutability
Once a canonical_facts.json artifact has been generated, it becomes a permanent record of the observations extracted from the source corpus.
Downstream systems SHALL NOT modify, rewrite, enrich, normalize, or correct L0 records.
Any derived interpretation MUST exist outside the L0 artifact.
2. Lexical Faithfulness
The extracted fact MUST represent what the source document explicitly states.
Extraction SHALL NOT introduce:
assumptions,
calculations,
semantic interpretations,
inferred relationships,
external knowledge.
The following fields must preserve source fidelity:
object
unit
period
source.context
The context field SHALL contain the original lexical evidence supporting the extracted observation.
3. Provenance Anchoring
Every fact MUST be independently verifiable through its provenance metadata.
Each observation SHALL contain:
{
  "document": "source filename",
  "page": "source page number",
  "section": "source section title",
  "context": "supporting lexical evidence"
}
A reviewer should be able to locate and verify every fact without requiring external interpretation.
4. Predicate Vocabulary
The schema remains invariant across organizations.
The predicate vocabulary is intentionally evolvable.
Common reporting terms SHOULD be reused where the meaning is equivalent:
Examples:
turnover
revenue
ebitda
operating_profit
board_approval_date
Organization-specific or industry-specific observations MAY introduce new predicates:
Examples:
mpesa_capacity_tps
specific_net_co2_emissions
monetary_gain_ias29
Predicate selection belongs to the extraction layer and reflects the reporting language of the source material.
5. Subject Identity
The subject field SHALL preserve the entity name as identified in the source document.
L0 SHALL NOT perform:
entity merging,
corporate hierarchy resolution,
ownership inference,
alias reconciliation.
Different names remain distinct observations until semantic processing occurs downstream.
6. Confidence
L0 confidence represents extraction certainty.
For verified source extraction:
"confidence": 1.0
Confidence does not represent business importance, prediction probability, or analytical certainty.
It represents confidence that the extracted observation accurately reflects the source document.
Layer Separation
L0 — Canonical Observation Layer
Responsibilities:
extract explicit facts,
preserve provenance,
maintain source fidelity,
create immutable genesis records.
Artifacts:
DATA/
├── canonical_facts_template.json
├── canonical_facts_contract.md
└── organization/
    └── canonical_facts.json
Semantic Processing Layers
Downstream layers are responsible for:
semantic mapping,
entity resolution,
ontology alignment,
RDF materialization,
inference,
analytical interpretation.
These operations MUST NOT alter the original L0 dataset.
Architectural Principle
The system follows the principle:
Facts are observed. Knowledge is constructed.
canonical_facts.json records what was found.
Higher layers determine what those observations mean, how they relate, and what can be derived from them.
The integrity of all downstream knowledge depends on the integrity of this L0 contract. EOF
