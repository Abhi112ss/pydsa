METADATA = {
    "id": 2427,
    "name": "Number of Common Factors",
    "slug": "number-of-common-factors",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "gcd", "divisors"],
    "difficulty": "easy",
    "time_complexity": "O(sqrt(min(a, b)))",
    "space_complexity": "O(1)",
    "description": "Find the number of positive integers that divide both a and b.",
}

import math

def solve(a: int, b: int) -> int:
    """
    Calculates the number of common factors between two positive integers.

    The algorithm finds the Greatest Common Divisor (GCD) of the two numbers
    and then counts the number of divisors of that GCD.

    Args:
        a: The first positive integer.
        b: The second positive integer.

    Returns:
        The count of positive integers that divide both a and b.

    Examples:
        >>> solve(2, 4)
        2
        >>> solve(3, 4)
        1
        >>> solve(12, 24)
        6
    """
    # The common factors of a and b are exactly the divisors of gcd(a, b)
    common_gcd = math.gcd(a, b)
    
    count = 0
    limit = int(math.isqrt(common_gcd))
    
    # Iterate up to the square root of the GCD to find all divisors efficiently
    for i in range(1, limit + 1):
        if common_gcd % i == 0:
            # If i is a divisor, then (common_gcd // i) is also a divisor
            if i * i == common_gcd:
                count += 1
            else:
                count += 2
                
    return count
