METADATA = {
    "id": 878,
    "name": "Nth Magical Number",
    "slug": "nth-magical-number",
    "category": "Math",
    "aliases": [],
    "tags": ["binary_search", "inclusion_exclusion", "lcm"],
    "difficulty": "medium",
    "time_complexity": "O(log(n * min(a, b)))",
    "space_complexity": "O(1)",
    "description": "Find the nth number that is divisible by either a or b using binary search and LCM.",
}

import math

def solve(n: int, a: int, b: int) -> int:
    """
    Finds the nth magical number that is divisible by either a or b.

    A magical number is a positive integer that is divisible by either a or b.
    The result should be returned modulo 10^9 + 7.

    Args:
        n (int): The index of the magical number to find.
        a (int): The first divisor.
        b (int): The second divisor.

    Returns:
        int: The nth magical number modulo 10^9 + 7.

    Examples:
        >>> solve(1, 2, 3)
        2
        >>> solve(3, 2, 3)
        4
        >>> solve(4, 2, 3)
        6
    """
    MOD = 1_000_000_007

    # Calculate the Least Common Multiple (LCM) to handle numbers divisible by both.
    # Using the property: lcm(a, b) = (a * b) // gcd(a, b)
    lcm_val = (a * b) // math.gcd(a, b)

    # The search range for binary search:
    # The smallest possible nth magical number is n * min(a, b).
    # The largest possible is n * lcm_val (though n * min(a, b) is a tighter upper bound).
    low = min(a, b)
    high = n * min(a, b)
    
    ans = high

    while low <= high:
        mid = (low + high) // 2
        
        # Inclusion-Exclusion Principle:
        # Count of numbers <= mid divisible by a: mid // a
        # Count of numbers <= mid divisible by b: mid // b
        # Count of numbers <= mid divisible by both (lcm): mid // lcm_val
        # Total count = (mid // a) + (mid // b) - (mid // lcm_val)
        count = (mid // a) + (mid // b) - (mid // lcm_val)

        if count >= n:
            # If we found at least n numbers, mid could be our answer, 
            # but we try to find a smaller one.
            ans = mid
            high = mid - 1
        else:
            # If we found fewer than n numbers, the answer must be larger.
            low = mid + 1

    return ans % MOD
