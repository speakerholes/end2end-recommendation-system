---
title: Overview
description: Why the data section comes first in an end-to-end recommendation system build.
---

# Understanding the Data

This documentation starts with the data because recommendation quality is constrained by what the system can actually observe. Before retrieval models, embeddings, and serving strategies, you need to understand what counts as a user event, what identifies an item, and how reliably review data can be joined with product metadata.

The current codebase already reflects that priority. In `src/end2end_recommendation_system/data.py`, the project focuses on acquiring and loading the Amazon Reviews 2023 dataset from the McAuley Lab release on Hugging Face, then normalizing it into local Parquet assets for downstream analysis.

## Why this section exists

The first document set should answer four questions clearly:

1. What source assets do we have?
2. What entity does each row represent?
3. How do reviews and metadata connect?
4. What data quality checks should happen before modeling?

Those answers become the contract for every later section:

- Candidate generation depends on stable item identifiers and realistic interaction semantics.
- A two-tower model depends on well-defined user and item features.
- Offline evaluation depends on trustworthy train, validation, and test boundaries.
- Serving depends on the same schemas staying intact outside notebooks.

## Near-term expansion path

This site is intentionally structured so it can grow into a full recommender system narrative without a rewrite. The next major chapters can layer in:

- Interaction labeling and target design
- Feature engineering for user and item towers
- Retrieval model training
- Approximate nearest neighbor serving
- Ranking, re-ranking, and business constraints
- Monitoring, drift, and feedback loops

For now, the objective is narrower: make the data legible enough that every later modeling decision has a defensible foundation.
