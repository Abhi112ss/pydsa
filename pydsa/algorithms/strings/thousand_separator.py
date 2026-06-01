METADATA = {
    "id": 1556,
    "name": "Thousand Separator",
    "slug": "thousand_separator",
    "category": "String",
    "aliases": [],
    "tags": ["strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Convert an integer to a string with commas separating every three digits.",
}


def solve(n: int) -> str:
    """Convert an integer to a string with commas inserted every three digits.

    Args:
        n: A non‑negative integer.

    Returns:
        A string representation of *n* with commas separating each group of three
        digits from the right.

    Examples:
        >>> solve(123456789)
        '123,456,789'
        >>> solve(0)
        '0'
    """
    number_str = str(n)  # original decimal representation
    reversed_chars = []  # will hold characters in reverse order

    # Iterate over the digits from right to left, inserting commas after every three digits
    for position, digit in enumerate(reversed(number_str)):
        if position and position % 3 == 0:
            reversed_chars.append(',')  # insert thousand separator
        reversed_chars.append(digit)

    # Reverse the list to obtain the correctly ordered string
    return ''.join(reversed(reversed_chars))