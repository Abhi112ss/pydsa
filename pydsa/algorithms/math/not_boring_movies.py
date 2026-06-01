METADATA = {
    "id": 620,
    "name": "Not Boring Movies",
    "slug": "not_boring_movies",
    "category": "SQL",
    "aliases": [],
    "tags": ["filtering", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Filter movies with odd-numbered IDs and non-boring descriptions, sorted by rating descending.",
}

def solve(movies: list[dict]) -> list[dict]:
    """
    Filter and sort movies based on criteria from LeetCode #620.

    Args:
        movies: List of dicts with keys 'id' (int), 'movie' (str),
                'description' (str), 'rating' (float).

    Returns:
        Filtered and sorted list of movie dicts.

    Examples:
        >>> movies = [
        ...     {"id": 1, "movie": "Hero", "description": "great", "rating": 8.5},
        ...     {"id": 2, "movie": "Boring", "description": "boring", "rating": 5.0},
        ...     {"id": 3, "movie": "Epic", "description": "exciting", "rating": 9.0},
        ... ]
        >>> result = solve(movies)
        >>> len(result)
        2
        >>> result[0]["id"]
        3
        >>> result[1]["id"]
        1
    """
    # Filter: odd ID (modulo 2 != 0) and description not 'boring'
    filtered = [
        movie for movie in movies
        if movie["id"] % 2 != 0 and movie["description"].lower() != "boring"
    ]

    # Sort by rating descending (stable sort preserves original order for ties)
    filtered.sort(key=lambda m: m["rating"], reverse=True)

    return filtered