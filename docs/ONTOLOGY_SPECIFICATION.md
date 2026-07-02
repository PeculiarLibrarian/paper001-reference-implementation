# Finance Ontology Specification

Version: 1.0

---

# Purpose

The Finance Ontology defines the meaning of every concept within the Finance Collection.

It is the semantic authority of the repository.

Every other layer derives from this ontology.

---

# Semantic Hierarchy

Meaning

↓

Knowledge

↓

Vocabulary

↓

Validation

↓

Query

↓

Publication

---

# W3C Stack

Ontology
→ OWL

Knowledge
→ RDF

Vocabulary
→ SKOS

Validation
→ SHACL

Query
→ SPARQL

Publication
→ JSON-LD

---

# Responsibilities

The ontology defines:

- classes
- object properties
- datatype properties
- semantic relationships
- constraints that describe reality

The ontology never stores observations.

---

# Canonical Classes

At minimum, the ontology defines:

Company

FinancialStatement

FinancialMetric

Observation

ReportingPeriod

Citation

Authority

Unit

Currency

Scale

Confidence

ValidationStatus

---

# Canonical Relationships

Examples include:

Company
hasObservation
Observation

Observation
measures
FinancialMetric

Observation
reportedFor
ReportingPeriod

Observation
hasCitation
Citation

Observation
usesUnit
Unit

Observation
usesCurrency
Currency

Observation
hasConfidence
Confidence

Observation
validatedBy
ValidationStatus

---

# Design Principles

The ontology describes meaning.

It never stores values.

For example

Revenue

belongs in OWL.

Revenue = 388.7 Billion

belongs in RDF.

---

# Stability

Ontology evolution must preserve semantic compatibility.

Existing knowledge should not become invalid after ontology upgrades.

Breaking semantic changes require version increments.

---

# Versioning

Every ontology release must include:

version identifier

release date

change summary

compatibility statement

---

# Dependency Model

Everything depends on the ontology.

OWL

↓

RDF

↓

SKOS

↓

SHACL

↓

SPARQL

↓

JSON-LD

No layer may redefine ontology concepts.

---

# Mission

The ontology provides the semantic foundation upon which the Finance Collection is built.

