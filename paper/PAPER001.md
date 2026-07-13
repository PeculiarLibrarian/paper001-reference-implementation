# Paper 001

## Deterministic Provenance-Enforced Knowledge Graph Reference Implementation

**Samuel Muriithi Gitandu, B.S.**  
*Peculiar Librarian*  

Independent Researcher  
Nairobi, Kenya  

**ORCID**  
https://orcid.org/0009-0009-2784-9577

**Archived replication package (DOI)**  
https://doi.org/10.5281/zenodo.21341462

**Development repository**  
https://github.com/PeculiarLibrarian/paper001-reference-implementation

---
# Abstract

This paper presents the Peculiar Library, a deterministic provenance-enforced knowledge graph architecture for canonical enterprise information extraction and semantic validation.

The architecture separates semantic definitions from implementation logic by expressing canonical knowledge using W3C Semantic Web standards, including RDF, OWL 2, SKOS, and SHACL. Rather than embedding validation semantics within application code, structural constraints are represented declaratively and evaluated using standards-compliant validation engines.

The evaluation consists of three reproducible experiments. First, ontology and vocabulary artifacts are validated for syntactic correctness using Apache Jena RIOT. Second, a materialized enterprise knowledge graph is validated against the SHACL constraint library using Apache Jena SHACL, demonstrating structural conformance. Third, an adversarial graph containing a deliberately removed provenance relationship is generated deterministically and shown to be rejected by the same validation framework.

The results demonstrate that provenance integrity can be specified declaratively and evaluated independently of the runtime implementation. All experiments are distributed as executable scripts with automated assertions to support independent reproduction through the archived Paper 001 reference implementation.

# 1. Introduction

Enterprise knowledge graphs increasingly serve as the semantic foundation for information integration, governance, and decision support. Although modern graph technologies provide expressive modeling capabilities, many implementations continue to couple semantic meaning tightly with application logic, reducing interoperability and making independent validation difficult. This observation is situated within the Semantic Web literature and discussed in Section 2.

The Peculiar Library addresses this problem by separating semantic representation from runtime implementation. Canonical enterprise facts are represented using RDF and governed through declarative vocabularies expressed with OWL 2, SKOS, and SHACL. Validation is therefore defined by semantic specifications rather than implementation-specific code.

This paper presents the architecture of the Peculiar Library and evaluates its structural integrity using independently implemented Semantic Web tooling. The evaluation focuses on three questions:

1. Can the semantic artifacts be validated for syntactic correctness?
2. Do materialized knowledge graphs conform to the declared SHACL constraints?
3. Does the validation framework correctly reject structurally invalid provenance relationships?

The contribution of this paper is a deterministic provenance-enforced knowledge graph architecture whose structural integrity is specified using W3C Semantic Web standards and empirically validated through independent-implementation positive and adversarial experiments.

# 2. Related Work

Enterprise knowledge graphs are commonly constructed using Semantic Web technologies that provide standardized mechanisms for representing entities, relationships, controlled vocabularies, ontologies, and structural constraints. The Peculiar Library adopts these standards as the semantic foundation of its architecture rather than introducing a new knowledge representation language.

#

# 2.1 Resource Description Framework (RDF)

The Resource Description Framework (RDF) defines a graph-based data model for representing information as subject–predicate–object triples. RDF provides the common representation upon which higher semantic layers are constructed and enables interoperability between independently developed systems [@w3c-rdf11].

Within the Peculiar Library, canonical enterprise facts are materialized as RDF graphs that serve as the implementation-independent representation of extracted knowledge.

#

# 2.2 OWL 2

OWL 2 extends RDF with formally defined ontology constructs that enable explicit modeling of classes, properties, domains, ranges, identity constraints, and logical relationships [@w3c-owl2].

The reference implementation employs OWL 2 to define the semantic vocabulary governing enterprise entities while leaving runtime behaviour outside the ontology itself.

#

# 2.3 SHACL

The Shapes Constraint Language (SHACL) provides a declarative mechanism for expressing structural constraints over RDF graphs independently of application logic [@w3c-shacl].

Rather than embedding validation rules within procedural code, the Peculiar Library specifies graph integrity requirements as SHACL shapes evaluated by standards-compliant validation engines.

#

# 2.4 SKOS

The Simple Knowledge Organization System (SKOS) defines a standardized model for representing controlled vocabularies, concept hierarchies, and taxonomies [@w3c-skos].

The Peculiar Library employs SKOS to organize semantic concepts independently from executable runtime components, preserving clear separation between terminology management and knowledge materialization.

#

# 2.5 Provenance Representation

Provenance has long been recognized as a fundamental requirement for trustworthy information systems. The W3C PROV ontology provides a standardized vocabulary for representing derivation, attribution, and evidence relationships within semantic graphs [@w3c-prov].

The Peculiar Library builds upon these principles by requiring every canonical fact to preserve explicit provenance relationships throughout the materialization pipeline.

#

# 2.6 Architectural Separation

