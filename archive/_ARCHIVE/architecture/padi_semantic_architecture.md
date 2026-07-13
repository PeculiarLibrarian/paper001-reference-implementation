# PADI Semantic Architecture
Version: 1.0.0
Status: Canonical Architecture

---

# Foundational Principle

Knowledge is the asset.

Graphs are implementations.

Everything inside Peculiar Librarian exists to faithfully materialize canonical knowledge into deterministic semantic representations.

---

# Layered Architecture

Layer 0

PADI Kernel

Responsibilities

- Identity Resolution
- Namespace Registry
- URI Policy
- Deterministic Hashing
- Semantic Contracts
- Graph Contracts
- Execution Contracts

The Kernel contains NO domain knowledge.

---

Layer 1

Canonical Library

Responsibilities

- Curate knowledge
- Preserve documents
- Preserve canonical facts

Artifacts

- canonical_facts.json
- documents/
- media/
- metadata/

The Library is the single source of truth.

Nothing writes back into the Library.

---

Layer 2

Semantic Library

Responsibilities

- Ontology
- SKOS
- SHACL
- JSON-LD Context
- SPARQL Templates

The Semantic Library defines vocabulary only.

It contains no business facts.

---

Layer 3

Semantic Materializer

Responsibilities

- Resolve identities
- Construct semantic resources
- Materialize RDF

The Materializer never performs reasoning.

---

Layer 4

Knowledge Graph

Contains

- Canonical Facts
- Source Records
- Entity relationships
- Domain vocabulary

The graph is deterministic.

Running the Materializer twice produces an identical graph.

---

Layer 5

Intelligence

Responsibilities

- Reasoning
- Inference
- Validation
- Constraint Enforcement

Reasoning never modifies canonical knowledge.

Validation never repairs data.

---

Layer 6

Execution

Responsibilities

- SPARQL
- APIs
- Semantic Search
- AI Retrieval

Execution is read-only.

---

# Canonical Fact Contract

One canonical JSON record SHALL produce exactly one CanonicalFact resource.

Every CanonicalFact SHALL contain

- aboutEntity
- hasMetric
- hasValue
- hasPeriod
- hasUnit
- confidence
- hasSource

---

# Source Contract

Every CanonicalFact SHALL reference exactly one SourceRecord.

Every SourceRecord SHALL reference exactly one SourceDocument.

---

# Identity Doctrine

Everything reusable becomes a semantic resource.

Examples

Entity

Metric

ReportingPeriod

Unit

Document

CanonicalFact

SourceRecord

Primitive measurements remain RDF literals.

---

# Deterministic Identity

Every semantic resource SHALL possess a deterministic identity.

Identity generation SHALL be reproducible.

Random identifiers are prohibited.

---

# Compiler Doctrine

The compiler SHALL be implemented as a Semantic Materializer.

Responsibilities

- Identity Resolution
- Semantic Construction
- Graph Materialization

The compiler SHALL NOT perform reasoning.

---

# Reasoning Doctrine

The Reasoner SHALL generate new semantic observations.

The Reasoner SHALL preserve provenance.

The Reasoner SHALL NOT modify canonical knowledge.

---

# Validation Doctrine

Validation SHALL verify semantic integrity.

Validation SHALL NOT mutate graphs.

---

# Audit Doctrine

Audit SHALL record provenance.

Audit SHALL NEVER generate business knowledge.

---

# Execution Doctrine

Queries SHALL NEVER modify state.

Execution SHALL be isolated from materialization.

---

# System Invariant

Canonical Library

↓

Semantic Materializer

↓

Knowledge Graph

↓

Reasoner

↓

Validator

↓

Audit

↓

Execution

No component may bypass this lifecycle.

---

# Architectural Invariant

Knowledge is immutable.

Identity is deterministic.

Semantics are explicit.

Graphs are reproducible.

