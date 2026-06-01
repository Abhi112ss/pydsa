METADATA = {
    "id": 231,
    "name": "Power of Two",
    "slug": "power_of_two",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Given an integer n, return true if it is a power of two, otherwise return false.",
}

def solve(n: int) -> bool:
    """Determine if a given integer is a power of two.

    A power of two has exactly one bit set in its binary representation.
    Using the bit trick: n & (n - 1) clears the lowest set bit, so if n is a
    power of two, the result is zero. We also require n > 0 since 0 and negatives
    are not powers of two.

    Args:
        n: The integer to check.

    Returns:
        True if n is a power of two, False otherwise.

    Examples:
        >>> solve(1)
        True
        >>> solve(16)
        True
        >>> solve(3)
        False
        >>> solve(0)
        False
        >>> solve(-2)
        False
    """
    # n must be positive, and n & (n - 1) must be 0 (exactly one bit set)
    return n > 0 and (n & (n - 1)) == 0