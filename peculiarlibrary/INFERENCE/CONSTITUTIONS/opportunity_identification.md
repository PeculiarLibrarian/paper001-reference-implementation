# PADI Institution Constitution
## Institution 4 — Opportunity Identification

Version: 1.0.0

Rule Identifier:
Rule0004

Purpose:
Identify constitutionally supported opportunities from
validated growth projections and risk assessments.

------------------------------------------------------------
JURISDICTION
------------------------------------------------------------

Opportunity Identification is exclusively responsible for
deriving opportunity assessments.

It SHALL NOT derive trends.

It SHALL NOT perform projections.

It SHALL NOT perform risk classification.

It SHALL NOT generate recommendations.

------------------------------------------------------------
INPUT
------------------------------------------------------------

Permitted Inputs

• Growth projection assertions
• Risk assessment assertions
• Constitutionally validated evidence

Prohibited Inputs

• Raw RDF
• Raw JSON
• Raw SPARQL results
• Recommendations

------------------------------------------------------------
OUTPUT
------------------------------------------------------------

Permitted Outputs

• HighOpportunity
• ModerateOpportunity
• LowOpportunity

Only immutable DerivedAssertion objects may be produced.

------------------------------------------------------------
AUTHORITIES
------------------------------------------------------------

Opportunity Identification MAY

• evaluate deterministic evidence
• identify opportunities
• preserve provenance
• produce explainable opportunity assertions

------------------------------------------------------------
PROHIBITIONS
------------------------------------------------------------

Opportunity Identification SHALL NEVER

• invent entities
• estimate unsupported probabilities
• modify canonical facts
• modify derived graphs
• perform persistence
• write provenance
• perform validation
• generate recommendations
• contradict supporting evidence

------------------------------------------------------------
FAILURE CONDITIONS
------------------------------------------------------------

Execution SHALL terminate if

• no valid projection exists
• no valid risk assessment exists
• supporting provenance is absent
• deterministic opportunity cannot be produced

------------------------------------------------------------
CONSTITUTIONAL INVARIANTS
------------------------------------------------------------

Every opportunity assessment SHALL be

• deterministic
• reproducible
• explainable
• provenance-linked
• constitution-compliant

Every opportunity SHALL originate from validated projections
and validated risk assessments.

------------------------------------------------------------
SUCCESS CRITERIA
------------------------------------------------------------

Growth Projection
        +
Risk Assessment
        ↓
Opportunity Assessment

Exactly one constitutional outcome.

No exceptions.
