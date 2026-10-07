import pandas as pd


def get_data():
    authors_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
    metadata_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"

    authors = pd.read_csv(authors_url)
    metadata = pd.read_csv(metadata_url)

    data = authors.merge(
        metadata,
        on="gutenberg_author_id"
    )

    return data


def get_languages():
    languages_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv"

    languages = pd.read_csv(languages_url)

    return languages