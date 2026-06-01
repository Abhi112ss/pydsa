METADATA = {
    "id": 485,
    "name": "Max Consecutive Ones",
    "slug": "max_consecutive_ones",
    "category": "array",
    "aliases": [],
    "tags": ["array", "iteration"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest subarray of 1's.",
}


def solve(nums: list[int]) -> int:
    """Return the maximum number of consecutive 1's in the given list.

    Args:
        nums: A list of integers containing only 0s and 1s.

    Returns:
        The length of the longest contiguous subarray consisting solely of 1's.

    Examples:
        >>> solve([1, 1, 0, 1, 1, 1])
        3
        >>> solve([0, 0, 0])
        0
        >>> solve([1, 1, 1, 1])
        4
    """
    max_streak = 0
    current_streak = 0
    for value in nums:
        if value == 1:
            current_streak += 1  # extend the current run of 1's
            if current_streak > max_streak:
                max_streak = current_streak  # update maximum if needed
        else:
            current_streak = 0  # reset when a 0 is encountered
    return max_streak