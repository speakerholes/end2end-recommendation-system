---
title: Schema and Granularity
description: What a row means and how those records map to recommender-system entities.
---

# Schema and Granularity

Recommendation systems fail quietly when teams confuse row-level granularity. A review row is not the same thing as a user, a session, or an item impression. This section establishes the basic mapping.

## Review table semantics

At a high level, a review row should be treated as an **interaction event** between a user and an item. That makes it a plausible training source for implicit or explicit feedback tasks, depending on how labels are defined later.

Questions to answer during exploration:

- Which column uniquely identifies the user?
- Which column uniquely identifies the product?
- Does each row represent one final review or can duplicates exist?
- Are timestamps present and trustworthy enough for temporal splits?
- Which text, rating, or verified-purchase fields are available for feature design?

## Metadata table semantics

A metadata row should be treated as an **item-side feature source**. This is where tower inputs later come from:

- Category and taxonomy signals
- Title and description text
- Brand or seller features
- Price and merchandising context
- Structured attributes

## Recommender entity model

Even before modeling, it helps to frame the data as three conceptual objects:

| Entity | Likely source | Purpose |
| --- | --- | --- |
| User | Review data | Interaction history and user features |
| Item | Metadata data | Retrieval targets and item embeddings |
| Interaction | Review data | Supervision, sequence history, and evaluation events |

Once that mapping is validated against the actual columns, the project can move into feature contracts for a two-tower architecture.
