import pandas as pd


def load_gutenberg_data():
    authors = pd.read_csv("data/gutenberg_authors.csv")
    metadata = pd.read_csv("data/gutenberg_metadata.csv")
    languages = pd.read_csv("data/gutenberg_languages.csv")

    return authors, metadata, languages