# Finance Collection Specification

Version: 1.0

---

# Purpose

The Finance Collection is a semantic knowledge collection dedicated to representing financial knowledge using W3C Semantic Web standards.

It is one collection within the Peculiar Librarian ecosystem.

This repository models finance only.

---

# Scope

The Finance Collection represents:

- Companies
- Financial Statements
- Financial Metrics
- Reporting Periods
- Market Observations
- Corporate Actions
- Citations
- Provenance

It does not perform forecasting.

It does not execute trades.

It does not make investment decisions.

It represents financial knowledge.

---

# Semantic Standards

| Layer | Standard |
|--------|----------|
| Meaning | OWL |
| Knowledge | RDF |
| Vocabulary | SKOS |
| Validation | SHACL |
| Queries | SPARQL |
| Publication | JSON-LD |

---

# Core Semantic Entities

The Finance Collection models the following entities.

## Company

Examples

- Safaricom PLC
- Equity Group
- KCB Group

---

## Financial Statement

Examples

- Statement of Financial Position
- Income Statement
- Cash Flow Statement

---

## Financial Metric

Examples

- Revenue
- Operating Profit
- Net Profit
- Earnings Per Share
- Free Cash Flow
- Total Assets
- Total Liabilities
- Equity

---

## Reporting Period

Examples

- FY2025
- H1 2026
- Q3 2027

---

## Observation

An observation represents one measured financial fact.

Examples

Revenue for FY2025

EPS for FY2025

Operating Profit for FY2025

---

## Citation

Every observation must be traceable to an authoritative source.

Examples

Annual Report

Audited Financial Statements

Exchange Filing

---

## Provenance

Every observation records:

- source
- publication date
- reporting period
- compiler
- confidence
- validation status

---

# Collection Boundaries

Included

✓ Public company financial reporting

✓ Corporate disclosures

✓ Audited statements

✓ Regulatory filings

✓ Market data

Excluded

✗ Investment advice

✗ Trading strategies

✗ Portfolio optimisation

✗ Predictive models

✗ Machine learning outputs

---

# Canonical Principle

Every financial fact is represented exactly once.

Derived knowledge must reference canonical observations.

No duplication.

---

# Knowledge Lifecycle

Research

↓

Ontology

↓

Observation

↓

Validation

↓

Publication

Knowledge always flows forward.

---

# Extension Policy

The Finance Collection grows by adding:

- companies
- observations
- reports
- metrics
- vocabularies
- queries

The semantic architecture remains unchanged.

---

# Mission

The Finance Collection exists to preserve financial knowledge with semantic precision, interoperability and provenance.

It is a knowledge collection.

Nothing more.

Nothing less.

