METADATA = {
    "id": 3238,
    "name": "Find the Number of Winning Players",
    "slug": "find-the-number-of-winning-players",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count how many players can win a game where a player wins if their score is strictly greater than all subsequent players' scores.",
}

def solve(player_scores: list[int]) -> int:
    """
    Calculates the number of players who can win the game.
    
    A player wins if their score is strictly greater than the maximum score 
    of all players appearing after them in the list.

    Args:
        player_scores: A list of integers representing the scores of players.

    Returns:
        The total count of winning players.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        1
        >>> solve([5, 4, 3, 2, 1])
        5
        >>> solve([1, 3, 2, 4, 5])
        1
        >>> solve([1, 5, 2, 3, 4])
        1
    """
    n = len(player_scores)
    if n == 0:
        return 0

    winning_players_count = 0
    # We track the maximum score encountered from the right side (suffix maximum)
    # Initialize with a value smaller than any possible score
    current_suffix_max = -1

    # Iterate backwards to maintain the maximum score seen so far to the right
    for i in range(n - 1, -1, -1):
        current_score = player_scores[i]
        
        # A player wins if their score is strictly greater than the max score 
        # of all players to their right.
        if current_score > current_suffix_max:
            winning_players_count += 1
            # Update the suffix maximum for the next player to the left
            current_suffix_max = current_score

    return winning_players_count
