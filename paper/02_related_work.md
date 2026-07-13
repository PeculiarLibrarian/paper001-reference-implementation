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

