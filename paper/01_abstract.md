# Abstract

This paper presents the Peculiar Library, a deterministic provenance-enforced knowledge graph architecture for canonical enterprise information extraction and semantic validation.

The architecture separates semantic definitions from implementation logic by expressing canonical knowledge using W3C Semantic Web standards, including RDF, OWL 2, SKOS, and SHACL. Rather than embedding validation semantics within application code, structural constraints are represented declaratively and evaluated using standards-compliant validation engines.

The evaluation consists of three reproducible experiments. First, ontology and vocabulary artifacts are validated for syntactic correctness using Apache Jena RIOT. Second, a materialized enterprise knowledge graph is validated against the SHACL constraint library using Apache Jena SHACL, demonstrating structural conformance. Third, an adversarial graph containing a deliberately removed provenance relationship is generated deterministically and shown to be rejected by the same validation framework.

The results demonstrate that provenance integrity can be specified declaratively and evaluated independently of the runtime implementation. All experiments are distributed as executable scripts with automated assertions to support independent reproduction through the archived Paper 001 reference implementation.

