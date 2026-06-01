METADATA = {
    "id": 717,
    "name": "1-bit and 2-bit Characters",
    "slug": "1_bit_and_2_bit_characters",
    "category": "Algorithms",
    "aliases": ["One Bit and Two Bit Characters"],
    "tags": ["array", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine whether the final character in a bit sequence is a 1-bit character.",
}


def solve(bits: list[int]) -> bool:
    """Determine if the last character in the bit sequence is a 1-bit character.

    Args:
        bits: A list of integers (0 or 1) representing the encoded characters.
               The sequence always ends with a 0.

    Returns:
        True if the last character is a 1-bit character, False otherwise.

    Examples:
        >>> solve([1, 0, 0])
        True
        >>> solve([1, 1, 1, 0])
        False
    """
    index: int = 0
    last_position: int = len(bits) - 1

    # Walk through the array, skipping 1 step for '0' and 2 steps for '1'
    while index < last_position:
        if bits[index] == 0:
            index += 1  # 1-bit character
        else:
            index += 2  # 2-bit character

    # If we land exactly on the last element, it must be a 1-bit character
    return index == last_position