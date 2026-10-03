from tt_gutenberg.data import load_gutenberg_data


def list_authors(by_languages=True, alias=True):
    authors, metadata, languages = load_gutenberg_data()

    # Merge author information with book information
    author_metadata = authors.merge(
        metadata,
        on="gutenberg_author_id"
    )

    # Add language information
    full_data = author_metadata.merge(
        languages,
        on="gutenberg_id"
    )

    # Remove rows with missing aliases
    clean_data = full_data.dropna(subset=["alias"])

    # Keep one row per author/work
    works = clean_data[
        ["alias", "author_x", "gutenberg_id", "total_languages"]
    ].drop_duplicates()

    # Number of translations for each work
    works["translations"] = works["total_languages"] - 1

    if by_languages:
        # Calculate total translations for each author
        translation_counts = (
            works
            .groupby("alias")["translations"]
            .sum()
            .sort_values(ascending=False)
        )

        if alias:
            return translation_counts.index.tolist()

    if alias:
        return works["alias"].drop_duplicates().tolist()

    return works["author_x"].drop_duplicates().tolist()