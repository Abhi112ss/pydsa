METADATA = {
    "id": 389,
    "name": "Find the Difference",
    "slug": "find_the_difference",
    "category": "String",
    "aliases": [],
    "tags": ["bit_manipulation", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the extra character in t that is not present in s.",
}


def solve(s: str, t: str) -> str:
    """Find the extra character in string ``t`` that is not present in ``s``.

    Args:
        s: The original string.
        t: The string formed by adding one extra character to ``s``.

    Returns:
        The extra character that appears in ``t`` but not in ``s``.

    Examples:
        >>> solve("abcd", "abcde")
        'e'
        >>> solve("", "z")
        'z'
    """
    xor_result: int = 0
    # XOR all characters from the original string.
    for character in s:
        xor_result ^= ord(character)  # combine with current XOR accumulator
    # XOR all characters from the modified string, which includes the extra character.
    for character in t:
        xor_result ^= ord(character)  # extra character remains after cancellation
    return chr(xor_result)