METADATA = {
    "id": 1608,
    "name": "Special Array With X Elements Greater Than or Equal X",
    "slug": "special_array_with_x_elements_greater_than_or_equal_x",
    "category": "array",
    "aliases": [],
    "tags": ["sorting", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find an integer X such that exactly X elements in the array are greater than or equal to X.",
}


def solve(nums: list[int]) -> int:
    """Return the special number X for the given list.

    Args:
        nums: List of integers.

    Returns:
        The integer X such that exactly X elements in `nums` are greater than or
        equal to X. If no such X exists, returns -1.

    Examples:
        >>> solve([0, 4, 3, 0, 4])
        3
        >>> solve([3, 5])
        -1
        >>> solve([-3, -2, -1])
        0
    """
    length = len(nums)
    if length == 0:
        return -1

    # Sort in‑place to enable binary‑search‑like checks.
    nums.sort()

    # Iterate over each possible candidate X = length - index.
    for index, value in enumerate(nums):
        candidate = length - index
        # Ensure this is the first position where value >= candidate.
        if value >= candidate and (index == 0 or nums[index - 1] < candidate):
            return candidate

    # Special case: X = 0 is valid only when all numbers are negative.
    if nums[-1] < 0:
        return 0

    return -1