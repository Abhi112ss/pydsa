METADATA = {
    "id": 2520,
    "name": "Count the Digits That Divide a Number",
    "slug": "count_the_digits_that_divide_a_number",
    "category": "math",
    "aliases": [],
    "tags": ["math", "implementation"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Count how many digits of an integer evenly divide the integer itself.",
}


def solve(num: int) -> int:
    """Count the digits of ``num`` that divide ``num`` without remainder.

    Args:
        num: A positive integer whose digits are examined.

    Returns:
        The count of non‑zero digits that evenly divide ``num``.

    Examples:
        >>> solve(7)
        1
        >>> solve(121)
        2
        >>> solve(1012)
        3
    """
    original_number: int = num
    count: int = 0

    while num > 0:
        digit: int = num % 10  # extract the least‑significant digit
        if digit != 0 and original_number % digit == 0:
            count += 1  # digit divides the original number
        num //= 10  # move to the next digit

    return count