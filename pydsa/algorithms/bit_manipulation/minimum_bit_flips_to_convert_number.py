METADATA = {
    "id": 2220,
    "name": "Minimum Bit Flips to Convert Number",
    "slug": "minimum_bit_flips_to_convert_number",
    "category": "algorithms",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Return the minimum number of bit flips required to convert start to goal.",
}


def solve(start: int, goal: int) -> int:
    """Calculate the minimum number of bit flips to convert one integer to another.

    Args:
        start: The initial integer value.
        goal: The target integer value.

    Returns:
        The count of bits that differ between start and goal.

    Examples:
        >>> solve(10, 20)
        4
        >>> solve(0, 0)
        0
        >>> solve(1, 2)
        2
    """
    # XOR highlights bits that differ between start and goal.
    differing_bits = start ^ goal
    # Count the number of set bits in the XOR result.
    flip_count = bin(differing_bits).count('1')
    return flip_count