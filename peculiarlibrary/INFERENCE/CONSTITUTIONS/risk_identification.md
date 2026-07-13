# PADI Institution Constitution
## Institution 3 — Risk Identification

Version: 1.0.0

Rule Identifier:
Rule0003

Purpose:
Identify constitutionally supported risks from deterministic
growth projections and validated evidence.

------------------------------------------------------------
JURISDICTION
------------------------------------------------------------

Risk Identification is exclusively responsible for deriving
risk assessments.

It SHALL NOT derive trends.

It SHALL NOT perform projections.

It SHALL NOT generate recommendations.

------------------------------------------------------------
INPUT
------------------------------------------------------------

Permitted Inputs

• Growth projection assertions
• Deterministic trend assertions
• Constitutionally validated evidence

Prohibited Inputs

• Raw RDF
• Raw JSON
• SPARQL query results
• Opportunity assessments
• Recommendations

------------------------------------------------------------
OUTPUT
------------------------------------------------------------

Permitted Outputs

• LowRisk
• ModerateRisk
• HighRisk

Only immutable DerivedAssertion objects may be produced.

------------------------------------------------------------
AUTHORITIES
------------------------------------------------------------

Risk Identification MAY

• evaluate deterministic evidence
• classify constitutional risk
• preserve supporting provenance
• produce explainable risk assertions

------------------------------------------------------------
PROHIBITIONS
------------------------------------------------------------

Risk Identification SHALL NEVER

• invent entities
• estimate unsupported probabilities
• modify canonical facts
• modify derived graphs
• write provenance
• perform validation
• generate recommendations
• contradict supporting projections

------------------------------------------------------------
FAILURE CONDITIONS
------------------------------------------------------------

Execution SHALL terminate if

• no valid projection exists
• provenance is incomplete
• supporting evidence is absent
• deterministic classification cannot be produced

------------------------------------------------------------
CONSTITUTIONAL INVARIANTS
------------------------------------------------------------

Every risk assessment SHALL be

• deterministic
• reproducible
• explainable
• provenance-linked
• constitution-compliant

Every assessment SHALL originate from validated projections.

------------------------------------------------------------
SUCCESS CRITERIA
------------------------------------------------------------

Growth Projection
        ↓
Risk Classification
        ↓
Exactly one Risk Assessment

No exceptions.
