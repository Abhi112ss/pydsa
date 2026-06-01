METADATA = {
    "id": 896,
    "name": "Monotonic Array",
    "slug": "monotonic_array",
    "category": "Array",
    "aliases": ["monotonic array", "is monotonic"],
    "tags": ["iteration"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if the given array is monotonic (either entirely non-increasing or non-decreasing).",
}

def solve(nums: list[int]) -> bool:
    """Determine if the given array is monotonic (either entirely non-increasing or non-decreasing).

    Args:
        nums: A list of integers to check for monotonicity.

    Returns:
        True if the array is monotonic, False otherwise.

    Examples:
        >>> solve([1, 2, 2, 3])
        True
        >>> solve([6, 5, 4, 4])
        True
        >>> solve([1, 3, 2])
        False
    """
    if len(nums) <= 1:
        return True

    # Initialize flags to track if the array is increasing or decreasing
    increasing = True
    decreasing = True

    # Iterate through the array to check for monotonicity
    for index in range(1, len(nums)):
        if nums[index] > nums[index - 1]:
            # If current element is greater than previous, it cannot be decreasing
            decreasing = False
        elif nums[index] < nums[index - 1]:
            # If current element is less than previous, it cannot be increasing
            increasing = False

        # If both flags are False, the array is not monotonic
        if not increasing and not decreasing:
            return False

    # If we reach here, at least one flag is still True, so the array is monotonic
    return True