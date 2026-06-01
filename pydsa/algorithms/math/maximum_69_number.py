METADATA = {
    "id": 1323,
    "name": "Maximum 69 Number",
    "slug": "maximum_69_number",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Replace the leftmost digit 6 with 9 to maximize the integer.",
}


def solve(num: int) -> int:
    """Return the maximum number obtainable by changing at most one digit 6 to 9.

    Args:
        num: A positive integer consisting only of digits 6 and 9.

    Returns:
        The largest possible integer after at most one replacement of a digit 6 with 9.

    Examples:
        >>> solve(9669)
        9969
        >>> solve(9996)
        9999
        >>> solve(9999)
        9999
    """
    # Convert the number to a mutable list of characters.
    digits: list[str] = list(str(num))

    # Find the first occurrence of '6' and replace it with '9'.
    for index, digit in enumerate(digits):
        if digit == '6':
            digits[index] = '9'
            break  # Only one replacement is allowed.

    # Reconstruct the integer from the possibly modified digit list.
    return int(''.join(digits))