from __future__ import annotations

import logging
from enum import Enum
from pathlib import Path
from typing import Sequence

import pandas as pd
from datasets import load_dataset
from pandas import DataFrame


logger = logging.getLogger(__name__)


HF_DATASET_REPO = "McAuley-Lab/Amazon-Reviews-2023"
HF_DATASET_BASE_PATH = f"hf://datasets/{HF_DATASET_REPO}"
DEFAULT_OUTPUT_DIR = Path("data/raw/amazon_reviews_2023")
HF_SPLIT_NAME = "full"


AMAZON_CATEGORIES = {
    "All_Beauty",
    "Amazon_Fashion",
    "Appliances",
    "Arts_Crafts_and_Sewing",
    "Automotive",
    "Baby_Products",
    "Beauty_and_Personal_Care",
    "Books",
    "CDs_and_Vinyl",
    "Cell_Phones_and_Accessories",
    "Clothing_Shoes_and_Jewelry",
    "Digital_Music",
    "Electronics",
    "Gift_Cards",
    "Grocery_and_Gourmet_Food",
    "Handmade_Products",
    "Health_and_Household",
    "Health_and_Personal_Care",
    "Home_and_Kitchen",
    "Industrial_and_Scientific",
    "Kindle_Store",
    "Magazine_Subscriptions",
    "Movies_and_TV",
    "Musical_Instruments",
    "Office_Products",
    "Patio_Lawn_and_Garden",
    "Pet_Supplies",
    "Software",
    "Sports_and_Outdoors",
    "Subscription_Boxes",
    "Tools_and_Home_Improvement",
    "Toys_and_Games",
    "Video_Games",
    "Unknown",
}


class DataType(str, Enum):
    REVIEWS = "reviews"
    METADATA = "metadata"


def download_data(
    categories: Sequence[str],
    output_dir: str | Path = DEFAULT_OUTPUT_DIR,
    data_type: DataType = DataType.REVIEWS,
    overwrite: bool = False,
) -> list[Path]:
    """
    Download Amazon Reviews 2023 category files from Hugging Face and save them as Parquet.

    Args:
        categories:
            Amazon product categories to download.
        output_dir:
            Directory where Parquet files will be saved.
        data_type:
            Whether to download review interactions or item metadata.
        overwrite:
            If False, skip files that already exist locally.

    Returns:
        List of local Parquet file paths.
    """
    validate_categories(categories)

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    saved_paths: list[Path] = []

    for category in categories:
        parquet_path = get_local_parquet_path(
            category=category,
            output_dir=output_path,
            data_type=data_type,
        )

        if parquet_path.exists() and not overwrite:
            logger.info("Skipping %s because it already exists: %s", category, parquet_path)
            saved_paths.append(parquet_path)
            continue

        remote_path = get_remote_jsonl_path(category=category, data_type=data_type)

        logger.info("Downloading %s %s from %s", category, data_type.value, remote_path)

        dataset_dict = load_dataset(
            "json",
            data_files={HF_SPLIT_NAME: remote_path},
        )

        dataset = dataset_dict[HF_SPLIT_NAME]

        logger.info("Saving %s rows to %s", len(dataset), parquet_path)

        dataset.to_parquet(str(parquet_path))
        saved_paths.append(parquet_path)

    return saved_paths


def load_local_data(
    categories: Sequence[str],
    data_dir: str | Path = DEFAULT_OUTPUT_DIR,
    data_type: DataType = DataType.REVIEWS,
) -> DataFrame:
    """
    Load one or more locally saved Parquet category files into a single pandas DataFrame.

    Args:
        categories:
            Amazon product categories to load.
        data_dir:
            Directory containing saved Parquet files.
        data_type:
            Whether to load review interactions or item metadata.

    Returns:
        Combined pandas DataFrame.
    """
    validate_categories(categories)

    data_path = Path(data_dir)
    frames: list[DataFrame] = []

    for category in categories:
        parquet_path = get_local_parquet_path(
            category=category,
            output_dir=data_path,
            data_type=data_type,
        )

        if not parquet_path.exists():
            raise FileNotFoundError(
                f"Missing local file for category '{category}': {parquet_path}. "
                "Run download_data(...) first."
            )

        frame = pd.read_parquet(parquet_path)
        frame["category"] = category
        frames.append(frame)

    if not frames:
        return pd.DataFrame()

    return pd.concat(frames, ignore_index=True)


def get_remote_jsonl_path(category: str, data_type: DataType) -> str:
    """
    Build the Hugging Face JSONL path for a category and data type.
    """
    if data_type == DataType.REVIEWS:
        return f"{HF_DATASET_BASE_PATH}/raw/review_categories/{category}.jsonl"

    if data_type == DataType.METADATA:
        return f"{HF_DATASET_BASE_PATH}/raw/meta_categories/meta_{category}.jsonl"

    raise ValueError(f"Unsupported data type: {data_type}")


def get_local_parquet_path(
    category: str,
    output_dir: Path,
    data_type: DataType,
) -> Path:
    """
    Build the local Parquet path for a category and data type.
    """
    filename = f"{category}.parquet"

    if data_type == DataType.METADATA:
        filename = f"meta_{filename}"

    return output_dir / data_type.value / filename


def validate_categories(categories: Sequence[str]) -> None:
    """
    Validate that all requested categories exist in Amazon Reviews 2023.
    """
    if not categories:
        raise ValueError("At least one category must be provided.")

    invalid_categories = sorted(set(categories) - AMAZON_CATEGORIES)

    if invalid_categories:
        raise ValueError(
            f"Invalid Amazon categories: {invalid_categories}. "
            f"Valid categories are: {sorted(AMAZON_CATEGORIES)}"
        )


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


if __name__ == "__main__":
    configure_logging()

    download_data(
        categories=["All_Beauty"],
        data_type=DataType.REVIEWS,
        overwrite=False,
    )

    df = load_local_data(
        categories=["All_Beauty"],
        data_type=DataType.REVIEWS,
    )

    print(df.head())
