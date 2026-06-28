# Finance Collection Knowledge Graph

Portfolio
    ├── owns → Position
    ├── contains → Cash
    ├── follows → Investment Policy
    └── applies → Strategy

Position
    ├── references → Security
    └── contributes_to → Risk

Security
    ├── listed_on → Exchange
    ├── belongs_to → Market
    ├── generates → Dividend
    └── affected_by → Corporate Action

Order
    ├── targets → Security
    └── produces → Trade

Trade
    └── creates → Position

Market Observation
    ├── describes → Market
    └── provides → Evidence

Evidence
    └── supports → Recommendation

Recommendation
    └── identifies → Opportunity

Opportunity
    └── satisfies → Investment Policy

Strategy
    └── evaluates → Opportunity

Risk
    └── constrains → Capital Allocation

Capital Allocation
    └── modifies → Portfolio

Exchange
    └── operates_within → Market

