METADATA = {
    "id": 53,
    "name": "Maximum Subarray",
    "slug": "maximum-subarray",
    "category": "Array",
    "aliases": [],
    "tags": ["dynamic_programming", "greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the contiguous subarray within a one-dimensional array of numbers which has the largest sum.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum sum of a contiguous subarray using Kadane's Algorithm.

    Args:
        nums: A list of integers.

    Returns:
        The maximum sum found among all contiguous subarrays.

    Examples:
        >>> solve([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
        >>> solve([1])
        1
        >>> solve([5, 4, -1, 7, 8])
        23
    """
    if not nums:
        return 0

    # current_max tracks the maximum sum ending at the current position
    # global_max tracks the overall maximum sum encountered so far
    current_max = global_max = nums[0]

    for i in range(1, len(nums)):
        # Decision: Either start a new subarray at the current element 
        # or extend the existing subarray ending at the previous element.
        current_max = max(nums[i], current_max + nums[i])
        
        # Update the global maximum if the current subarray sum is larger
        if current_max > global_max:
            global_max = current_max

    return global_max
