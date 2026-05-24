---
title: Source Assets
description: The review and metadata assets already modeled in the codebase.
---

# Source Assets

The current project works with the **Amazon Reviews 2023** dataset and distinguishes between two raw asset types:

- Review records
- Product metadata records

In the code, those are downloaded separately and materialized into local Parquet files.

## Review assets

`download_review_data(...)` pulls category-specific review JSONL files from the Hugging Face-hosted dataset and stores them under `data/raw/reviews`.

```python
download_review_data(["Books", "Electronics"])
```

Each saved file is category-scoped:

```text
data/raw/reviews/Books.parquet
data/raw/reviews/Electronics.parquet
```

## Metadata assets

`download_metadata(...)` performs the same pattern for product metadata and stores the results under `data/raw/metadata`.

```python
download_metadata(["Books", "Electronics"])
```

Each metadata file is also category-scoped:

```text
data/raw/metadata/meta_Books.parquet
data/raw/metadata/meta_Electronics.parquet
```

## Why category partitioning matters

This is a practical starting point:

- It keeps ingestion incremental.
- It makes debugging cheaper.
- It allows early experiments on a narrow domain before expanding to cross-category retrieval.

It also creates a future design question: should the final recommender remain category-bounded, or should it learn across categories with shared item and user representations? That decision should come after exploratory analysis, not before.
