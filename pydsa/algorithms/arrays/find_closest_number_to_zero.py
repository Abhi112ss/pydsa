METADATA = {
    "id": 2239,
    "name": "Find Closest Number to Zero",
    "slug": "find_closest_number_to_zero",
    "category": "array",
    "aliases": [],
    "tags": ["arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the integer in the array whose absolute value is smallest, preferring the larger number when a tie occurs.",
}


def solve(nums: list[int]) -> int:
    """Return the integer whose absolute value is closest to zero.

    Args:
        nums: A list of integers (may contain positive, negative, and zero).

    Returns:
        The integer with the smallest absolute value. If two numbers have the same
        absolute value, the larger (i.e., more positive) number is returned.

    Examples:
        >>> solve([-4, -2, 1, 4, 8])
        1
        >>> solve([7, -10, 13, 8, 4])
        4
        >>> solve([-5, 5])
        5
    """
    # Initialize with the first element as the current best candidate.
    closest_number = nums[0]

    for number in nums:
        # Compare absolute values; if equal, prefer the larger number.
        if abs(number) < abs(closest_number) or (abs(number) == abs(closest_number) and number > closest_number):
            closest_number = number

    return closest_number