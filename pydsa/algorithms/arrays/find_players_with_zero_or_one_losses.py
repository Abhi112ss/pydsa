METADATA = {
    "id": 2225,
    "name": "Find Players With Zero or One Losses",
    "slug": "find-players-with-zero-or-one-losses",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "sorting", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find players who have either zero or exactly one loss from a given list of match results.",
}

def solve(losses: list[list[int]]) -> list[list[int]]:
    """
    Finds players with zero or one losses from the match results.

    Args:
        losses: A list of lists, where each sub-list contains two integers [winner, loser].

    Returns:
        A list of lists where each sub-list contains [player_id, loss_count], 
        sorted by player_id. Only includes players with 0 or 1 loss.

    Examples:
        >>> solve([[1, 2], [1, 3], [2, 3]])
        [[1, 0], [2, 1], [3, 2]] -> Wait, the logic is: 
        Player 1: 0 losses. Player 2: 1 loss. Player 3: 2 losses.
        Result: [[1, 0], [2, 1]]
    """
    loss_counts: dict[int, int] = {}
    all_players: set[int] = set()

    # Iterate through matches to track all unique players and their loss counts
    for winner, loser in losses:
        all_players.add(winner)
        all_players.add(loser)
        # Increment loss count for the loser
        loss_counts[loser] = loss_counts.get(loser, 0) + 1

    result: list[list[int]] = []

    # Check every player identified in the matches
    for player in all_players:
        # Get loss count (default to 0 if player never lost)
        count = loss_counts.get(player, 0)
        
        # Criteria: zero or one loss
        if count <= 1:
            result.append([player, count])

    # Sort the result by player ID as required by the problem
    result.sort(key=lambda x: x[0])
    
    return result
