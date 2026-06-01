METADATA = {
    "id": 2929,
    "name": "Distribute Candies Among Children II",
    "slug": "distribute-candies-among-children-ii",
    "category": "combinatorics",
    "aliases": [],
    "tags": ["combinatorics", "inclusion_exclusion", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the number of ways to distribute n candies among k children such that each child receives at most limit candies, using the Principle of Inclusion-Exclusion.",
}

def solve(n: int, k: int, limit: int) -> int:
    """
    Calculates the number of ways to distribute n candies among k children 
    where each child receives between 0 and limit candies (inclusive).

    The problem is equivalent to finding the coefficient of x^n in the 
    expansion of (1 + x + x^2 + ... + x^limit)^k.
    Using the formula for a finite geometric series, this is:
    ((1 - x^(limit + 1)) / (1 - x))^k = (1 - x^(limit + 1))^k * (1 - x)^(-k)

    Args:
        n: Total number of candies to distribute.
        k: Total number of children.
        limit: Maximum number of candies any single child can receive.

    Returns:
        The number of valid distributions modulo 10^9 + 7.

    Examples:
        >>> solve(3, 2, 2)
        2
        >>> solve(5, 3, 2)
        3
    """
    MOD = 1_000_000_007

    if n < 0:
        return 0
    if k == 0:
        return 1 if n == 0 else 0

    # Precompute factorials for combinations
    # Max value needed is n + k
    max_val = n + k
    fact = [1] * (max_val + 1)
    inv_fact = [1] * (max_val + 1)

    for i in range(1, max_val + 1):
        fact[i] = (fact[i - 1] * i) % MOD

    inv_fact[max_val] = pow(fact[max_val], MOD - 2, MOD)
    for i in range(max_val - 1, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

    def nCr(n_val: int, r_val: int) -> int:
        if r_val < 0 or r_val > n_val:
            return 0
        num = fact[n_val]
        den = (inv_fact[r_val] * inv_fact[n_val - r_val]) % MOD
        return (num * den) % MOD

    # Principle of Inclusion-Exclusion (PIE)
    # Total ways = sum_{i=0}^{k} (-1)^i * C(k, i) * C(n - i*(limit + 1) + k - 1, k - 1)
    # where i is the number of children who violate the limit (receive >= limit + 1 candies)
    ans = 0
    for i in range(k + 1):
        # Number of candies remaining after giving (limit + 1) to 'i' children
        remaining_n = n - i * (limit + 1)
        
        if remaining_n < 0:
            break
            
        # Ways to choose 'i' children to violate the limit
        ways_to_choose_children = nCr(k, i)
        
        # Stars and Bars: ways to distribute remaining_n candies to k children
        # Formula: C(remaining_n + k - 1, k - 1)
        ways_to_distribute_remaining = nCr(remaining_n + k - 1, k - 1)
        
        term = (ways_to_choose_children * ways_to_distribute_remaining) % MOD
        
        if i % 2 == 1:
            ans = (ans - term + MOD) % MOD
        else:
            ans = (ans + term) % MOD
            
    return ans
