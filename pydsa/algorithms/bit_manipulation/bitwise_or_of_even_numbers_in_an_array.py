METADATA = {
    "id": 3688,
    "name": "Bitwise OR of Even Numbers in an Array",
    "slug": "bitwise_or_of_even_numbers_in_an_array",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the bitwise OR of all even numbers present in a given integer array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the bitwise OR of all even numbers in the provided list.

    Args:
        nums: A list of integers.

    Returns:
        The bitwise OR result of all even numbers. Returns 0 if no even numbers exist.

    Examples:
        >>> solve([1, 2, 4, 7])
        6
        >>> solve([1, 3, 5])
        0
        >>> solve([10, 20, 30])
        30
    """
    result = 0
    even_found = False

    for num in nums:
        # Check if the number is even using bitwise AND with 1
        # (num & 1 == 0) is equivalent to (num % 2 == 0)
        if num % 2 == 0:
            result |= num
            even_found = True

    # If no even numbers were found, the problem context usually implies 0
    return result if even_found else 0
