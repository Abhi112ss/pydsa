METADATA = {
    "id": 674,
    "name": "Longest Continuous Increasing Subsequence",
    "slug": "longest_continuous_increasing_subsequence",
    "category": "array",
    "aliases": [],
    "tags": ["sliding_window", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest strictly increasing contiguous subarray.",
}


def solve(nums: list[int]) -> int:
    """Return the length of the longest continuous increasing subsequence.

    Args:
        nums: A list of integers.

    Returns:
        The maximum length of a subarray where each element is strictly greater
        than its predecessor. Returns 0 for an empty input list.

    Examples:
        >>> solve([1, 3, 5, 4, 7])
        3
        >>> solve([2, 2, 2, 2, 2])
        1
        >>> solve([])
        0
    """
    if not nums:
        return 0

    max_length = 1
    current_length = 1

    for index in range(1, len(nums)):
        # If the current element continues the increasing streak, extend it.
        if nums[index] > nums[index - 1]:
            current_length += 1
        else:
            # Reset the streak when the increasing property is broken.
            current_length = 1
        # Update the global maximum length if needed.
        if current_length > max_length:
            max_length = current_length

    return max_length