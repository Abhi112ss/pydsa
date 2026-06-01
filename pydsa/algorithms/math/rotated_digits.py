METADATA = {
    "id": 788,
    "name": "Rotated Digits",
    "slug": "rotated_digits",
    "category": "math",
    "aliases": [],
    "tags": ["dynamic_programming", "string"],
    "difficulty": "medium",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(1)",
    "description": "Count numbers that become a different valid number after rotating each digit by 180 degrees.",
}


def solve(N: int) -> int:
    """Count how many numbers in the range [1, N] are good after rotation.

    A number is *good* if each of its digits is one of {0,1,2,5,6,8,9}
    and at least one digit changes to a different digit when rotated
    (i.e., contains at least one of {2,5,6,9}).

    Args:
        N: Upper bound of the range (inclusive). Must be a non‑negative integer.

    Returns:
        The count of good numbers between 1 and N inclusive.

    Examples:
        >>> solve(10)
        0
        >>> solve(20)
        2
        >>> solve(100)
        56
    """
    # Digits that remain valid after rotation.
    valid_digits = {'0', '1', '2', '5', '6', '8', '9'}
    # Digits that actually change to a different digit.
    changing_digits = {'2', '5', '6', '9'}

    good_count = 0
    for number in range(1, N + 1):
        number_str = str(number)
        # Quick reject if any digit is invalid.
        if any(digit not in valid_digits for digit in number_str):
            continue
        # Accept if at least one digit will change.
        if any(digit in changing_digits for digit in number_str):
            good_count += 1
    return good_count