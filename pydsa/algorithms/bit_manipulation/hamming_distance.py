METADATA = {
    "id": 461,
    "name": "Hamming Distance",
    "slug": "hamming_distance",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit manipulation", "xor"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Returns the number of positions at which the corresponding bits are different.",
}


def solve(x: int, y: int) -> int:
    """Calculate the Hamming distance between two integers.

    Args:
        x: First non‑negative integer.
        y: Second non‑negative integer.

    Returns:
        The number of bit positions where `x` and `y` differ.

    Examples:
        >>> solve(1, 4)
        2
        >>> solve(0, 0)
        0
        >>> solve(15, 0)
        4
    """
    xor_result = x ^ y  # bits that differ between x and y
    # Use built‑in bit_count if available (Python 3.8+), otherwise fall back to Kernighan's method
    try:
        return xor_result.bit_count()
    except AttributeError:
        count = 0
        while xor_result:
            xor_result &= xor_result - 1  # clear the least‑significant set bit
            count += 1
        return count