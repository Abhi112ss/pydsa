METADATA = {
    "id": 1134,
    "name": "Armstrong Number",
    "slug": "armstrong_number",
    "category": "math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Determine whether an integer is an Armstrong number.",
}


def solve(number: int) -> bool:
    """Check if a given integer is an Armstrong number.

    An Armstrong number is an integer such that the sum of its digits each
    raised to the power of the number of digits equals the original number.

    Args:
        number: The integer to be evaluated. It is non‑negative.

    Returns:
        True if `number` is an Armstrong number, otherwise False.

    Examples:
        >>> solve(153)
        True
        >>> solve(123)
        False
        >>> solve(0)
        True
    """
    if number < 0:
        return False

    original_value = number

    # Count the number of digits; handle the special case where number is 0.
    digit_count = 0
    temp = number
    while temp > 0:
        digit_count += 1
        temp //= 10
    if digit_count == 0:  # number is 0
        digit_count = 1

    # Compute the sum of each digit raised to the power of digit_count.
    sum_of_powers = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** digit_count
        temp //= 10

    # For the case number == 0, the loop above does not execute; the sum should be 0^1.
    if original_value == 0:
        sum_of_powers = 0 ** digit_count

    return sum_of_powers == original_value