METADATA = {
    "id": 1735,
    "name": "Count Ways to Make Array With Product",
    "slug": "count-ways-to-make-array-with-product",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "prime factorization"],
    "difficulty": "hard",
    "time_complexity": "O(n * num_factors)",
    "space_complexity": "O(n * num_factors)",
    "description": "Count the number of ways to construct an array of length n such that the product of its elements equals target, using only positive integers.",
}

def solve(n: int, target: int) -> int:
    """
    Calculates the number of ways to form an array of length n with a given product.

    Args:
        n: The required length of the array.
        target: The required product of the array elements.

    Returns:
        The number of ways to form the array modulo 10^9 + 7.

    Examples:
        >>> solve(2, 6)
        4
        # Ways: [1, 6], [6, 1], [2, 3], [3, 2]
        >>> solve(3, 4)
        6
        # Ways: [1, 1, 4], [1, 4, 1], [4, 1, 1], [1, 2, 2], [2, 1, 2], [2, 2, 1]
    """
    MOD = 10**9 + 7

    # Step 1: Prime Factorization of target
    # We only care about the exponents of the prime factors.
    # For example, if target is 12 (2^2 * 3^1), we care about exponents [2, 1].
    temp_target = target
    exponents = []
    d = 2
    while d * d <= temp_target:
        if temp_target % d == 0:
            count = 0
            while temp_target % d == 0:
                count += 1
                temp_target //= d
            exponents.append(count)
        d += 1
    if temp_target > 1:
        exponents.append(1)

    if not exponents:
        # target is 1, all elements must be 1. Only 1 way.
        return 1

    num_primes = len(exponents)
    
    # Step 2: Combinatorial approach using Stars and Bars
    # For each prime factor p^k, we need to distribute k 'powers' into n slots.
    # However, the problem allows the number 1 in the array. 
    # The number 1 doesn't contribute to any prime factor.
    # This is equivalent to: for each prime factor p_i with exponent e_i,
    # we distribute e_i items into n bins.
    # The number of ways to distribute e items into n bins is C(e + n - 1, n - 1).
    
    # Precompute combinations using Pascal's triangle or formula
    # Since n and exponents are relatively small, we can use a simple function.
    def combinations(n_val: int, k_val: int) -> int:
        if k_val < 0 or k_val > n_val:
            return 0
        if k_val == 0 or k_val == n_val:
            return 1
        if k_val > n_val // 2:
            k_val = n_val - k_val
        
        num = 1
        den = 1
        for i in range(k_val):
            num = (num * (n_val - i))
            den = (den * (i + 1))
        return num // den

    # The total ways is the product of ways to distribute each prime factor's exponent.
    # For each prime factor with exponent e, we use Stars and Bars:
    # Ways = C(e + n - 1, n - 1)
    # This accounts for all possible combinations of integers whose product is target.
    # Note: The number 1 is implicitly handled because it's like assigning 0 to all prime exponents.
    
    total_ways = 1
    for e in exponents:
        # Ways to distribute 'e' identical items into 'n' distinct bins
        ways_for_this_prime = combinations(e + n - 1, n - 1)
        total_ways = (total_ways * ways_for_this_prime) % MOD

    return total_ways
