from datasets import load_dataset
from typing import List
from pathlib import Path 

AMAZON_CATEGORIES = [
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
]


def download_data(categories: List[str]) -> None: 
    _validate_categories(categories)
    output_path = Path("data")
    output_path.mkdir(parents=True, exist_ok=True)
        

    for cat in categories: 
        dataset = load_dataset( 
            "json",
            data_files={
                "full": f"hf://datasets/McAuley-Lab/Amazon-Reviews-2023/raw/review_categories/{cat}.jsonl", 
            },
        )
        
        reviews = dataset["full"]
        parquet_path = output_path / f"{cat}.parquet"
        reviews.to_parquet(str(parquet_path))
        print(dir(dataset["full"]))
    print(help(dataset["full"].to_parquet))
    print(dataset) 
    print(dataset[0])
    

def _validate_categories(categories: List[str]) -> None: 
    
    for category in categories: 
        if category not in AMAZON_CATEGORIES: 
            raise ValueError(f"Your category: {category} does not exist in the official amazon categories: {AMAZON_CATEGORIES}")

if __name__ == "__main__":
    download_data(["All_Beauty"])
