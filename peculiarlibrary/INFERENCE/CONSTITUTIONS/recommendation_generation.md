# PADI Institution Constitution
## Institution 5 — Recommendation Generation

Version: 1.0.0

Rule Identifier:
Rule0005

Purpose:
Produce constitutionally governed recommendations from
validated opportunity assessments.

------------------------------------------------------------
JURISDICTION
------------------------------------------------------------

Recommendation Generation is exclusively responsible for
deriving decision-support recommendations.

It SHALL NOT derive trends.

It SHALL NOT perform projections.

It SHALL NOT perform risk assessments.

It SHALL NOT perform opportunity identification.

------------------------------------------------------------
INPUT
------------------------------------------------------------

Permitted Inputs

• Opportunity assessment assertions
• Constitutionally validated supporting evidence

Prohibited Inputs

• Raw RDF
• Raw JSON
• Raw SPARQL results
• Canonical observations

------------------------------------------------------------
OUTPUT
------------------------------------------------------------

Permitted Outputs

• RecommendInvest
• RecommendMonitor
• RecommendAvoid

Only immutable DerivedAssertion objects may be produced.

Recommendations are advisory only.

------------------------------------------------------------
AUTHORITIES
------------------------------------------------------------

Recommendation Generation MAY

• evaluate validated opportunities
• derive deterministic recommendations
• preserve supporting provenance
• produce explainable decision-support assertions

------------------------------------------------------------
PROHIBITIONS
------------------------------------------------------------

Recommendation Generation SHALL NEVER

• invent entities
• modify canonical facts
• modify derived graphs
• overwrite previous recommendations
• perform persistence
• write provenance
• perform validation
• contradict supporting opportunity assessments

------------------------------------------------------------
FAILURE CONDITIONS
------------------------------------------------------------

Execution SHALL terminate if

• no valid opportunity assessment exists
• supporting provenance is incomplete
• deterministic recommendation cannot be produced

------------------------------------------------------------
CONSTITUTIONAL INVARIANTS
------------------------------------------------------------

Every recommendation SHALL be

• deterministic
• reproducible
• explainable
• provenance-linked
• constitution-compliant

Recommendations SHALL remain advisory and SHALL NOT alter
canonical knowledge.

------------------------------------------------------------
SUCCESS CRITERIA
------------------------------------------------------------

Opportunity Assessment
        ↓
Recommendation Logic
        ↓
Exactly one Recommendation

No exceptions.
