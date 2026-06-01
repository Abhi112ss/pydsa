METADATA = {
    "id": 504,
    "name": "Base 7",
    "slug": "base_7",
    "category": "math",
    "aliases": [],
    "tags": ["math", "base_conversion"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Convert an integer to its base 7 representation as a string.",
}


def solve(num: int) -> str:
    """Convert an integer to its base 7 representation.

    Args:
        num: The integer to convert. Can be negative, zero, or positive.

    Returns:
        A string representing the base‑7 form of ``num``. Negative numbers
        include a leading ``-`` sign.

    Examples:
        >>> solve(100)
        '202'
        >>> solve(-7)
        '-10'
        >>> solve(0)
        '0'
    """
    # Zero is a special case because the loop would produce an empty string.
    if num == 0:
        return "0"

    is_negative = num < 0
    remaining = -num if is_negative else num

    digits: list[str] = []
    # Repeatedly extract the least‑significant base‑7 digit.
    while remaining > 0:
        digits.append(str(remaining % 7))
        remaining //= 7

    # Digits were collected in reverse order; reverse them to obtain the correct string.
    base7_str = "".join(reversed(digits))

    return f"-{base7_str}" if is_negative else base7_str