Previous Semantic Web standards primarily define representation, reasoning, and validation mechanisms rather than prescribing software architecture [@hitzler2020].

The Peculiar Library adopts a standards-based architectural approach in which semantic definitions, structural validation, runtime execution, and application services remain explicitly separated. Semantic meaning is therefore governed by declarative specifications rather than implementation-specific logic.

#

# 2.7 Positioning of This Work

This work does not propose new Semantic Web standards, ontology languages, or validation mechanisms.

Instead, it demonstrates how established W3C recommendations—including RDF, OWL 2, SKOS, SHACL, and PROV—can be integrated into a deterministic provenance-enforced enterprise knowledge graph architecture.

Accordingly, the primary contribution of this paper is architectural rather than linguistic: the design, implementation, and empirical validation of a standards-based semantic interoperability infrastructure whose structural integrity can be independently verified using existing Semantic Web tooling.

# 3. System Architecture

The Peculiar Library is a deterministic provenance-enforced knowledge graph architecture designed to separate semantic representation, validation, execution, and application concerns.

The architecture is organized around distinct semantic and operational layers.

#

# 3.1 Semantic Representation Layer

The semantic representation layer defines canonical enterprise knowledge using W3C Semantic Web standards.

RDF provides the graph representation model, while OWL 2 defines semantic classes and relationships. SKOS provides controlled vocabulary and concept organization mechanisms.

Canonical enterprise facts are represented independently from runtime execution logic, allowing semantic definitions to remain stable across implementation environments.

#

# 3.2 Constraint Validation Layer

Structural integrity is enforced through SHACL constraint definitions.

The validation layer specifies requirements such as:

- required provenance relationships,
- graph structure constraints,
- entity consistency requirements,
- semantic completeness conditions.

Validation is performed independently from the application runtime using standards-compliant tooling.

#

# 3.3 Runtime Execution Layer

The runtime layer processes canonical knowledge artifacts through deterministic execution workflows.

Runtime components are responsible for:

- loading semantic datasets,
- mapping canonical structures,
- executing inference workflows,
- materializing RDF representations.

The runtime consumes semantic definitions rather than embedding domain constraints directly into procedural logic.

#

# 3.4 Materialization and Verification Layer

The materialization layer produces validated knowledge graph artifacts from canonical inputs.

The verification framework evaluates the resulting artifacts through executable validation workflows. These workflows include syntax validation, positive structural validation, and adversarial validation.

This separation enables independent evaluation of semantic integrity without requiring inspection of internal implementation details.

#

# 3.5 Architectural Contribution

The contribution of the Peculiar Library is not a new Semantic Web language or validation standard.

Instead, it demonstrates an architecture in which established semantic standards are combined with deterministic verification workflows to create a reproducible provenance-enforced knowledge graph system.

# 4. Methodology

#

# 4.1 Evaluation Design

The evaluation is designed to assess the structural correctness of the Peculiar Library reference implementation using independently implemented Semantic Web tooling. Rather than measuring predictive performance, the experiments verify syntactic correctness, declarative constraint conformance, and deterministic rejection of structurally invalid knowledge graphs.

Three experiments comprise the evaluation:

1. Ontology syntax validation.
2. Positive SHACL validation.
3. Adversarial SHACL validation.

Each experiment executes deterministically from version-controlled artifacts.

#

# 4.2 Reference Environment

The evaluation was performed using Apache Jena 6.1.0 [@apache-jena], specifically:

- Apache Jena RIOT for RDF syntax validation.
- Apache Jena SHACL for declarative constraint validation.

Python 3.11 was used to execute the accompanying verification scripts included within the replication package.

#

# 4.3 Experiment 1 — Ontology Validation

The first experiment verifies that all semantic artifacts are syntactically valid RDF and OWL documents.

Apache Jena RIOT is executed against every ontology and vocabulary artifact distributed with the reference implementation.

The experiment succeeds only if every document parses successfully without syntax errors.

#

# 4.4 Experiment 2 — Positive SHACL Validation

The second experiment validates the canonical enterprise knowledge graph against the SHACL constraint library.

The graph is expected to satisfy every declared structural constraint.

Successful validation demonstrates that the materialization pipeline produces graphs conforming to the semantic specification.

#

# 4.5 Experiment 3 — Adversarial Validation

The third experiment evaluates the robustness of the constraint library.

A deterministic adversarial graph is generated by removing a mandatory provenance relationship from the canonical graph before validation.

The experiment succeeds only if the SHACL validator rejects the modified graph.

This demonstrates that structural provenance violations are detected independently of the runtime implementation.

#

# 4.6 Deterministic Execution

All experiments execute from version-controlled artifacts without manual intervention.

Each workflow specifies:

- deterministic inputs,
- deterministic execution order,
- deterministic expected outcomes.

No stochastic components participate in the evaluation.

#

# 4.7 Evaluation Criteria

The evaluation reports only structural correctness.

Measured outcomes are binary:

- PASS
- FAIL

No probabilistic measures or statistical inference are used.

#

# 4.8 Reproducibility

