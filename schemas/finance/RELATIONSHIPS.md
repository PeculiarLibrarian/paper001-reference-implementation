# Finance Collection Relationship Authority

This document defines the canonical relationship vocabulary of the Finance Collection.

Every semantic artifact shall use only the relationships defined here.

---

issuesSecurity

Company → Security

Inverse

issuedBy

---

listedOn

Security → Exchange

Inverse

listsSecurity

---

operatesWithin

Exchange → Market

Inverse

containsExchange

---

belongsToSector

Company → Sector

---

domiciledIn

Company → Country

---

tradesInCurrency

Company → Currency

---

ownsPosition

Portfolio → Position

Inverse

ownedByPortfolio

---

referencesSecurity

Position → Security

---

targetsSecurity

Order → Security

---

producesTrade

Order → Trade

Inverse

generatedByOrder

---

createsPosition

Trade → Position

Inverse

createdByTrade

---

supportsRecommendation

Evidence → Recommendation

Inverse

supportedByEvidence

---

identifiesOpportunity

Recommendation → Opportunity

Inverse

identifiedByRecommendation

