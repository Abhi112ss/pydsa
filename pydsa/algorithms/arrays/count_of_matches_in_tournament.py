METADATA = {
    "id": 1688,
    "name": "Count of Matches in Tournament",
    "slug": "count_of_matches_in_tournament",
    "category": "math",
    "aliases": [],
    "tags": ["simulation", "math", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the total number of matches played in a tournament with n teams.",
}


def solve(n: int) -> int:
    """Calculate the total number of matches played in a tournament.

    Args:
        n: The initial number of teams (n >= 1).

    Returns:
        The total number of matches that will be played until a single champion remains.

    Examples:
        >>> solve(7)
        6
        >>> solve(4)
        3
        >>> solve(1)
        0
    """
    # The total number of matches equals the number of teams eliminated,
    # which is exactly n - 1 because one team remains as champion.
    total_matches: int = n - 1
    return total_matches