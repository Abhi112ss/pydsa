METADATA = {
    "id": 1692,
    "name": "Count Ways to Distribute Candies",
    "slug": "count-ways-to-distribute-candies",
    "category": "Math",
    "aliases": [],
    "tags": ["combinatorics", "math"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of ways to distribute remaining candies to children using the stars and bars formula.",
}

def solve(n: int, k: int, limit: int) -> int:
    """
    Calculates the number of ways to distribute n candies to k children 
    such that each child receives at most 'limit' candies.

    This problem is solved using the Principle of Inclusion-Exclusion (PIE) 
    combined with the Stars and Bars formula.

    Args:
        n: The total number of candies to distribute.
        k: The number of children.
        limit: The maximum number of candies any single child can receive.

    Returns:
        The total number of ways to distribute the candies modulo 10^9 + 7.

    Examples:
        >>> solve(3, 2, 2)
        2
        >>> solve(5, 3, 2)
        3
    """
    MOD = 1_000_000_007

    def combinations(n_val: int, k_val: int) -> int:
        """Calculates nCr modulo 10^9 + 7 using a simple iterative approach."""
        if k_val < 0 or k_val > n_val:
            return 0
        if k_val == 0 or k_val == n_val:
            return 1
        if k_val > n_val // 2:
            k_val = n_val - k_val
        
        num = 1
        den = 1
        for i in range(k_val):
            num = (num * (n_val - i)) % MOD
            den = (den * (i + 1)) % MOD
        
        # Using Fermat's Little Theorem for modular inverse: den^(MOD-2) % MOD
        return (num * pow(den, MOD - 2, MOD)) % MOD

    def stars_and_bars(candies: int, children: int) -> int:
        """Standard stars and bars: ways to put 'candies' into 'children' bins."""
        if candies < 0:
            return 0
        if children == 0:
            return 1 if candies == 0 else 0
        # Formula: (n + k - 1) choose (k - 1)
        return combinations(candies + children - 1, children - 1)

    # Principle of Inclusion-Exclusion (PIE)
    # Total ways = (Ways with 0 children violating limit) 
    #              - (Ways with at least 1 child violating limit)
    #              + (Ways with at least 2 children violating limit) ...
    # A child violates the limit if they get at least (limit + 1) candies.
    
    total_ways = 0
    for i in range(k + 1):
        # Number of candies already 'pre-allocated' to i children to force violation
        violation_count = i * (limit + 1)
        remaining_candies = n - violation_count
        
        if remaining_candies < 0:
            break
            
        # Ways to choose which 'i' children violate the limit
        ways_to_choose_violators = combinations(k, i)
        
        # Ways to distribute the remaining candies among all k children
        ways_to_distribute_rest = stars_and_bars(remaining_candies, k)
        
        term = (ways_to_choose_violators * ways_to_distribute_rest) % MOD
        
        # Add if even number of violators (inclusion), subtract if odd (exclusion)
        if i % 2 == 0:
            total_ways = (total_ways + term) % MOD
        else:
            total_ways = (total_ways - term + MOD) % MOD
            
    return total_ways
