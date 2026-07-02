# Semantic Pipeline Specification

Version: 1.0

---

# Purpose

The Peculiar Librarian represents financial knowledge through a deterministic semantic pipeline.

Each stage transforms knowledge without altering the responsibilities of any other stage.

The pipeline is linear.

Each stage has one responsibility.

---

# Canonical Pipeline

```
Research
    │
    ▼
OWL
    │
    ▼
RDF
    │
    ▼
SKOS
    │
    ▼
SHACL
    │
    ▼
SPARQL
    │
    ▼
JSON-LD
```

---

# Stage 1 — Research

Purpose

Collect authoritative financial information.

Examples

- Annual Reports
- Interim Reports
- Regulatory Filings
- Exchange Announcements
- Audited Statements

Outputs

Human knowledge.

This stage is outside the semantic system.

---

# Stage 2 — OWL

Standard

Web Ontology Language (OWL)

Purpose

Define meaning.

Responsibilities

- Classes
- Relationships
- Object Properties
- Datatype Properties
- Domain Constraints
- Range Constraints

Produces

Semantic model.

OWL never stores observations.

---

# Stage 3 — RDF

Standard

Resource Description Framework (RDF)

Purpose

Represent financial observations.

Responsibilities

- Companies
- Reports
- Statements
- Metrics
- Observations
- Citations
- Provenance

Produces

Canonical knowledge graph.

RDF is the source of truth.

---

# Stage 4 — SKOS

Standard

Simple Knowledge Organization System (SKOS)

Purpose

Standardize vocabulary.

Responsibilities

- Preferred Labels
- Alternative Labels
- Definitions
- Concept Schemes
- Authorities

Produces

Controlled vocabulary.

SKOS never models observations.

---

# Stage 5 — SHACL

Standard

Shapes Constraint Language (SHACL)

Purpose

Validate semantic integrity.

Responsibilities

- Required Properties
- Cardinality
- Datatypes
- Node Constraints
- Graph Constraints

Produces

Validation results.

SHACL never repairs data.

---

# Stage 6 — SPARQL

Standard

SPARQL Protocol and RDF Query Language

Purpose

Retrieve knowledge.

Responsibilities

- Discovery
- Analytics
- Navigation
- Semantic Retrieval

Produces

Knowledge views.

Queries never modify knowledge.

---

# Stage 7 — JSON-LD

Standard

JSON-LD

Purpose

Publish interoperable knowledge.

Responsibilities

- API Exchange
- Linked Data
- External Systems
- Web Integration

Produces

Portable semantic documents.

JSON-LD never becomes the source of truth.

---

# Pipeline Responsibilities

| Stage | Owns |
|--------|------|
| Research | Facts |
| OWL | Meaning |
| RDF | Knowledge |
| SKOS | Vocabulary |
| SHACL | Validation |
| SPARQL | Retrieval |
| JSON-LD | Publication |

---

# Canonical Source of Truth

The canonical representation is RDF.

Everything else exists to support, validate, retrieve or publish RDF.

```
Research

↓

OWL

↓

RDF ← Canonical Knowledge

↓

SKOS

↓

SHACL

↓

SPARQL

↓

JSON-LD
```

---

# Design Constraints

Every semantic artifact must belong to exactly one stage.

No stage may duplicate another.

Examples

Correct

OWL defines "Revenue".

RDF records Revenue for FY2025.

SKOS defines the preferred label "Revenue".

SHACL validates Revenue observations.

SPARQL retrieves Revenue observations.

JSON-LD publishes Revenue observations.

Incorrect

OWL stores Revenue values.

SKOS stores financial statements.

SHACL defines ontology classes.

SPARQL validates graphs.

JSON-LD becomes canonical storage.

---

# Acceptance Criteria

The semantic pipeline is complete when:

✓ OWL defines meaning.

✓ RDF stores observations.

✓ SKOS standardizes terminology.

✓ SHACL validates knowledge.

✓ SPARQL retrieves knowledge.

✓ JSON-LD publishes knowledge.

Each layer performs exactly one responsibility.

