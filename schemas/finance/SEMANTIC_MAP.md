# Finance Collection Semantic Map

This document describes the conceptual relationships that govern the Finance Collection.

It precedes ontology implementation.

---

Portfolio

    owns

        Position

Portfolio

    contains

        Cash

Portfolio

    follows

        Investment Policy

Portfolio

    applies

        Strategy

Position

    references

        Security

Position

    contributes_to

        Risk

Security

    listed_on

        Exchange

Security

    belongs_to

        Market

Security

    generates

        Dividend

Security

    affected_by

        Corporate Action

Order

    targets

        Security

Order

    produces

        Trade

Trade

    creates

        Position

Market Observation

    describes

        Market

Market Observation

    provides

        Evidence

Evidence

    supports

        Recommendation

Recommendation

    identifies

        Opportunity

Opportunity

    satisfies

        Investment Policy

Risk

    constrains

        Capital Allocation

Capital Allocation

    modifies

        Portfolio

Strategy

    evaluates

        Opportunity

Exchange

    operates_within

        Market

