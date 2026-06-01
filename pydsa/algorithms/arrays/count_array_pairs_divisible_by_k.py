METADATA = {
    "id": 2183,
    "name": "Count Array Pairs Divisible by K",
    "slug": "count-array-pairs-divisible-by-k",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Count the number of pairs (i, j) such that (nums[i] * nums[j]) % k == 0.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of pairs (i, j) such that (nums[i] * nums[j]) % k == 0.

    The core idea is that for the product of two numbers to be divisible by k,
    the product of their greatest common divisors with k must be divisible by k.
    Specifically, if gcd(nums[i], k) = g1 and gcd(nums[j], k) = g2, 
    then (g1 * g2) % k must be 0.

    Args:
        nums: A list of integers.
        k: The divisor.

    Returns:
        The total number of pairs (i, j) where 0 <= i < j < len(nums) 
        and (nums[i] * nums[j]) % k == 0.

    Examples:
        >>> solve([2, 3, 4, 6], 6)
        4
        >>> solve([1, 2, 3], 1)
        3
    """
    import math

    def get_gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    # Frequency map to store counts of gcd(num, k)
    # Since all gcd(num, k) must be divisors of k, the map size is at most the number of divisors of k.
    gcd_counts: dict[int, int] = {}

    for num in nums:
        # We only care about the part of num that contributes to divisibility by k
        common_factor = get_gcd(num, k)
        gcd_counts[common_factor] = gcd_counts.get(common_factor, 0) + 1

    total_pairs = 0
    # Get all unique gcd values present in the array
    unique_gcds = list(gcd_counts.keys())

    for i in range(len(unique_gcds)):
        g1 = unique_gcds[i]
        count1 = gcd_counts[g1]

        # Case 1: Pair two numbers that have the same gcd with k
        # This is only valid if (g1 * g1) % k == 0
        if (g1 * g1) % k == 0:
            # Combination formula nC2: n * (n - 1) // 2
            total_pairs += (count1 * (count1 - 1)) // 2

        # Case 2: Pair two numbers with different gcds (g1 and g2)
        # We only iterate for j > i to avoid double counting
        for j in range(i + 1, len(unique_gcds)):
            g2 = unique_gcds[j]
            count2 = gcd_counts[g2]
            
            if (g1 * g2) % k == 0:
                total_pairs += count1 * count2

    return total_pairs
