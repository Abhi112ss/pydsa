METADATA = {
    "id": 808,
    "name": "Soup Servings",
    "slug": "soup-servings",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "memoization", "probability"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the probability that soup A will be empty first, plus half the probability that both A and B become empty at the same time.",
}

def solve(n: int) -> float:
    """
    Calculates the probability that soup A empties first plus half the probability 
    that both A and B empty simultaneously.

    The key insight is that as n increases, the expected amount of soup A consumed 
    per operation (250ml) is greater than soup B (125ml), so the probability 
    of A emptying first approaches 1. For n > 4800, the result is within 
    the required precision of 10^-5.

    Args:
        n: The initial amount of soup A and soup B in ml.

    Returns:
        The calculated probability as a float.

    Examples:
        >>> solve(50)
        0.625
        >>> solve(100)
        0.71875
    """
    # For large n, the probability converges to 1.
    # 4800 is a safe threshold derived from the law of large numbers.
    if n > 4800:
        return 1.0

    # Normalize n to units of 25ml to reduce state space.
    # math.ceil(n / 25)
    units = (n + 24) // 25
    
    # memo stores (soup_a_units, soup_b_units) -> probability
    memo: dict[tuple[int, int], float] = {}

    def get_probability(a: int, b: int) -> float:
        """Recursive helper with memoization to calculate probability."""
        # Base cases:
        # Both empty at the same time
        if a <= 0 and b <= 0:
            return 0.5
        # A empties first
        if a <= 0:
            return 1.0
        # B empties first
        if b <= 0:
            return 0.0
        
        state = (a, b)
        if state in memo:
            return memo[state]

        # Four possible operations (each with 0.25 probability):
        # 1. A: 100ml, B: 0ml   -> (a-4, b-0)
        # 2. A: 75ml,  B: 25ml  -> (a-3, b-1)
        # 3. A: 50ml,  B: 50ml  -> (a-2, b-2)
        # 4. A: 25ml,  B: 75ml  -> (a-1, b-3)
        prob = 0.25 * (
            get_probability(a - 4, b) +
            get_probability(a - 3, b - 1) +
            get_probability(a - 2, b - 2) +
            get_probability(a - 1, b - 3)
        )
        
        memo[state] = prob
        return prob

    return get_probability(units, units)