All experiments are distributed as executable scripts within the replication package.

Running the documented workflows from the tagged reference implementation is expected to produce identical experimental outcomes when executed in equivalent software environments.

# 5. Experimental Evaluation

The evaluation investigates whether the Peculiar Library reference implementation satisfies its declared semantic and structural integrity requirements.

Three experiments were executed using the documented verification workflows.

#

# 5.1 Experiment 1 — Ontology Syntax Validation

The first experiment validates the syntactic correctness of ontology and vocabulary artifacts.

Apache Jena RIOT is executed against the distributed semantic documents to verify that each artifact conforms to RDF parsing requirements.

#

## Result

All evaluated semantic artifacts successfully passed syntax validation.

#

# 5.2 Experiment 2 — Positive SHACL Validation

The second experiment evaluates whether the canonical enterprise knowledge graph conforms to the declared SHACL constraints.

The materialized graph is validated against the constraint library using Apache Jena SHACL.

#

## Result

The canonical graph successfully satisfies all declared structural constraints.

#

# 5.3 Experiment 3 — Adversarial SHACL Validation

The third experiment evaluates whether the validation framework detects deliberate structural corruption.

A deterministic adversarial graph is generated by removing a mandatory provenance relationship from the canonical graph.

The modified graph is then submitted to the same SHACL validation process.

#

## Result

The corrupted graph is rejected by the validator, demonstrating that provenance integrity constraints are actively enforced.

#

# 5.4 Evaluation Summary

The three experiments demonstrate:

- successful parsing of semantic artifacts,
- structural conformance of valid materialized graphs,
- deterministic detection of invalid provenance structures.

The results support the claim that declarative semantic constraints can be independently evaluated using standards-compliant Semantic Web tooling.

# 6. Reproducibility

All experiments reported in this paper are distributed as executable workflows within the accompanying reference implementation.

**Archived replication package (DOI)**

https://doi.org/10.5281/zenodo.21341462

**Development repository**

https://github.com/PeculiarLibrarian/paper001-reference-implementation

**Archived release**

paper001-v1.0.1

The replication package contains:

- Experiment 01 — RIOT syntax validation
- Experiment 02 — Positive SHACL validation
- Experiment 03 — Adversarial SHACL validation

Each experiment includes:

- executable scripts,
- deterministic inputs,
- documented expected outcomes,
- automated pass/fail assertions.

The adversarial experiment generates a corrupted graph deterministically by removing a mandatory provenance relationship before validation.

Only the documented verification artifacts and experimental workflows are used to support the evaluation reported in this paper; the remaining repository contents provide supporting implementation infrastructure and architectural documentation.

The archived Zenodo release (DOI: https://doi.org/10.5281/zenodo.21341462) constitutes the canonical replication package for this publication. The GitHub repository serves as the active development repository for subsequent revisions.

Running the documented workflows from the archived release in an equivalent software environment is expected to reproduce the experimental results reported in this paper.
# 7. Limitations

This work evaluates the structural integrity of the reference implementation using standards-compliant Semantic Web tooling.

The evaluation does not constitute a formal proof of correctness, completeness, or semantic equivalence.

Performance benchmarking, distributed execution, heterogeneous deployment environments, and large-scale production workloads remain outside the scope of this paper.

Similarly, the experiments validate structural provenance constraints rather than the factual correctness of enterprise information itself.

Future work will investigate larger datasets, distributed validation workflows, formal verification of selected architectural properties, and comparative evaluation against additional semantic validation frameworks.

# 8. Conclusion

This paper presented the Peculiar Library, a deterministic provenance-enforced knowledge graph architecture based on W3C Semantic Web standards.

The architecture separates semantic representation from implementation logic through RDF, OWL 2, SKOS, and SHACL while preserving implementation independence.

Three reproducible experiments demonstrated:

- syntactic correctness of the semantic artifacts,
- structural conformance of the materialized enterprise knowledge graph,
- successful rejection of deliberately corrupted provenance relationships.

These results show that declarative semantic constraints can be evaluated independently of the runtime implementation using standards-compliant validation engines.

The archived Paper 001 reference implementation provides executable experiments, automated verification procedures, and deterministic evaluation artifacts that enable independent reproduction of the reported results.

# References

The manuscript bibliography is maintained in `bibliography.bib` and contains the cited standards and academic references supporting the evaluation.

The primary references include:

- RDF 1.1 Concepts and Abstract Syntax — W3C Recommendation.
- OWL 2 Web Ontology Language — W3C Recommendation.
- Simple Knowledge Organization System (SKOS) Reference — W3C Recommendation.
- Shapes Constraint Language (SHACL) — W3C Recommendation.
- PROV-O: The PROV Ontology — W3C Recommendation.
- Apache Jena documentation and implementation resources.
- Hitzler, P., Krötzsch, M., Parsia, B., Patel-Schneider, P. F., & Rudolph, S. *Semantic Web for the Working Ontologist*. 2nd Edition. IOS Press, 2020.

The complete citation metadata is provided in `bibliography.bib`.

