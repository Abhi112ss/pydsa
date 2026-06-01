METADATA = {
    "id": 2283,
    "name": "Check if Number Has Equal Digit Count and Digit Value",
    "slug": "check_if_number_has_equal_digit_count_and_digit_value",
    "category": "math",
    "aliases": [],
    "tags": ["math", "array"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Determine whether each digit i in the decimal representation of num appears exactly i times.",
}


def solve(num: int) -> bool:
    """Check if a number has equal digit count and digit value.

    Args:
        num: A non‑negative integer to be examined.

    Returns:
        True if for every digit i (0‑9) that appears in the decimal representation of
        ``num`` the count of i equals i; otherwise False.

    Examples:
        >>> solve(1223334444)
        True
        >>> solve(123)
        False
        >>> solve(0)
        False
    """
    # Special case: the representation "0" contains digit 0 once, which violates the rule.
    if num == 0:
        return False

    digit_counts: list[int] = [0] * 10  # fixed‑size array for digits 0‑9

    # Extract each digit and count its occurrences.
    while num > 0:
        digit = num % 10
        digit_counts[digit] += 1
        num //= 10

    # Verify that each non‑zero count matches its digit value.
    for digit_value, count in enumerate(digit_counts):
        if count != 0 and count != digit_value:
            return False
    return True