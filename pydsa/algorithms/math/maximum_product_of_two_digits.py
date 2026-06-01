METADATA = {
    "id": 3536,
    "name": "Maximum Product of Two Digits",
    "slug": "maximum-product-of-two-digits",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "arrays", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum product possible by multiplying two digits from a given array.",
}

def solve(digits: list[int]) -> int:
    """
    Finds the maximum product of any two digits in the provided list.

    The algorithm identifies the two largest digits in a single pass to 
    ensure the maximum possible product is calculated.

    Args:
        digits: A list of integers where each integer is a single digit (0-9).

    Returns:
        The maximum product of two digits from the list.

    Examples:
        >>> solve([1, 2, 3, 4])
        12
        >>> solve([9, 0, 5, 9])
        81
        >>> solve([1, 1])
        1
    """
    if len(digits) < 2:
        return 0

    # Initialize the two largest values found so far
    max_digit_one = -1
    max_digit_two = -1

    for digit in digits:
        # If current digit is larger than the largest found so far
        if digit > max_digit_one:
            # Shift the current largest to second largest
            max_digit_two = max_digit_one
            max_digit_one = digit
        # If current digit is larger than the second largest
        elif digit > max_digit_two:
            max_digit_two = digit

    # The maximum product is the product of the two largest digits
    return max_digit_one * max_digit_two
