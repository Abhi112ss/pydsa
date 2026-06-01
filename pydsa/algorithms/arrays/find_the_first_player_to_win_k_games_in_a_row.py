METADATA = {
    "id": 3175,
    "name": "Find The First Player to win K Games in a Row",
    "slug": "find-the-first-player-to-win-k-games-in-a-row",
    "category": "Simulation",
    "aliases": [],
    "tags": ["arrays", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the first player who achieves a winning streak of at least k consecutive games.",
}

def solve(players: list[int], winners: list[int], k: int) -> int:
    """
    Finds the first player to win k games in a row.

    Args:
        players: A list of player IDs in the order they appear in the games.
        winners: A list of player IDs who won each respective game.
        k: The required number of consecutive wins to be identified.

    Returns:
        The ID of the first player to achieve a streak of k wins, or -1 if no such player exists.

    Examples:
        >>> solve([1, 2, 3], [1, 1, 2], 2)
        1
        >>> solve([1, 2, 3], [1, 2, 1], 2)
        -1
    """
    if not winners or k <= 0:
        return -1

    current_streak_player = winners[0]
    current_streak_count = 0

    for winner in winners:
        # If the current winner is the same as the previous winner, increment streak
        if winner == current_streak_player:
            current_streak_count += 1
        else:
            # Otherwise, reset the streak to 1 for the new winner
            current_streak_player = winner
            current_streak_count = 1
        
        # Check if the current streak has reached the target k
        if current_streak_count == k:
            return current_streak_player

    return -1
