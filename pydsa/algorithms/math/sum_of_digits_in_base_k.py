METADATA = {
    "id": 1837,
    "name": "Sum of Digits in Base K",
    "slug": "sum_of_digits_in_base_k",
    "category": "math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(log_k n)",
    "space_complexity": "O(1)",
    "description": "Return the sum of the digits of n when represented in base k.",
}


def solve(n: int, k: int) -> int:
    """Calculate the sum of digits of ``n`` in base ``k``.

    Args:
        n: A non‑negative integer whose base‑k digit sum is required.
        k: The base (k >= 2).

    Returns:
        The sum of the digits of ``n`` when written in base ``k``.

    Examples:
        >>> solve(13, 3)
        5
        # 13 in base 3 is 111, and 1+1+1 = 3

        >>> solve(100, 10)
        1
        # 100 in base 10 is 100, and 1+0+0 = 1

        >>> solve(0, 2)
        0
    """
    digit_sum: int = 0
    remaining: int = n

    # Extract each base‑k digit using modulo and integer division.
    while remaining > 0:
        digit_sum += remaining % k          # add current least‑significant digit
        remaining //= k                     # shift to next higher digit

    return digit_sum