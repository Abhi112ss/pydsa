METADATA = {
    "id": 793,
    "name": "Preimage Size of Factorial Zeroes Function",
    "slug": "preimage-size-of-factorial-zeroes-function",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(log^2 k)",
    "space_complexity": "O(1)",
    "description": "Find the number of integers n such that the number of trailing zeros in n! is equal to k.",
}

def solve(k: int) -> int:
    """
    Calculates the number of integers n such that the number of trailing zeros in n! is k.

    The number of trailing zeros in n! is determined by the number of times 5 is a factor 
    in the prime factorization of n!. This is calculated using Legendre's Formula.
    Since the count of trailing zeros is a non-decreasing function of n, we can use 
    binary search to find the smallest n that produces at least k zeros.

    Args:
        k: The target number of trailing zeros.

    Returns:
        The size of the preimage of k. This will be 5 if such an n exists, or 0 otherwise.

    Examples:
        >>> solve(2)
        5
        >>> solve(3)
        0
        >>> solve(0)
        5
    """

    def count_trailing_zeros(n: int) -> int:
        """Calculates the number of trailing zeros in n! using Legendre's Formula."""
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count

    # The number of trailing zeros increases at multiples of 5.
    # If a value k is reachable, there will be exactly 5 integers (e.g., 5, 6, 7, 8, 9)
    # that share the same number of trailing zeros.
    
    # Binary search range: 0 to 5 * k (since each multiple of 5 adds at least one zero)
    # We use 5 * k + 5 to handle the k=0 case safely.
    low = 0
    high = 5 * k + 5
    first_n = -1

    while low <= high:
        mid = (low + high) // 2
        if count_trailing_zeros(mid) >= k:
            # If we found a number with >= k zeros, it might be our starting point
            first_n = mid
            high = mid - 1
        else:
            low = mid + 1

    # After finding the smallest n such that count_trailing_zeros(n) >= k,
    # we must verify if count_trailing_zeros(n) is exactly k.
    if first_n != -1 and count_trailing_zeros(first_n) == k:
        # If it matches, the preimage size is always 5 (the block of 5 numbers)
        # However, we must ensure we are looking at the start of the block.
        # The binary search finds the smallest n, which will always be a multiple of 5.
        return 5
    
    return 0
