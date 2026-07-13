# PADI Institution Constitution
## Institution 1 — Trend Detection

Version: 1.0.0

------------------------------------------------------------
JURISDICTION
------------------------------------------------------------

Trend Detection is the first constitutional reasoning
institution.

Its exclusive responsibility is to derive deterministic trend
assertions from ordered canonical observations.

No other institution may derive trends.

------------------------------------------------------------
INPUT
------------------------------------------------------------

The institution SHALL ONLY consume:

• Ordered Observation objects

The institution SHALL NEVER consume:

• Raw RDF
• Raw JSON
• SPARQL results
• Derived assertions
• Recommendations

------------------------------------------------------------
OUTPUT
------------------------------------------------------------

The institution SHALL ONLY produce immutable
DerivedAssertion objects.

Permitted conclusions:

• PositiveTrend
• NegativeTrend
• StableTrend

No other semantic conclusions are permitted.

------------------------------------------------------------
AUTHORITIES
------------------------------------------------------------

Trend Detection SHALL:

• Compare observations chronologically.
• Produce exactly one trend per entity/metric group.
• Preserve supporting fact identifiers.
• Produce deterministic output.

------------------------------------------------------------
PROHIBITIONS
------------------------------------------------------------

Trend Detection SHALL NEVER:

• Forecast future values.
• Estimate probabilities.
• Create entities.
• Modify canonical observations.
• Modify derived graphs.
• Write provenance.
• Perform persistence.
• Perform validation.

------------------------------------------------------------
FAILURE CONDITIONS
------------------------------------------------------------

Execution SHALL terminate if:

• Fewer than two observations exist.
• Observations cannot be ordered.
• Supporting fact identifiers are missing.
• Observation values cannot be compared.

------------------------------------------------------------
CONSTITUTIONAL INVARIANTS
------------------------------------------------------------

Every produced trend SHALL be:

• deterministic
• reproducible
• explainable
• provenance-linked

Trend Detection SHALL NEVER contradict canonical facts.

------------------------------------------------------------
SUCCESS CRITERIA
------------------------------------------------------------

For every valid observation sequence:

Observation
        ↓
Chronological Ordering
        ↓
Comparison
        ↓
Exactly one constitutional trend

No exceptions.
