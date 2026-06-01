METADATA = {
    "id": 2544,
    "name": "Alternating Digit Sum",
    "slug": "alternating_digit_sum",
    "category": "math",
    "aliases": [],
    "tags": ["math", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Compute the alternating sum of the digits of an integer from most significant to least significant.",
}


def solve(n: int) -> int:
    """Compute the alternating digit sum of an integer.

    Args:
        n: A non‑negative integer whose digits will be processed from most
           significant to least significant.

    Returns:
        The result of adding and subtracting the digits alternately, starting
        with addition for the most significant digit.

    Examples:
        >>> solve(521)
        4
        >>> solve(111)
        1
        >>> solve(8866)
        0
    """
    alternating_sum: int = 0
    # Iterate over the string representation to access digits from left to right.
    for index, character in enumerate(str(n)):
        digit: int = int(character)
        if index % 2 == 0:
            alternating_sum += digit  # add for even positions (0‑based)
        else:
            alternating_sum -= digit  # subtract for odd positions
    return alternating_sum