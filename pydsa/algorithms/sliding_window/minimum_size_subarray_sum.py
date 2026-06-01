METADATA = {
    "id": 209,
    "name": "Minimum Size Subarray Sum",
    "slug": "minimum_size_subarray_sum",
    "category": "Sliding Window",
    "aliases": ["min_sub_array_len"],
    "tags": ["sliding_window", "two_pointer", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimal length of a contiguous subarray whose sum is at least target.",
}

def solve(target: int, nums: list[int]) -> int:
    """Find the minimal length of a contiguous subarray with sum >= target.

    Uses a sliding window approach: expand the right boundary until the window sum
    meets or exceeds target, then shrink from the left to find the minimum length.

    Args:
        target: The minimum sum required.
        nums: List of positive integers.

    Returns:
        The minimal length of a contiguous subarray with sum >= target,
        or 0 if no such subarray exists.

    Examples:
        >>> solve(7, [2, 3, 1, 2, 4, 3])
        2
        >>> solve(4, [1, 4, 4])
        1
        >>> solve(11, [1, 1, 1, 1, 1, 1, 1, 1])
        0
    """
    min_length = float('inf')
    window_sum = 0
    left = 0

    for right in range(len(nums)):
        # Expand window by including the right element
        window_sum += nums[right]

        # Shrink window from the left while the sum is sufficient
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0