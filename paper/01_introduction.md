# 1. Introduction

Enterprise knowledge graphs increasingly serve as the semantic foundation for information integration, governance, and decision support. Although modern graph technologies provide expressive modeling capabilities, many implementations continue to couple semantic meaning tightly with application logic, reducing interoperability and making independent validation difficult. This observation is situated within the Semantic Web literature and discussed in Section 2.

The Peculiar Library addresses this problem by separating semantic representation from runtime implementation. Canonical enterprise facts are represented using RDF and governed through declarative vocabularies expressed with OWL 2, SKOS, and SHACL. Validation is therefore defined by semantic specifications rather than implementation-specific code.

This paper presents the architecture of the Peculiar Library and evaluates its structural integrity using independently implemented Semantic Web tooling. The evaluation focuses on three questions:

1. Can the semantic artifacts be validated for syntactic correctness?
2. Do materialized knowledge graphs conform to the declared SHACL constraints?
3. Does the validation framework correctly reject structurally invalid provenance relationships?

The contribution of this paper is a deterministic provenance-enforced knowledge graph architecture whose structural integrity is specified using W3C Semantic Web standards and empirically validated through independent-implementation positive and adversarial experiments.

