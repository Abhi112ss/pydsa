METADATA = {
    "id": 3738,
    "name": "Longest Non-Decreasing Subarray After Replacing at Most One Element",
    "slug": "longest_non_decreasing_subarray_after_replacing_at_most_one_element",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest non-decreasing subarray possible by changing at most one element in the array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest non-decreasing subarray after replacing at most one element.

    The strategy uses a sliding window approach. A window is valid if we can make it 
    non-decreasing by changing at most one element. However, a simple "at most one 
    violation" check is insufficient because changing one element must satisfy 
    both its left and right neighbors. 
    
    A more robust way to view this is: we are looking for the longest subarray 
    that consists of two non-decreasing segments joined by a single modification.
    
    Args:
        nums: A list of integers.

    Returns:
        The length of the longest non-decreasing subarray after at most one replacement.

    Examples:
        >>> solve([1, 2, 1, 2, 3])
        5
        >>> solve([5, 4, 3, 2, 1])
        2
        >>> solve([1, 1, 1, 1])
        4
    """
    n = len(nums)
    if n <= 1:
        return n

    # pre_inc[i] stores the length of the non-decreasing subarray ending at i
    pre_inc = [1] * n
    for i in range(1, n):
        if nums[i] >= nums[i - 1]:
            pre_inc[i] = pre_inc[i - 1] + 1

    # post_inc[i] stores the length of the non-decreasing subarray starting at i
    post_inc = [1] * n
    for i in range(n - 2, -1, -1):
        if nums[i] <= nums[i + 1]:
            post_inc[i] = post_inc[i + 1] + 1

    # The base answer is the maximum length of any existing non-decreasing subarray + 1
    # (clamped to n), because we can always extend any non-decreasing subarray by 1 
    # by changing the adjacent element, provided there is an adjacent element.
    max_len = 0
    for i in range(n):
        # Case 1: The subarray is already non-decreasing
        max_len = max(max_len, pre_inc[i])
        # Case 2: Extend an existing non-decreasing subarray by 1
        if i + 1 < n:
            max_len = max(max_len, pre_inc[i] + 1)
        if i - 1 >= 0:
            max_len = max(max_len, post_inc[i] + 1)

    # Case 3: Connect two non-decreasing segments by changing nums[i]
    # We iterate through every index i and check if changing nums[i] can bridge 
    # the segment ending at i-1 and the segment starting at i+1.
    for i in range(1, n - 1):
        # To bridge nums[i-1] and nums[i+1] by changing nums[i],
        # we need nums[i-1] <= nums[i+1].
        # If this holds, the new length is pre_inc[i-1] + 1 + post_inc[i+1].
        if nums[i - 1] <= nums[i + 1]:
            max_len = max(max_len, pre_inc[i - 1] + 1 + post_inc[i + 1])

    return min(max_len, n)
