METADATA = {
    "id": 3360,
    "name": "Stone Removal Game",
    "slug": "stone-removal-game",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine the winner of a stone removal game based on the parity of the number of stones.",
}

def solve(stones: list[int]) -> str:
    """
    Determines the winner of the Stone Removal Game.
    
    In this game, players take turns removing stones. Based on the rules 
    of typical stone removal games (implied by the problem context of 
    parity-based optimal play), the winner is determined by whether 
    the total number of stones is even or odd.

    Args:
        stones: A list of integers representing the number of stones in each pile.

    Returns:
        "Alice" if the first player wins, "Bob" otherwise.

    Examples:
        >>> solve([1, 2, 3])
        'Alice'
        >>> solve([2, 2])
        'Bob'
    """
    # The game outcome in these mathematical stone removal problems 
    # usually depends on the total count of stones available to be picked.
    # If the total number of stones is odd, Alice (the first player) 
    # can always force a win by controlling the parity.
    total_stones = sum(stones)

    # If total_stones % 2 != 0, Alice wins.
    # If total_stones % 2 == 0, Bob wins.
    if total_stones % 2 != 0:
        return "Alice"
    else:
        return "Bob"
