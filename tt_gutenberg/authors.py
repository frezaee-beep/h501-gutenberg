from tt_gutenberg.transform import get_data, get_languages


def list_authors(by_languages=True, alias=True):
    author_metadata = get_data()
    languages = get_languages()

    # Add language information
    full_data = author_metadata.merge(
        languages,
        on="gutenberg_id"
    )

    if by_languages:
        # Count the number of distinct languages for each author
        language_counts = (
            full_data
            .groupby("gutenberg_author_id")["language_y"]
            .nunique()
            .reset_index(name="translation_count")
        )

        # Add the translation counts back to the author information
        author_counts = author_metadata.merge(
            language_counts,
            on="gutenberg_author_id"
        )

        if alias:
            result = (
                author_counts
                .dropna(subset=["alias"])
                .sort_values("translation_count", ascending=False)
                .drop_duplicates(subset=["alias"])
            )

            return result["alias"].tolist()

        result = (
            author_counts
            .sort_values("translation_count", ascending=False)
            .drop_duplicates(subset=["gutenberg_author_id"])
        )

        return result["author_x"].tolist()

    if alias:
        return (
            author_metadata["alias"]
            .dropna()
            .drop_duplicates()
            .tolist()
        )

    return (
        author_metadata["author_x"]
        .drop_duplicates()
        .tolist()
    )