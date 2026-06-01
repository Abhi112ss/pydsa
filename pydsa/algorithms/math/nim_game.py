METADATA = {
    "id": 292,
    "name": "Nim Game",
    "slug": "nim_game",
    "category": "Brainteaser",
    "aliases": ["nim_game", "can_win_nim"],
    "tags": ["game_theory", "brainteaser"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine whether you can win the Nim game given the number of stones in the heap.",
}

def solve(n: int) -> bool:
    """Determine if you can win the Nim game given the number of stones in the heap.

    In the Nim game, you and your friend take turns removing 1 to 3 stones from a heap.
    You go first. The player who removes the last stone wins.

    Args:
        n: The number of stones in the heap.

    Returns:
        True if you can win the game, False otherwise.

    Examples:
        >>> solve(4)
        False
        >>> solve(1)
        True
        >>> solve(5)
        True
    """
    # The key insight is that you will lose if and only if the number of stones is a multiple of 4.
    # If n is divisible by 4, your opponent can always force a win by making the total removed
    # stones in each round equal to 4, leaving you with a multiple of 4 again.
    return n % 4 != 0