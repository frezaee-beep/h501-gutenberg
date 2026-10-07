import pandas as pd


def get_data():
    authors = pd.read_csv("data/gutenberg_authors.csv")
    metadata = pd.read_csv("data/gutenberg_metadata.csv")

    data = authors.merge(
        metadata,
        on="gutenberg_author_id"
    )

    return data



def get_languages():
    languages = pd.read_csv("data/gutenberg_languages.csv")
    return languages