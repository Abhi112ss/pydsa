METADATA = {
    "id": 3423,
    "name": "Maximum Difference Between Adjacent Elements in a Circular Array",
    "slug": "maximum_difference_between_adjacent_elements_in_a_circular_array",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "circular_array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum absolute difference between any two adjacent elements in a circular array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum absolute difference between adjacent elements in a circular array.

    Args:
        nums: A list of integers representing the circular array.

    Returns:
        The maximum absolute difference found between any two adjacent elements.

    Examples:
        >>> solve([1, 2, 3, 4])
        1
        >>> solve([1, 10, 2, 5])
        9
        >>> solve([5, 1, 5])
        4
    """
    n = len(nums)
    if n < 2:
        return 0

    max_diff = 0

    # Iterate through the array to check adjacent pairs (i, i+1)
    for i in range(n - 1):
        current_diff = abs(nums[i] - nums[i + 1])
        if current_diff > max_diff:
            max_diff = current_diff

    # Check the wrap-around case: the difference between the last and first element
    wrap_around_diff = abs(nums[n - 1] - nums[0])
    if wrap_around_diff > max_diff:
        max_diff = wrap_around_diff

    return max_diff
