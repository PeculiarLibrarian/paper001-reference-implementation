# Peculiar Librarian Kernel Specification (v1.0)

## Purpose

The Peculiar Librarian Kernel is the semantic infrastructure responsible for discovering, validating, compiling, and publishing knowledge collections.

It never owns domain knowledge.

It provides the machinery that allows collections to become discoverable, trustworthy, and interoperable.

---

# Kernel Architecture

```
kernel/

    discovery/

    validation/

    modeling/

    publication/

    orchestration/
```

Each module has exactly one responsibility.

---

# Discovery

## Responsibility

Locate semantic collections.

Discover their artifacts.

Load collection metadata.

### Components

- CollectionLoader
- ArtifactCatalog

---

# Validation

## Responsibility

Protect semantic integrity.

Validation never modifies knowledge.

It only verifies conformance.

### Components

- CollectionContract
- Future Shape Validators

---

# Modeling

## Responsibility

Convert structured research facts into canonical knowledge models.

### Components

- FinancialObservation
- FinancialObservationFactory
- KnowledgeCompiler
- ObservationCollectionBuilder

Modeling owns no publication logic.

---

# Publication

## Responsibility

Expose canonical knowledge through multiple endpoints.

Canonical knowledge is never modified.

Publishers only transform representation.

### Current Endpoints

- RDF
- JSON-LD
- CSV
- GraphDB
- SPARQL Endpoint
- REST API

Future publication targets may be added without modifying the modeling layer.

---

# Orchestration

## Responsibility

Coordinate the complete pipeline.

The librarian orchestrates.

It does not reason.

It does not own knowledge.

It does not perform domain inference.

---

# Canonical Pipeline

```
Research

↓

Notebook LM

↓

Structured Facts

↓

Observation Factory

↓

Observation

↓

Knowledge Compiler

↓

Observation Collection Builder

↓

Canonical Knowledge

↓

Publishers

├── RDF
├── JSON-LD
├── CSV
├── GraphDB
├── SPARQL Endpoint
└── REST API
```

---

# Governing Principle

The canonical representation is the Observation model.

Everything else is a publication format.

```
Observation

↓

Knowledge

↓

Publication
```

No publisher may become the source of truth.

---

# Extension Rules

A new collection must never require kernel modification.

Adding a new domain should require only:

- ontology
- taxonomy
- shapes
- queries
- knowledge

The kernel remains unchanged.

---

# Semantic Authorities

Authorities define controlled vocabularies.

Current authorities include:

- Financial Metrics
- Financial Statements
- Reporting Periods
- Reporting Scopes
- Scales
- Observation Status
- Observation Confidence
- Citations
- Authority

Collections may introduce additional authorities without altering the kernel.

---

# Design Principles

- Knowledge is separate from infrastructure.
- Infrastructure is separate from orchestration.
- Publication is separate from modeling.
- Validation is independent of publication.
- Every module has one responsibility.
- Every semantic distinction is explicit.

---

# Stability Policy

The kernel is versioned independently of collections.

Collections may evolve continuously.

Kernel evolution requires explicit specification changes and version increments.

Kernel compatibility is considered a long-term commitment.

---

# Mission

The Peculiar Librarian Kernel exists to preserve, organize, validate, compile, and publish knowledge.

It is not a finance engine.

It is not a reasoning engine.

It is semantic infrastructure upon which knowledge collections are built.
