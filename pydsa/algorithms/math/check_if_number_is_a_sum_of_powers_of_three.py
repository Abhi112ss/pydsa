METADATA = {
    "id": 1780,
    "name": "Check if Number is a Sum of Powers of Three",
    "slug": "check_if_number_is_a_sum_of_powers_of_three",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(log₃ n)",
    "space_complexity": "O(1)",
    "description": "Determine whether a non‑negative integer can be expressed as a sum of distinct powers of three.",
}


def solve(number: int) -> bool:
    """Check if a non‑negative integer is a sum of distinct powers of three.

    Args:
        number: The integer to evaluate (0 ≤ number ≤ 10⁹).

    Returns:
        True if the integer can be represented as a sum of distinct powers of three,
        otherwise False.

    Examples:
        >>> solve(12)
        True  # 12 = 3¹ + 3²
        >>> solve(91)
        False # contains a digit '2' in base‑3 representation
    """
    # Repeatedly examine the least‑significant digit in base‑3.
    while number > 0:
        if number % 3 == 2:  # digit '2' indicates the need for a repeated power of three
            return False
        number //= 3
    return True