METADATA = {
    "id": 625,
    "name": "Minimum Factorization",
    "slug": "minimum-factorization",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of single-digit factors that multiply to a given integer n.",
}

def solve(n: int) -> int:
    """
    Finds the minimum number of single-digit factors (2-9) that multiply to n.

    The strategy is to greedily divide the number by the largest possible 
    single-digit factors (starting from 9 down to 2) to minimize the count.

    Args:
        n: The target integer to factorize.

    Returns:
        The minimum number of single-digit factors. Returns -1 if no such 
        factorization exists.

    Examples:
        >>> solve(12)
        2  # (6 * 2 or 4 * 3 or 3 * 2 * 2 -> min is 2)
        >>> solve(13)
        -1 # (Prime > 7)
        >>> solve(100)
        3  # (5 * 5 * 4)
    """
    if n == 1:
        return 0

    count = 0
    current_n = n

    # Iterate from the largest single-digit factor down to 2
    for factor in range(9, 1, -1):
        # Greedily extract as many of the current factor as possible
        while current_n % factor == 0:
            current_n //= factor
            count += 1
            
    # If current_n is not 1, it means there's a prime factor > 7
    if current_n > 1:
        return -1
        
    return count
