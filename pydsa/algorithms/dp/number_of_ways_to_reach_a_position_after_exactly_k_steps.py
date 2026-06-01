METADATA = {
    "id": 2400,
    "name": "Number of Ways to Reach a Position After Exactly k Steps",
    "slug": "number-of-ways-to-reach-a-position-after-exactly-k-steps",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "combinatorics"],
    "difficulty": "hard",
    "time_complexity": "O(k^2)",
    "space_complexity": "O(k^2)",
    "description": "Calculate the number of ways to reach a target position (x, y) from (0, 0) in exactly k steps.",
}

def solve(x: int, y: int, k: int) -> int:
    """
    Calculates the number of ways to reach (x, y) from (0, 0) in exactly k steps.
    
    The problem can be modeled as finding the number of ways to choose steps 
    in four directions: Up, Down, Left, and Right.
    Let:
    u = steps up, d = steps down, l = steps left, r = steps right.
    
    Constraints:
    1) u + d + l + r = k
    2) r - l = x
    3) u - d = y
    
    From (2) and (3):
    r = l + x
    u = d + y
    
    Substitute into (1):
    (d + y) + d + l + (l + x) = k
    2d + 2l + x + y = k
    2(d + l) = k - x - y
    
    This implies (k - x - y) must be non-negative and even.
    Let S = (k - x - y) // 2. Then d + l = S.
    We can iterate through all possible values of l from 0 to S.
    For a fixed l:
    l = l
    r = l + x
    d = S - l
    u = d + y = S - l + y
    
    The number of ways for a specific set of (u, d, l, r) is the multinomial coefficient:
    Ways = k! / (u! * d! * l! * r!)
    
    Args:
        x: Target x-coordinate.
        y: Target y-coordinate.
        k: Exact number of steps.

    Returns:
        The number of ways to reach (x, y) in k steps.

    Examples:
        >>> solve(1, 1, 2)
        1
        >>> solve(0, 0, 1)
        0
        >>> solve(1, 0, 3)
        2
    """
    MOD = 10**9 + 7
    
    # Absolute values because directions are symmetric
    x, y = abs(x), abs(y)
    
    # Parity check and reachability check
    # The total steps k must be at least the Manhattan distance,
    # and the remaining steps must be even to allow for back-and-forth movement.
    if (k - x - y) < 0 or (k - x - y) % 2 != 0:
        return 0

    # Precompute factorials for multinomial coefficient calculation
    fact = [1] * (k + 1)
    inv_fact = [1] * (k + 1)
    for i in range(1, k + 1):
        fact[i] = (fact[i - 1] * i) % MOD
        
    # Modular inverse using Fermat's Little Theorem
    inv_fact[k] = pow(fact[k], MOD - 2, MOD)
    for i in range(k - 1, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

    def multinomial(u: int, d: int, l: int, r: int) -> int:
        # k! / (u! * d! * l! * r!)
        num = fact[k]
        den = (inv_fact[u] * inv_fact[d]) % MOD
        den = (den * inv_fact[l]) % MOD
        den = (den * inv_fact[r]) % MOD
        return (num * den) % MOD

    total_ways = 0
    # S is the number of 'extra' pairs of steps (one step in one direction, one in opposite)
    # specifically, d + l = (k - x - y) // 2
    S = (k - x - y) // 2
    
    # Iterate through all possible distributions of the 'extra' steps between 
    # the vertical axis (d) and horizontal axis (l)
    for l in range(S + 1):
        d = S - l
        r = l + x
        u = d + y
        
        # Ensure all step counts are non-negative
        if u >= 0 and d >= 0 and l >= 0 and r >= 0:
            total_ways = (total_ways + multinomial(u, d, l, r)) % MOD
            
    return total_ways
