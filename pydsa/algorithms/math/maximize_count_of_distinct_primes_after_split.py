METADATA = {
    "id": 3569,
    "name": "Maximize Count of Distinct Primes After Split",
    "slug": "maximize-count-of-distinct-primes-after-split",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy", "prime factorization"],
    "difficulty": "medium",
    "time_complexity": "O(n * sqrt(max_val))",
    "space_complexity": "O(1)",
    "description": "Maximize the count of distinct prime factors obtained by splitting an array into two parts.",
}

def get_prime_factors(n: int) -> set[int]:
    """
    Helper function to find all unique prime factors of a given integer.

    Args:
        n: The integer to factorize.

    Returns:
        A set containing the unique prime factors of n.
    """
    factors = set()
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            factors.add(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        factors.add(temp)
    return factors

def solve(nums: list[int]) -> int:
    """
    Finds the maximum number of distinct prime factors that can be collected
    by splitting the array into two non-empty contiguous subarrays.

    The problem asks to split the array at some index i (0 <= i < len(nums) - 1)
    such that the union of prime factors of elements in nums[0...i] and 
    nums[i+1...n-1] is maximized.

    Args:
        nums: A list of positive integers.

    Returns:
        The maximum count of distinct prime factors across the split.

    Examples:
        >>> solve([2, 3, 4, 5])
        4
        >>> solve([6, 10, 15])
        3
    """
    n = len(nums)
    if n < 2:
        return 0

    # Precompute prime factors for each number to avoid redundant calculations
    # prime_sets[i] stores the set of unique prime factors of nums[i]
    prime_sets = [get_prime_factors(x) for x in nums]

    # prefix_primes[i] will store the set of all unique prime factors 
    # present in the subarray nums[0...i]
    prefix_primes = [set() for _ in range(n)]
    current_prefix = set()
    for i in range(n):
        current_prefix.update(prime_sets[i])
        prefix_primes[i] = set(current_prefix)

    # suffix_primes[i] will store the set of all unique prime factors 
    # present in the subarray nums[i...n-1]
    suffix_primes = [set() for _ in range(n)]
    current_suffix = set()
    for i in range(n - 1, -1, -1):
        current_suffix.update(prime_sets[i])
        suffix_primes[i] = set(current_suffix)

    max_distinct_primes = 0

    # Iterate through all possible split points. 
    # A split at index i means the left part is nums[0...i] 
    # and the right part is nums[i+1...n-1].
    for i in range(n - 1):
        # The union of prime factors from both sides
        # Using the precomputed prefix and suffix sets
        combined_primes = prefix_primes[i] | suffix_primes[i + 1]
        max_distinct_primes = max(max_distinct_primes, len(combined_primes))

    return max_distinct_primes
