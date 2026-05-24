---
title: Quality Checks
description: Data validation work that should happen before recommender modeling.
---

# Quality Checks

Before feature engineering or model training, the dataset should survive a small set of hard checks. These are not optional polish tasks. They determine whether later metrics mean anything.

## Minimum checks

1. Verify row counts by category for reviews and metadata after download.
2. Measure join coverage between review item identifiers and metadata item identifiers.
3. Quantify missingness in user IDs, item IDs, timestamps, ratings, and key text fields.
4. Detect duplicate interactions at the `(user, item, timestamp)` level when possible.
5. Check whether timestamps support chronological train, validation, and test splits.

## Why these checks matter for a two-tower system

Two-tower retrieval introduces strong assumptions:

- The item tower needs stable item records and enough metadata coverage.
- The user tower needs enough interaction history to build meaningful user representations.
- The training pairs need trustworthy positives and, later, sensible negative sampling.

If join coverage is poor or identifiers drift between files, the model architecture is not the first problem. The data contract is.

## Suggested next implementation step

After this documentation pass, the next practical code addition should be a small exploratory or validation module that:

- Profiles downloaded Parquet files
- Surfaces null rates and join coverage
- Produces a compact dataset report that can be embedded back into this site later

That creates a much better bridge between documentation and the eventual training pipeline.
