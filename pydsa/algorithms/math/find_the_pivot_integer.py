METADATA = {
    "id": 2485,
    "name": "Find the Pivot Integer",
    "slug": "find-the-pivot-integer",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "binary_search"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find an integer x such that the sum of integers from 1 to x is equal to the sum of integers from x to n.",
}

import math

def solve(n: int) -> int:
    """
    Finds the pivot integer x such that the sum of integers from 1 to x 
    is equal to the sum of integers from x to n.

    The problem asks for x where:
    Sum(1 to x) = Sum(x to n)
    x(x + 1) / 2 = (n(n + 1) / 2) - (x(x - 1) / 2) + x (Wait, the sum from x to n includes x once)
    
    Correct derivation:
    Sum(1 to x) = x(x + 1) / 2
    Sum(x to n) = Sum(1 to n) - Sum(1 to x-1)
               = [n(n + 1) / 2] - [(x - 1)x / 2]
    
    Setting them equal:
    x(x + 1) / 2 = [n(n + 1) / 2] - [x(x - 1) / 2]
    Multiply by 2:
    x^2 + x = n(n + 1) - (x^2 - x)
    x^2 + x = n^2 + n - x^2 + x
    2x^2 = n^2 + n
    x^2 = n(n + 1) / 2

    Args:
        n: The upper bound of the range of integers.

    Returns:
        The pivot integer x if it exists, otherwise -1.

    Examples:
        >>> solve(1)
        1
        >>> solve(8)
        6
        >>> solve(10)
        -1
    """
    # Calculate the target value for x^2 based on the derived formula: x^2 = n(n+1)/2
    target_squared = (n * (n + 1)) // 2
    
    # Calculate the integer square root of the target
    pivot_candidate = int(math.isqrt(target_squared))
    
    # Check if the candidate squared actually equals the target
    # This confirms if the target is a perfect square
    if pivot_candidate * pivot_candidate == target_squared:
        return pivot_candidate
    
    return -1
