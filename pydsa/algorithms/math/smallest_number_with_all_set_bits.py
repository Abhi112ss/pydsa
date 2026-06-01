METADATA = {
    "id": 3370,
    "name": "Smallest Number With All Set Bits",
    "slug": "smallest-number-with-all-set-bits",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the smallest number that has all bits set up to a certain position.",
}

def solve(n: int) -> int:
    """
    Calculates the smallest number that has all bits set from position 0 to n.

    A number with all bits set from 0 to n is equivalent to a sequence of (n + 1) 
    ones in binary. This is mathematically represented as 2^(n+1) - 1.

    Args:
        n (int): The highest bit position (0-indexed) that must be set.

    Returns:
        int: The smallest integer with all bits from 0 to n set to 1.

    Examples:
        >>> solve(0)
        1
        >>> solve(1)
        3
        >>> solve(2)
        7
    """
    # The number of bits to be set is (n + 1).
    # A number with k bits set is (1 << k) - 1.
    # For example, if n=2, we need 3 bits set (111 in binary), which is 2^3 - 1 = 7.
    return (1 << (n + 1)) - 1