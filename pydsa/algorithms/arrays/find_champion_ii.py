METADATA = {
    "id": 2924,
    "name": "Find Champion II",
    "slug": "find-champion-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the unique player who has never lost a match based on the provided tournament results.",
}

def solve(players: list[int], matches: list[list[int]]) -> int:
    """
    Identifies the unique player who has never lost a match.

    Args:
        players: A list of integers representing the IDs of all players.
        matches: A list of pairs [winner, loser] representing the match results.

    Returns:
        The ID of the player who has no losses.

    Examples:
        >>> solve([1, 2, 3], [[1, 2], [1, 3]])
        1
        >>> solve([1, 2, 3, 4], [[1, 2], [3, 4], [1, 3]])
        1
    """
    # Use a set to keep track of all players who have lost at least one match.
    # A set provides O(1) average time complexity for additions and lookups.
    losers = set()
    
    for winner, loser in matches:
        losers.add(loser)
        
    # The champion is the player present in the players list but not in the losers set.
    # Since the problem guarantees a unique undefeated player, we return the first match.
    for player in players:
        if player not in losers:
            return player
            
    # Fallback return (though problem constraints imply a champion always exists)
    return -1
