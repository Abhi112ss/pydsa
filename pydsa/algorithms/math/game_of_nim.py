METADATA = {
    "id": 1908,
    "name": "Game of Nim",
    "slug": "game_of_nim",
    "category": "math",
    "aliases": [],
    "tags": ["math", "game_theory"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if the first player can win the Nim game given the number of stones.",
}


def solve(stones: int) -> bool:
    """Determine whether the first player wins the Nim game.

    Args:
        stones: The total number of stones in the pile (non‑negative integer).

    Returns:
        True if the first player can force a win, False otherwise.

    Examples:
        >>> solve(1)
        True
        >>> solve(4)
        False
        >>> solve(7)
        True
    """
    # The losing positions are exactly those where stones is a multiple of 4.
    # If stones % 4 != 0, the first player can move to a multiple of 4 and win.
    return stones % 4 != 0