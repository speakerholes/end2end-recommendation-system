from end2end_recommendation_system.data import (
    download_metadata,
    download_review_data,
    load_metadata,
    load_review_data,
)


def main() -> None:
    categories = ["All_Beauty"]

    download_review_data(categories)
    download_metadata(categories)

    reviews = load_review_data(categories)
    metadata = load_metadata(categories)

    print("Reviews:")
    print(reviews.head())

    print("Metadata:")
    print(metadata.head())


if __name__ == "__main__":
    main()
