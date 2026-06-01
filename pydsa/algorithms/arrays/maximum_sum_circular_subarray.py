METADATA = {
    "id": 918,
    "name": "Maximum Sum Circular Subarray",
    "slug": "maximum-sum-circular-subarray",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["kadane", "dynamic_programming", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum possible sum of a non-empty subarray of a circular array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum sum of a non-empty subarray in a circular array.

    The maximum sum can occur in two cases:
    1. The maximum subarray is a standard contiguous subarray (found via Kadane's).
    2. The maximum subarray wraps around the end of the array. This is equivalent 
       to (Total Sum - Minimum Subarray Sum).

    Args:
        nums: A list of integers representing the circular array.

    Returns:
        The maximum sum of a non-empty subarray.

    Examples:
        >>> solve([1, -2, 3, -2])
        3
        >>> solve([5, -3, 5])
        10
        >>> solve([-3, -2, -3])
        -2
    """
    if not nums:
        return 0

    # Initialize variables for Kadane's (max) and inverse Kadane's (min)
    current_max = 0
    max_sum = nums[0]
    current_min = 0
    min_sum = nums[0]
    total_sum = 0

    for x in nums:
        # Standard Kadane's to find the maximum contiguous subarray sum
        current_max = max(x, current_max + x)
        max_sum = max(max_sum, current_max)

        # Inverse Kadane's to find the minimum contiguous subarray sum
        current_min = min(x, current_min + x)
        min_sum = min(min_sum, current_min)

        total_sum += x

    # If max_sum is negative, all numbers in the array are negative.
    # In this case, the circular sum (total_sum - min_sum) would result in 0 
    # (an empty subarray), which is not allowed. We must return the max_sum.
    if max_sum < 0:
        return max_sum

    # The result is the maximum of the non-circular max and the circular max
    return max(max_sum, total_sum - min_sum)
