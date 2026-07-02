# Peculiar Librarian Mission Specification

Version: 1.0

---

# Purpose

Peculiar Librarian exists to curate, preserve, validate, and publish finance knowledge using W3C Semantic Web standards.

The repository treats financial knowledge as a long-lived semantic asset rather than as application data.

---

# Mission

Build a canonical semantic representation of finance that is:

- Explicit
- Verifiable
- Interoperable
- Machine-readable
- Extensible

Every semantic artifact should contribute to this objective.

---

# Scope

The repository models finance exclusively.

Examples include:

- Companies
- Financial Statements
- Financial Metrics
- Corporate Actions
- Dividends
- Earnings
- Assets
- Liabilities
- Equity
- Cash Flows
- Reporting Periods
- Citations
- Provenance
- Measurement Units

---

# Repository Responsibilities

The repository is responsible for:

- defining finance ontologies;
- representing finance observations;
- maintaining controlled vocabularies;
- validating semantic integrity;
- publishing interoperable semantic knowledge;
- preserving provenance.

---

# Repository Non-Responsibilities

The repository is **not** responsible for:

- workflow orchestration;
- execution engines;
- runtime kernels;
- agent coordination;
- infrastructure management;
- generic semantic tooling.

These belong in independent repositories.

---

# Governing Principles

## Knowledge First

Knowledge is the primary product.

Infrastructure exists only to support knowledge.

---

## Explicit Semantics

Every concept must have an explicit semantic definition.

Implicit meaning is prohibited.

---

## Standards First

Every layer maps directly to an established W3C standard.

| Responsibility | Standard |
|----------------|----------|
| Ontology | OWL |
| Knowledge | RDF |
| Vocabulary | SKOS |
| Validation | SHACL |
| Queries | SPARQL |
| Publication | JSON-LD |

---

## Separation of Concerns

Each semantic layer has exactly one responsibility.

No layer should duplicate another.

---

## Canonical Representation

The RDF knowledge graph is the canonical source of truth.

All publications derive from it.

---

## Validation Before Publication

Knowledge must validate successfully before publication.

Publication never repairs invalid knowledge.

---

## Provenance Always

Every observation must have traceable provenance.

Knowledge without provenance is incomplete.

---

## Extensibility

New finance concepts should be introduced by extending semantic models rather than modifying infrastructure.

---

# Repository Philosophy

The repository behaves like a library.

Knowledge is:

- acquired;
- verified;
- catalogued;
- classified;
- indexed;
- validated;
- published;
- preserved.

---

# Long-Term Objective

Become a reference-quality finance semantic collection suitable for:

- knowledge graphs;
- semantic search;
- linked data publication;
- intelligent agents;
- machine reasoning;
- research preservation.

---

# Stability Policy

Semantic standards evolve slowly.

Knowledge evolves continuously.

Infrastructure changes only when necessary to support semantic correctness.

