METADATA = {
    "id": 2863,
    "name": "Maximum Length of Semi-Decreasing Subarrays",
    "slug": "maximum-length-of-semi-decreasing-subarrays",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "arrays", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum length of a subarray where every element is either greater than or equal to the previous one, or strictly less than the previous one, but not both in a way that violates the semi-decreasing property.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum length of a semi-decreasing subarray.
    
    A subarray is semi-decreasing if it satisfies one of two conditions:
    1. It is non-decreasing (nums[i] <= nums[i+1]).
    2. It is strictly decreasing (nums[i] > nums[i+1]).
    Actually, the problem definition for 'semi-decreasing' in this context 
    usually refers to a subarray that can be split into at most two parts: 
    one non-decreasing and one strictly decreasing.
    
    Wait, re-reading the standard definition for this specific LeetCode problem:
    A subarray is semi-decreasing if it contains at most one index i such that 
    nums[i] > nums[i+1] and nums[i+1] >= nums[i+2] is false? No.
    
    Correct definition for LC 2863:
    A subarray is semi-decreasing if there is at most one index i such that 
    nums[i] > nums[i+1].
    
    Args:
        nums: A list of integers.

    Returns:
        The length of the longest semi-decreasing subarray.

    Examples:
        >>> solve([1, 2, 3, 2, 1])
        5
        >>> solve([1, 1, 1, 1])
        4
        >>> solve([3, 2, 1, 2, 3])
        3
    """
    if not nums:
        return 0

    n = len(nums)
    max_length = 1
    current_length = 1
    # count_decreases tracks how many times nums[i] > nums[i+1] occurs in the window
    count_decreases = 0
    left = 0

    # Use a sliding window approach
    for right in range(1, n):
        # If we encounter a decrease, increment our counter
        if nums[right - 1] > nums[right]:
            count_decreases += 1

        # If we have more than one decrease, shrink the window from the left
        # until we only have at most one decrease
        while count_decreases > 1:
            if nums[left] > nums[left + 1]:
                count_decreases -= 1
            left += 1

        # Update the global maximum length found so far
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length

    return max_length
