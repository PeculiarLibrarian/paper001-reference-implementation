# PADI Control Plane Doctrine v1.0.0
## (Sovereign Architecture Specification)

---

# 1. Core Principle

The PADI system is a **single semantic operating system** expressed through three abstraction layers:

- **PADI** → Control Plane (Truth + Ontology + Constraints)
- **peculiarlibrary** → Execution Plane (Compiler + Transformation Engine)
- **peculiarlibrarian** → Operator Plane (Interface + Tooling + Observation)

These are not separate systems.
They are a single system with enforced separation of concerns.

---

# 2. Control Plane Definition (PADI)

## 2.1 Role
PADI is the **only source of semantic truth**.

It defines:
- Ontology classes
- Property semantics
- Domain invariants
- Alignment contracts
- Valid relationships

## 2.2 Rule of Sovereignty

> No execution layer is permitted to define or override meaning.

PADI is immutable at runtime.

---

# 3. Execution Plane Definition (peculiarlibrary)

## 3.1 Role
peculiarlibrary is the **deterministic compiler and execution substrate**.

It is responsible for:
- Mapping raw data → semantic commands
- Constructing RDF graphs
- Enforcing SHACL constraints
- Injecting alignment relationships
- Executing factory transformations

## 3.2 Constraint

Execution may ONLY:
- transform
- validate
- materialize

Execution may NEVER:
- redefine ontology
- redefine predicates
- redefine class semantics

---

# 4. Operator Plane Definition (peculiarlibrarian)

## 4.1 Role
The operator layer provides:
- CLI tools
- audits
- dependency inspection
- debugging utilities
- visualization of system state

## 4.2 Constraint

The operator layer is:
> observational and procedural only

It has no authority over semantic structure.

---

# 5. Layer Boundary Law

## 5.1 Hard Rule

| Layer | Allowed to Define Meaning? |
|------|---------------------------|
| PADI | YES |
| peculiarlibrary | NO |
| peculiarlibrarian | NO |

---

## 5.2 Direction of Dependency
PADI → peculiarlibrary → peculiarlibrarian

Reverse dependency is forbidden.

---

# 6. Semantic Integrity Rule

All valid system outputs must satisfy:

1. Ontology originates in PADI
2. Transformation occurs in peculiarlibrary
3. Observation occurs in peculiarlibrarian
4. No cross-layer semantic leakage is allowed

---

# 7. System Identity Assertion

This system is not a collection of scripts.

It is:

> A deterministic semantic compiler with a sovereign ontology kernel.

---

# 8. Enforcement Statement

Any violation of layer boundaries constitutes:

- architectural drift
- semantic corruption risk
- invalid compiler state

---

# 9. Final Doctrine Statement

> PADI is truth.  
> peculiarlibrary is transformation.  
> peculiarlibrarian is visibility.  

These roles are fixed, non-overlapping, and non-negotiable.

