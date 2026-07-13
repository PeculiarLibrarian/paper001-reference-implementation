# PADI Institution Constitution
## Institution 2 — Growth Projection

Version: 1.0.0

Rule Identifier:
Rule0002

Purpose:
Derive deterministic growth projection assertions from
constitutionally valid trend assertions.

------------------------------------------------------------
JURISDICTION
------------------------------------------------------------

Growth Projection is exclusively responsible for projecting
future directional growth from validated trends.

It SHALL NOT derive trends.

It SHALL NOT perform recommendations.

------------------------------------------------------------
INPUT
------------------------------------------------------------

Permitted Inputs

• Derived trend assertions
• Ordered observations (when constitutionally permitted)

Prohibited Inputs

• Raw RDF
• Raw JSON
• SPARQL query results
• Risk assessments
• Recommendations

------------------------------------------------------------
OUTPUT
------------------------------------------------------------

Permitted Outputs

• PositiveGrowthProjection
• NegativeGrowthProjection
• StableGrowthProjection

Only immutable DerivedAssertion objects may be produced.

------------------------------------------------------------
AUTHORITIES
------------------------------------------------------------

Growth Projection MAY

• consume deterministic trends
• project directional growth
• preserve supporting fact identifiers
• produce explainable projections

------------------------------------------------------------
PROHIBITIONS
------------------------------------------------------------

Growth Projection SHALL NEVER

• invent entities
• estimate unsupported probabilities
• modify canonical facts
• modify derived graphs
• write provenance
• validate inference
• produce recommendations
• contradict trend assertions

------------------------------------------------------------
FAILURE CONDITIONS
------------------------------------------------------------

Execution SHALL terminate if

• no trend assertion exists
• supporting provenance is absent
• input observations are unordered
• deterministic projection cannot be produced

------------------------------------------------------------
CONSTITUTIONAL INVARIANTS
------------------------------------------------------------

Every projection SHALL be

• deterministic
• reproducible
• explainable
• provenance-linked
• constitution-compliant

Every projection SHALL originate from an existing trend.

------------------------------------------------------------
SUCCESS CRITERIA
------------------------------------------------------------

Trend Assertion
        ↓
Projection Logic
        ↓
Exactly one Growth Projection

No exceptions.
