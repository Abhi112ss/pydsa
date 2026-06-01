METADATA = {
    "id": 1149,
    "name": "Article Views II",
    "slug": "article-views-ii",
    "category": "Database",
    "aliases": [],
    "tags": ["hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find all authors who viewed at least three different articles on the same day.",
}

def solve(views: list[dict]) -> list[dict]:
    """
    Finds all authors who viewed at least three different articles on the same day.

    Args:
        views: A list of dictionaries where each dictionary represents a view record.
               Each dictionary contains 'author_id', 'viewer_id', 'view_date', and 'article_id'.

    Returns:
        A list of dictionaries containing 'id' (the author_id) sorted in ascending order.

    Examples:
        >>> views = [
        ...     {"author_id": 1, "viewer_id": 1, "view_date": "2019-01-01", "article_id": 1},
        ...     {"author_id": 1, "viewer_id": 1, "view_date": "2019-01-01", "article_id": 2},
        ...     {"author_id": 1, "viewer_id": 1, "view_date": "2019-01-01", "article_id": 3},
        ...     {"author_id": 2, "viewer_id": 2, "view_date": "2019-01-01", "article_id": 1}
        ... ]
        >>> solve(views)
        [{'id': 1}]
    """
    # Grouping structure: {(author_id, view_date): set(article_ids)}
    # We use a set to automatically handle distinct article_ids per author per day
    author_daily_articles: dict[tuple[int, str], set[int]] = {}

    for view in views:
        author_id = view["author_id"]
        view_date = view["view_date"]
        article_id = view["article_id"]
        
        key = (author_id, view_date)
        if key not in author_daily_articles:
            author_daily_articles[key] = set()
        
        author_daily_articles[key].add(article_id)

    # Identify authors who meet the criteria: 3 or more distinct articles on the same day
    result_ids = set()
    for (author_id, view_date), articles in author_daily_articles.items():
        if len(articles) >= 3:
            result_ids.add(author_id)

    # Format the output as a list of dictionaries and sort by id ascending
    sorted_authors = sorted(list(result_ids))
    return [{"id": author_id} for author_id in sorted_authors]
