METADATA = {
    "id": 1025,
    "name": "Divisor Game",
    "slug": "divisor-game",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "dynamic_programming", "game_theory"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if Alice wins a game where players choose a divisor x of N such that 0 < x < N and N = N - x.",
}

def solve(n: int) -> bool:
    """
    Determines if Alice wins the divisor game starting with number n.

    The game follows these rules:
    1. Alice starts first.
    2. On each turn, a player chooses an integer x such that 0 < x < N and N % x == 0.
    3. The player replaces N with N - x.
    4. The player who cannot make a move loses.

    Mathematical Insight:
    If N is even, Alice can always choose x = 1, making the new N odd.
    An odd number N only has odd divisors. Subtracting an odd divisor from an 
    odd number always results in an even number.
    Therefore, Alice can always return an even number to Bob, and Bob will 
    always be forced to return an odd number to Alice, until Bob eventually 
    receives N = 1 and loses.

    Args:
        n (int): The starting integer.

    Returns:
        bool: True if Alice wins, False otherwise.

    Examples:
        >>> solve(2)
        True
        >>> solve(3)
        False
    """
    # If n is even, Alice can always force a win by picking x=1.
    # If n is odd, any divisor x must be odd, making (n - x) even, 
    # which hands the winning position back to the opponent.
    return n % 2 == 0
