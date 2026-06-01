METADATA = {
    "id": 877,
    "name": "Stone Game",
    "slug": "stone-game",
    "category": "Game Theory",
    "aliases": [],
    "tags": ["game_theory", "dynamic_programming", "math"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if the first player can win a game where players take stones from either end of a row, given an even number of piles and odd total stones.",
}

def solve(piles: list[int]) -> bool:
    """
    Determines if Alice (the first player) can win the stone game.

    In this game, Alice and Bob take turns picking a pile from either end.
    Alice goes first. The total number of piles is even, and the total 
    number of stones is odd.

    The mathematical insight is that Alice can choose to take all even-indexed 
    piles or all odd-indexed piles. Since the total number of stones is odd, 
    one of these two sets must have a sum greater than the other. 
    Therefore, Alice can always force a win.

    Args:
        piles: A list of integers representing the number of stones in each pile.

    Returns:
        True if Alice can win, False otherwise.

    Examples:
        >>> solve([5, 3, 4, 5])
        True
        >>> solve([5, 6, 7, 4, 11, 5])
        True
    """
    # Because the number of piles is even and the total number of stones is odd,
    # Alice can calculate the sum of stones at even positions and the sum 
    # of stones at odd positions. She then chooses the strategy that 
    # guarantees her the larger sum.
    
    # In the context of the problem constraints and rules, Alice always wins.
    return True
