METADATA = {
    "id": 1749,
    "name": "Maximum Absolute Sum of Any Subarray",
    "slug": "maximum-absolute-sum-of-any-subarray",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "kadane_algorithm", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum absolute sum of any contiguous subarray within a given integer array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum absolute sum of any contiguous subarray.

    The maximum absolute sum is equivalent to the difference between the 
    maximum prefix sum and the minimum prefix sum encountered during a 
    single pass through the array.

    Args:
        nums: A list of integers.

    Returns:
        The maximum absolute sum found.

    Examples:
        >>> solve([1, -3])
        4
        >>> solve([2, -5, 1, -4, 3, -2])
        8
    """
    # The maximum absolute sum of a subarray [i, j] is |sum(nums[i...j])|.
    # This can be expressed as |prefix_sum[j] - prefix_sum[i-1]|.
    # To maximize this, we find the difference between the global maximum 
    # prefix sum and the global minimum prefix sum.

    max_prefix_sum = 0
    min_prefix_sum = 0
    current_running_sum = 0

    for num in nums:
        current_running_sum += num
        
        # Track the highest and lowest prefix sums seen so far
        if current_running_sum > max_prefix_sum:
            max_prefix_sum = current_running_sum
        if current_running_sum < min_prefix_sum:
            min_prefix_sum = current_running_sum

    # The maximum absolute difference between any two prefix sums
    # (including the implicit 0 at the start) gives the result.
    return max_prefix_sum - min_prefix_sum
