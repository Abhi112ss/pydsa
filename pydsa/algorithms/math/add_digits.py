METADATA = {
    "id": 258,
    "name": "Add Digits",
    "slug": "add_digits",
    "category": "Math",
    "aliases": ["Digital Root"],
    "tags": ["math", "number_theory"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.",
}

def solve(num: int) -> int:
    """Return the digital root of a non-negative integer.

    The digital root is the single-digit value obtained by repeatedly summing
    the digits of a number until only one digit remains. This can be computed
    in O(1) time using the congruence formula for digital roots.

    Args:
        num: A non-negative integer whose digital root is to be computed.

    Returns:
        The digital root of the given number, which is a single digit from 0 to 9.

    Examples:
        >>> solve(38)
        2
        >>> solve(0)
        0
        >>> solve(9)
        9
        >>> solve(12345)
        6
    """
    # Special case: the digital root of 0 is 0, not handled by the formula directly
    if num == 0:
        return 0

    # The digital root formula: 1 + (num - 1) % 9
    # This works because the digital root cycles every 9 numbers (mod 9 arithmetic)
    # Subtracting 1 before mod and adding 1 after handles the edge case where num is a multiple of 9
    return 1 + (num - 1) % 9