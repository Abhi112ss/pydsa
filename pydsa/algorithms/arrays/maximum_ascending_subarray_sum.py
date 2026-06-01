METADATA = {
    "id": 1800,
    "name": "Maximum Ascending Subarray Sum",
    "slug": "maximum-ascending-subarray-sum",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "array_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum sum of a contiguous subarray where each element is strictly greater than the previous one.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum sum of an ascending subarray within the given list.

    An ascending subarray is a contiguous sequence of elements where each 
    element is strictly greater than the one preceding it.

    Args:
        nums: A list of integers.

    Returns:
        The maximum sum found among all ascending subarrays.

    Examples:
        >>> solve([10, 20, 30, 5, 10, 50])
        60
        >>> solve([10, 20, 30, 40, 50])
        150
        >>> solve([100])
        100
    """
    if not nums:
        return 0

    max_sum = nums[0]
    current_subarray_sum = nums[0]

    for i in range(1, len(nums)):
        # Check if the current element continues the ascending sequence
        if nums[i] > nums[i - 1]:
            current_subarray_sum += nums[i]
        else:
            # Sequence broken, reset the current sum to the current element
            current_subarray_sum = nums[i]
        
        # Update the global maximum sum found so far
        if current_subarray_sum > max_sum:
            max_sum = current_subarray_sum

    return max_sum
