METADATA = {
    "id": 1436,
    "name": "Destination City",
    "slug": "destination_city",
    "category": "graph",
    "aliases": [],
    "tags": ["hash_map", "graphs"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the city that appears only as a destination and never as a starting point.",
}


def solve(paths: list[list[str]]) -> str:
    """Return the destination city from a list of directed paths.

    Args:
        paths: A list of pairs [origin, destination] representing directed edges
            between cities. Each city name is a non‑empty string.

    Returns:
        The name of the city that never appears as an origin but appears as a
        destination exactly once.

    Examples:
        >>> solve([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
        'Sao Paulo'
        >>> solve([["A","B"],["B","C"],["C","D"]])
        'D'
    """
    # Collect all cities that appear as an origin.
    origin_cities: set[str] = {origin for origin, _ in paths}
    # The destination city is the one whose destination is not an origin.
    for _, destination in paths:
        if destination not in origin_cities:
            return destination
    # According to problem constraints, a solution always exists.
    raise ValueError("No destination city found")