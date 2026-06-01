METADATA = {
    "id": 1295,
    "name": "Find Numbers with Even Number of Digits",
    "slug": "find_numbers_with_even_number_of_digits",
    "category": "Array",
    "aliases": [],
    "tags": ["math", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the count of numbers that have an even number of digits.",
}


def solve(nums: list[int]) -> int:
    """Count numbers that contain an even number of digits.

    Args:
        nums: A list of non‑negative integers.

    Returns:
        The count of integers in ``nums`` whose decimal representation has an even
        number of digits.

    Examples:
        >>> solve([12, 345, 2, 6, 7896])
        2
        >>> solve([555, 901, 482, 1771])
        1
    """
    even_digit_count = 0

    for number in nums:
        # Convert the number to a string and check the length parity.
        digit_count = len(str(number))
        if digit_count % 2 == 0:
            even_digit_count += 1

    return even_digit_count