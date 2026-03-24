"""
services.py
-----------
Fetches the HDR UK dataset metadata JSON from the source URL.
Provides helper functions for fetching, preparing, and transforming
dataset metadata for the application.
"""

import requests


SOURCE_URL = "https://raw.githubusercontent.com/HDRUK/hackathon-entity-linkage/refs/heads/dev/fe-implement/app/data/all_datasets.json"

# Return a clean string value or a fallback if the value is missing.
def clean_text(value: object, fallback: str = "Not provided") -> str:
    if value is None:
        return fallback

    text = str(value).strip()
    return text if text else fallback

# Check whether a value looks like a web link.
def is_url(value: str) -> bool:
    return value.startswith("http://") or value.startswith("https://") or value.startswith("www.")

# Download the dataset JSON from the source URL.
def get_json_from_url(url: str) -> list[dict]:
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    data = response.json()

    if not isinstance(data, list):
        raise ValueError("Expected the JSON root to be a list.")

    return data

# Extract the four required fields from each dataset record.
def transform_datasets(raw_datasets: list[dict]) -> list[dict]:
    transformed_datasets = []

    for item in raw_datasets:
        metadata = item.get("metadata", {})
        summary = metadata.get("summary", {})
        accessibility = metadata.get("accessibility", {})
        access = accessibility.get("access", {})

        transformed_datasets.append(
            {
                "title": clean_text(summary.get("title")),
                "description": clean_text(summary.get("description")),
                "accessServiceCategory": clean_text(access.get("accessServiceCategory")),
                "accessRights": clean_text(access.get("accessRights")),
            }
        )

    return transformed_datasets

# Fetch the dataset JSON and return only the transformed fields needed by the app.
def get_transformed_datasets() -> list[dict]:
    raw_datasets = get_json_from_url(SOURCE_URL)
    return transform_datasets(raw_datasets)