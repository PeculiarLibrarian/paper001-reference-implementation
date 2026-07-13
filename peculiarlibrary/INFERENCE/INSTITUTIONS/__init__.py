"""
PADI Inference Rule Package
Version: 1.0.0

This package contains executable implementations of
constitutionally approved inference institutions.

Each module SHALL implement exactly one inference institution.

Institution Order

1. Trend Detection
2. Growth Projection
3. Risk Identification
4. Opportunity Identification
5. Recommendation Generation

Rule modules SHALL NEVER:

• modify canonical facts
• invent entities
• bypass provenance
• bypass constitutional validation

The inference engine orchestrates execution.

Individual rule modules only implement deterministic logic.
"""
