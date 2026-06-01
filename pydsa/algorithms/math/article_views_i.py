METADATA = {
    "id": 1148,
    "name": "Article Views I",
    "slug": "article_views_i",
    "category": "Database",
    "aliases": [],
    "tags": ["hash_map", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Return sorted article IDs where the author also viewed the article.",
}


def solve(views: list[list[int]]) -> list[int]:
    """Return sorted unique article IDs where the author also viewed the article.

    Args:
        views: A list of rows, each row is a list or tuple of three integers
            [viewer_id, article_id, author_id].

    Returns:
        A list of distinct article_id values for which viewer_id == author_id,
        sorted in ascending order.

    Examples:
        >>> solve([[1, 5, 1], [2, 5, 3], [3, 6, 3]])
        [5, 6]
        >>> solve([[10, 100, 20], [20, 101, 20], [30, 102, 30]])
        [101, 102]
    """
    # Use a set to collect article IDs that satisfy the condition.
    matching_article_ids = set()
    for row in views:
        viewer_id, article_id, author_id = row
        if viewer_id == author_id:
            matching_article_ids.add(article_id)

    # Return the IDs sorted in ascending order.
    return sorted(matching_article_ids)