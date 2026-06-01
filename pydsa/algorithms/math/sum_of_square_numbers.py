METADATA = {
    "id": 633,
    "name": "Sum of Square Numbers",
    "slug": "sum-of-square-numbers",
    "category": "Math",
    "aliases": [],
    "tags": ["two_pointer", "math", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(sqrt(c))",
    "space_complexity": "O(1)",
    "description": "Determine if a non-negative integer c can be expressed as the sum of two squares.",
}

import math

def solve(c: int) -> bool:
    """
    Determines if a non-negative integer c can be expressed as the sum of two squares.

    The algorithm uses a two-pointer approach on the range of possible square roots.
    One pointer starts at 0 and the other starts at the integer square root of c.

    Args:
        c: A non-negative integer.

    Returns:
        True if there exist integers a and b such that a^2 + b^2 = c, False otherwise.

    Examples:
        >>> solve(5)
        True
        >>> solve(3)
        False
    """
    if c < 0:
        return False

    # Initialize two pointers: 
    # left starts at the smallest possible square root (0)
    # right starts at the largest possible square root (floor(sqrt(c)))
    left = 0
    right = int(math.isqrt(c))

    while left <= right:
        current_sum = left * left + right * right
        
        if current_sum == c:
            # Found a pair of squares that sum to c
            return True
        elif current_sum < c:
            # Sum is too small, increment the lower bound to increase the sum
            left += 1
        else:
            # Sum is too large, decrement the upper bound to decrease the sum
            right -= 1

    return False
