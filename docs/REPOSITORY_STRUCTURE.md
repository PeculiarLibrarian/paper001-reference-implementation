# Repository Structure

Version: 1.0

---

# Purpose

This document defines the canonical layout of the Peculiar Librarian repository.

The repository mirrors the semantic pipeline.

Every directory has exactly one responsibility.

---

# Canonical Repository

```
schemas/

    finance/

        ontology/

        knowledge/

        taxonomy/

        shapes/

        queries/

        publication/
```

Nothing outside this structure is considered part of the semantic knowledge model.

---

# ontology/

Standard

OWL

Purpose

Defines semantic meaning.

Contains

- Classes
- Object Properties
- Datatype Properties
- Restrictions
- Ontology Metadata

Never contains observations.

---

# knowledge/

Standard

RDF

Purpose

Stores canonical financial knowledge.

Contains

- Companies
- Reports
- Statements
- Metrics
- Observations
- Citations
- Provenance

This directory is the canonical knowledge graph.

---

# taxonomy/

Standard

SKOS

Purpose

Defines controlled vocabularies.

Contains

- Concept Schemes
- Preferred Labels
- Alternative Labels
- Definitions
- Authorities

Never stores observations.

---

# shapes/

Standard

SHACL

Purpose

Validates RDF knowledge.

Contains

- Node Shapes
- Property Shapes
- Graph Constraints

Shapes never modify data.

---

# queries/

Standard

SPARQL

Purpose

Retrieves semantic knowledge.

Contains

- Analytics
- Discovery Queries
- Navigation Queries
- Reporting Queries

Queries are read-only.

---

# publication/

Standard

JSON-LD

Purpose

Publishes interoperable knowledge.

Contains

- Contexts
- Export Profiles
- JSON-LD Templates
- Linked Data Documents

Publication is derived from RDF.

---

# Repository Rules

Every semantic artifact belongs to one directory.

Example

OWL

↓

ontology/

RDF

↓

knowledge/

SKOS

↓

taxonomy/

SHACL

↓

shapes/

SPARQL

↓

queries/

JSON-LD

↓

publication/

---

# Forbidden Structures

The following are prohibited:

- mixed semantic standards inside one directory;
- RDF inside ontology/;
- OWL inside knowledge/;
- SHACL inside taxonomy/;
- JSON-LD inside knowledge/.

---

# Naming Principles

Every artifact should describe exactly one semantic concern.

Prefer

```
financial_metrics.ttl

companies.ttl

dividend_observations.ttl
```

Avoid

```
everything.ttl

misc.ttl

finance_data.ttl
```

---

# Growth Policy

As the finance collection grows:

Directories remain unchanged.

Only semantic artifacts increase.

The repository scales by adding knowledge rather than redesigning infrastructure.

