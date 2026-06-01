METADATA = {
    "id": 3222,
    "name": "Find the Winning Player in Coin Game",
    "slug": "find-the-winning-player-in-coin-game",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "game_theory"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine the winner of a coin game based on the parity of the total number of coins.",
}

def solve(n: int, k: int) -> int:
    """
    Determines the winner of the coin game.
    
    In this game, players take turns removing coins. Based on the game rules 
    implied by the parity of the total coins (n) and the turn constraints (k), 
    the winner can be determined by checking if the total number of coins 
    is even or odd.

    Args:
        n (int): The total number of coins available.
        k (int): The number of coins a player can take or a turn constraint.

    Returns:
        int: 1 if the first player wins, 2 if the second player wins.

    Examples:
        >>> solve(3, 1)
        1
        >>> solve(4, 1)
        2
    """
    # The game outcome in such parity-based games typically depends on 
    # whether the total number of items is even or odd.
    # If n is odd, the first player (1) takes the last coin.
    # If n is even, the second player (2) takes the last coin.
    
    if n % 2 != 0:
        return 1
    else:
        return 2
