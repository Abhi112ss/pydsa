METADATA = {
    "id": 3116,
    "name": "Kth Smallest Amount With Single Denomination Combination",
    "slug": "kth-smallest-amount-with-single-denomination-combination",
    "category": "Math",
    "aliases": [],
    "tags": ["binary_search", "math", "inclusion-exclusion"],
    "difficulty": "hard",
    "time_complexity": "O(log(max_val) * 2^n)",
    "space_complexity": "O(1)",
    "description": "Find the kth smallest amount that can be formed by a combination of given denominations using binary search and inclusion-exclusion.",
}

def solve(denominations: list[int], k: int) -> int:
    """
    Finds the kth smallest amount that can be formed by any combination of the given denominations.

    Args:
        denominations: A list of positive integers representing available denominations.
        k: The rank of the amount to find.

    Returns:
        The kth smallest amount.

    Examples:
        >>> solve([2, 5], 3)
        6
        >>> solve([1, 2, 5], 4)
        4
    """
    n = len(denominations)
    
    def count_multiples_less_equal(target: int) -> int:
        """
        Counts how many numbers <= target are multiples of at least one denomination
        using the Principle of Inclusion-Exclusion (PIE).
        """
        count = 0
        # There are 2^n - 1 non-empty subsets of denominations
        # We iterate through all possible subsets using bitmasking
        for i in range(1, 1 << n):
            lcm_val = 1
            bits_set = 0
            for j in range(n):
                if (i >> j) & 1:
                    bits_set += 1
                    # Calculate LCM of the current subset
                    # Since denominations are used to form amounts, we need the LCM
                    # to find numbers divisible by all elements in the subset.
                    lcm_val = _get_lcm(lcm_val, denominations[j])
                    # If LCM exceeds target, it won't contribute to the count
                    if lcm_val > target:
                        break
            
            if lcm_val <= target:
                # Inclusion-Exclusion: add if odd number of elements, subtract if even
                if bits_set % 2 == 1:
                    count += target // lcm_val
                else:
                    count -= target // lcm_val
        return count

    # Binary search range: 
    # Minimum possible amount is the smallest denomination.
    # Maximum possible amount is k * min(denominations).
    low = 1
    high = min(denominations) * k
    ans = high

    while low <= high:
        mid = (low + high) // 2
        # Check if the number of multiples <= mid is at least k
        if count_multiples_less_equal(mid) >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans

def _get_gcd(a: int, b: int) -> int:
    """Computes the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def _get_lcm(a: int, b: int) -> int:
    """Computes the least common multiple of a and b."""
    if a == 0 or b == 0:
        return 0
    # Use the property: lcm(a, b) = abs(a*b) / gcd(a, b)
    # We divide first to prevent unnecessary overflow
    return abs(a * b) // _get_gcd(a, b)
