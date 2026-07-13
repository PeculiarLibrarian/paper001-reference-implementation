# PADI Institution Constitution Template

Version: 1.0.0

This document is the canonical template for every reasoning
institution within the PADI Inference Layer.

Every institution SHALL define every section below.

------------------------------------------------------------
INSTITUTION
------------------------------------------------------------

Institution Name:

Version:

Rule Identifier:

Purpose:

------------------------------------------------------------
JURISDICTION
------------------------------------------------------------

Define the exclusive semantic responsibility of the institution.

The institution SHALL NOT operate outside this jurisdiction.

------------------------------------------------------------
INPUT
------------------------------------------------------------

Permitted inputs.

Explicitly list prohibited inputs.

------------------------------------------------------------
OUTPUT
------------------------------------------------------------

Permitted outputs.

The institution SHALL produce only these outputs.

------------------------------------------------------------
AUTHORITIES
------------------------------------------------------------

Enumerate the operations the institution is constitutionally
authorized to perform.

------------------------------------------------------------
PROHIBITIONS
------------------------------------------------------------

Enumerate every operation that is constitutionally forbidden.

Examples include:

• entity creation
• hallucination
• persistence
• graph mutation
• validation
• provenance writing
• recommendation generation
• statistical estimation (unless explicitly authorized)

------------------------------------------------------------
FAILURE CONDITIONS
------------------------------------------------------------

Execution SHALL terminate when any constitutional precondition
is violated.

List every mandatory failure condition.

------------------------------------------------------------
CONSTITUTIONAL INVARIANTS
------------------------------------------------------------

Every output SHALL satisfy the required invariants.

Typical invariants include:

• deterministic
• reproducible
• explainable
• provenance-linked
• constitution-compliant

------------------------------------------------------------
SUCCESS CRITERIA
------------------------------------------------------------

Describe the expected execution path.

Recommended format:

Input
    ↓
Transformation
    ↓
Derived Output

Exactly one constitutional outcome for every valid execution.

------------------------------------------------------------
IMPLEMENTATION NOTES
------------------------------------------------------------

The Constitution governs behaviour.

Python implements behaviour.

When implementation and constitution disagree,
the Constitution prevails.

