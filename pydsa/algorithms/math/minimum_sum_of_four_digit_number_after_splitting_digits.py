METADATA = {
    "id": 2160,
    "name": "Minimum Sum of Four Digit Number After Splitting Digits",
    "slug": "minimum_sum_of_four_digit_number_after_splitting_digits",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Return the minimum possible sum of two numbers formed by splitting the digits of a four‑digit integer.",
}


def solve(num: int) -> int:
    """Return the minimum sum of two two‑digit numbers formed from the digits of ``num``.

    Args:
        num: A four‑digit integer (1000 ≤ num ≤ 9999).

    Returns:
        The smallest possible sum of two numbers created by using each digit exactly once.

    Examples:
        >>> solve(2932)
        52
        >>> solve(4009)
        13
    """
    # Extract each digit of the four‑digit number.
    digit_thousands = num // 1000
    digit_hundreds = (num // 100) % 10
    digit_tens = (num // 10) % 10
    digit_ones = num % 10

    # Sort digits to pair the smallest with the smallest tens place.
    sorted_digits = sorted([digit_thousands, digit_hundreds, digit_tens, digit_ones])

    # Form the two numbers: smallest digit as tens of first number, next smallest as tens of second.
    first_number = sorted_digits[0] * 10 + sorted_digits[2]
    second_number = sorted_digits[1] * 10 + sorted_digits[3]

    # The sum of these two numbers is the minimal possible sum.
    return first_number + second_number