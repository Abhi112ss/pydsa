METADATA = {
    "id": 2555,
    "name": "Maximize Win From Two Segments",
    "slug": "maximize-win-from-two-segments",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "prefix_sum", "sliding_window"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum of two non-overlapping subarrays of length k in an integer array.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum sum of two non-overlapping subarrays of length k.

    The strategy uses dynamic programming to precompute the maximum sum of a 
    subarray of length k ending at or before each index (prefix max) and 
    the maximum sum of a subarray of length k starting at or after each index (suffix max).
    Then, we iterate through all possible split points to find the maximum combined sum.

    Args:
        nums: A list of integers representing the array.
        k: The fixed length of the two subarrays.

    Returns:
        The maximum sum of two non-overlapping subarrays of length k.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        14  # [2, 3] and [4, 5] -> 5 + 9 = 14
        >>> solve([1, 1, 1, 1, 1], 2)
        4   # [1, 1] and [1, 1] -> 2 + 2 = 4
    """
    n = len(nums)
    if n < 2 * k:
        return 0

    # pre_max[i] stores the maximum sum of a subarray of length k 
    # that ends at or before index i.
    pre_max = [0] * n
    current_window_sum = sum(nums[:k])
    pre_max[k - 1] = current_window_sum

    for i in range(k, n):
        # Slide the window to calculate the sum of the subarray ending at i
        current_window_sum += nums[i] - nums[i - k]
        # The max sum ending at or before i is either the max sum ending before i
        # or the sum of the current window ending at i.
        pre_max[i] = max(pre_max[i - 1], current_window_sum)

    # suf_max[i] stores the maximum sum of a subarray of length k 
    # that starts at or after index i.
    suf_max = [0] * n
    current_window_sum = sum(nums[n - k:])
    suf_max[n - k] = current_window_sum

    for i in range(n - k - 1, -1, -1):
        # Slide the window backwards to calculate the sum of the subarray starting at i
        current_window_sum += nums[i] - nums[i + k]
        # The max sum starting at or after i is either the max sum starting after i
        # or the sum of the current window starting at i.
        suf_max[i] = max(suf_max[i + 1], current_window_sum)

    max_total_win = 0
    # Iterate through all possible split points. 
    # A split point 'i' means the first subarray ends at or before 'i'
    # and the second subarray starts at or after 'i + 1'.
    for i in range(k - 1, n - k):
        max_total_win = max(max_total_win, pre_max[i] + suf_max[i + 1])

    return max_total_win
