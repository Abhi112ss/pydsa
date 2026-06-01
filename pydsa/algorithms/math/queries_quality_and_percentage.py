METADATA = {
    "id": 1211,
    "name": "Queries Quality and Percentage",
    "slug": "queries_quality_and_percentage",
    "category": "Database",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Compute average quality and percentage of low ratings per query name.",
}

def solve(queries: list[tuple[str, int, int]]) -> list[tuple[str, float, float]]:
    """Compute average quality and low‑rating percentage for each query name.

    Args:
        queries: A list of tuples where each tuple contains
            (query_name, rating, position). `rating` and `position` are positive integers.

    Returns:
        A list of tuples (query_name, average_quality, low_rating_percentage) sorted
        by `query_name` in ascending order. `average_quality` is the mean of
        rating/position for the given query name. `low_rating_percentage` is the
        percentage of rows with rating < 3.

    Examples:
        >>> data = [
        ...     ("q1", 5, 2),
        ...     ("q1", 2, 1),
        ...     ("q2", 1, 3),
        ...     ("q2", 4, 2),
        ... ]
        >>> solve(data)
        [('q1', 3.5, 50.0), ('q2', 1.8333333333333333, 50.0)]
    """
    # Mapping from query_name to (sum_quality, total_count, low_rating_count)
    aggregates: dict[str, tuple[float, int, int]] = {}

    for query_name, rating, position in queries:
        quality = rating / position  # quality metric for this row
        if query_name not in aggregates:
            aggregates[query_name] = (0.0, 0, 0)
        sum_quality, total_count, low_count = aggregates[query_name]

        sum_quality += quality
        total_count += 1
        low_count += 1 if rating < 3 else 0

        aggregates[query_name] = (sum_quality, total_count, low_count)

    result: list[tuple[str, float, float]] = []
    for query_name in sorted(aggregates):
        sum_quality, total_count, low_count = aggregates[query_name]
        average_quality = sum_quality / total_count
        low_rating_percentage = (low_count / total_count) * 100.0
        result.append((query_name, average_quality, low_rating_percentage))

    return result