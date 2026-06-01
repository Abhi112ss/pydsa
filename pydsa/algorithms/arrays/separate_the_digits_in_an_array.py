METADATA = {
    "id": 2553,
    "name": "Separate the Digits in an Array",
    "slug": "separate_the_digits_in_an_array",
    "category": "array",
    "aliases": [],
    "tags": ["arrays", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n * log10(max(nums)))",
    "space_complexity": "O(n * log10(max(nums)))",
    "description": "Return an array of the digits of each number in the given array, preserving order.",
}

def solve(nums: list[int]) -> list[int]:
    """Separate the digits of each integer in the input list.

    Args:
        nums: A list of non‑negative integers.

    Returns:
        A list containing the digits of each integer from ``nums`` in the same order.

    Examples:
        >>> solve([13, 25, 83, 77])
        [1, 3, 2, 5, 8, 3, 7, 7]
        >>> solve([0, 5, 100])
        [0, 5, 1, 0, 0]
    """
    result: list[int] = []
    for number in nums:
        # Convert the number to a string to iterate over its digits in order.
        for digit_char in str(number):
            # Append each digit as an integer to the result list.
            result.append(int(digit_char))
    return result