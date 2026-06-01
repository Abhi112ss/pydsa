METADATA = {
    "id": 201,
    "name": "Bitwise AND of Numbers Range",
    "slug": "bitwise_and_of_numbers_range",
    "category": "Bit Manipulation",
    "aliases": ["bitwise-and-of-numbers-range"],
    "tags": ["bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Compute the bitwise AND of all numbers in the range [left, right].",
}

def solve(left: int, right: int) -> int:
    """Compute the bitwise AND of all numbers in the range [left, right].

    The key insight is that the result is the common prefix of the binary
    representations of left and right, with zeros padded to the right.

    Args:
        left (int): The start of the range.
        right (int): The end of the range.

    Returns:
        int: The bitwise AND of all numbers in the range [left, right].

    Examples:
        >>> solve(5, 7)
        4
        >>> solve(0, 0)
        0
        >>> solve(1, 2147483647)
        0
    """
    shift = 0
    # Find the common prefix by shifting right until left == right
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    # Shift back to get the common prefix with zeros padded to the right
    return left << shift