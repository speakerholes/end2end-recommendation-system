from pathlib import Path

import pandas as pd
from datasets import load_dataset
from pandas import DataFrame


HF_DATASET_REPO = "McAuley-Lab/Amazon-Reviews-2023"
HF_DATASET_BASE_PATH = f"hf://datasets/{HF_DATASET_REPO}"
HF_SPLIT_NAME = "full"

DEFAULT_REVIEWS_DIR = Path("data/raw/reviews")
DEFAULT_METADATA_DIR = Path("data/raw/metadata")


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


def download_review_data(
    categories: list[str],
    output_dir: str | Path = DEFAULT_REVIEWS_DIR,
    overwrite: bool = False,
) -> list[Path]:
    """
    Download Amazon Reviews 2023 review JSONL files and save them as Parquet.
    """
    validate_categories(categories)

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    saved_paths: list[Path] = []

    for category in categories:
        parquet_path = get_review_parquet_path(category, output_path)

        if parquet_path.exists() and not overwrite:
            print(f"Skipping {category}; already exists at {parquet_path}")
            saved_paths.append(parquet_path)
            continue

        remote_path = get_review_jsonl_path(category)

        dataset_dict = load_dataset(
            "json",
            data_files={HF_SPLIT_NAME: remote_path},
        )

        reviews = dataset_dict[HF_SPLIT_NAME]
        reviews.to_parquet(str(parquet_path))

        print(f"Saved reviews for {category} to {parquet_path}")
        saved_paths.append(parquet_path)

    return saved_paths


def download_metadata(
    categories: list[str],
    output_dir: str | Path = DEFAULT_METADATA_DIR,
    overwrite: bool = False,
) -> list[Path]:
    """
    Download Amazon Reviews 2023 metadata JSONL files and save them as Parquet.
    """
    validate_categories(categories)

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    saved_paths: list[Path] = []

    for category in categories:
        parquet_path = get_metadata_parquet_path(category, output_path)

        if parquet_path.exists() and not overwrite:
            print(f"Skipping metadata for {category}; already exists at {parquet_path}")
            saved_paths.append(parquet_path)
            continue

        remote_path = get_metadata_jsonl_path(category)

        dataset_dict = load_dataset(
            "json",
            data_files={HF_SPLIT_NAME: remote_path},
        )

        metadata = dataset_dict[HF_SPLIT_NAME]
        metadata.to_parquet(str(parquet_path))

        print(f"Saved metadata for {category} to {parquet_path}")
        saved_paths.append(parquet_path)

    return saved_paths


def load_review_data(
    categories: list[str],
    data_dir: str | Path = DEFAULT_REVIEWS_DIR,
) -> DataFrame:
    """
    Load one or more local review Parquet files into a single pandas DataFrame.
    """
    validate_categories(categories)

    frames: list[DataFrame] = []
    data_path = Path(data_dir)

    for category in categories:
        parquet_path = get_review_parquet_path(category, data_path)

        if not parquet_path.exists():
            raise FileNotFoundError(
                f"Missing review file for category '{category}': {parquet_path}. "
                "Run download_review_data(...) first."
            )

        df = pd.read_parquet(parquet_path)
        df["category"] = category
        frames.append(df)

    return _concat_frames(frames)


def load_metadata(
    categories: list[str],
    data_dir: str | Path = DEFAULT_METADATA_DIR,
) -> DataFrame:
    """
    Load one or more local metadata Parquet files into a single pandas DataFrame.
    """
    validate_categories(categories)

    frames: list[DataFrame] = []
    data_path = Path(data_dir)

    for category in categories:
        parquet_path = get_metadata_parquet_path(category, data_path)

        if not parquet_path.exists():
            raise FileNotFoundError(
                f"Missing metadata file for category '{category}': {parquet_path}. "
                "Run download_metadata(...) first."
            )

        df = pd.read_parquet(parquet_path)
        df["category"] = category
        frames.append(df)

    return _concat_frames(frames)


def get_review_jsonl_path(category: str) -> str:
    """
    Build remote Hugging Face path for a review category JSONL file.
    """
    validate_categories([category])
    return f"{HF_DATASET_BASE_PATH}/raw/review_categories/{category}.jsonl"


def get_metadata_jsonl_path(category: str) -> str:
    """
    Build remote Hugging Face path for a metadata category JSONL file.
    """
    validate_categories([category])
    return f"{HF_DATASET_BASE_PATH}/raw/meta_categories/meta_{category}.jsonl"


def get_review_parquet_path(category: str, output_dir: str | Path) -> Path:
    """
    Build local Parquet path for a review category file.
    """
    validate_categories([category])
    return Path(output_dir) / f"{category}.parquet"


def get_metadata_parquet_path(category: str, output_dir: str | Path) -> Path:
    """
    Build local Parquet path for a metadata category file.
    """
    validate_categories([category])
    return Path(output_dir) / f"meta_{category}.parquet"


def validate_categories(categories: list[str]) -> None:
    """
    Validate Amazon Reviews 2023 category names.
    """
    if not categories:
        raise ValueError("At least one category must be provided.")

    invalid_categories = sorted(set(categories) - AMAZON_CATEGORIES)

    if invalid_categories:
        raise ValueError(
            f"Invalid Amazon categories: {invalid_categories}. "
            f"Valid categories are: {sorted(AMAZON_CATEGORIES)}"
        )


def _concat_frames(frames: list[DataFrame]) -> DataFrame:
    """
    Concatenate DataFrames and handle the empty case cleanly.
    """
    if not frames:
        return pd.DataFrame()

    return pd.concat(frames, ignore_index=True)
