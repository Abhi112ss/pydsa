METADATA = {
    "id": 2923,
    "name": "Find Champion I",
    "slug": "find-champion-i",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the player who has never lost a match in the given results.",
}

def solve(losers: list[int], winners: list[int]) -> int:
    """
    Finds the champion among players, where a champion is a player who has never lost.

    Args:
        losers: A list of integers representing the players who lost a match.
        winners: A list of integers representing the players who won a match.

    Returns:
        The integer ID of the champion.

    Examples:
        >>> solve([1, 2], [2, 3])
        3
        >>> solve([0, 1, 2], [1, 2, 3])
        3
    """
    # Use a set to store all players who have lost at least one match.
    # Sets provide O(1) average time complexity for lookups.
    lost_set = set(losers)
    
    # The champion must be a player who is present in the winners list 
    # but is not present in the losers list.
    # Since the problem guarantees exactly one champion exists, 
    # we can return the first winner we find who isn't in the lost_set.
    for winner in winners:
        if winner not in lost_set:
            return winner
            
    # Fallback for safety, though problem constraints imply a champion always exists.
    return -1
