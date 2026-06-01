METADATA = {
    "id": 1658,
    "name": "Minimum Operations to Reduce X to Zero",
    "slug": "minimum-operations-to-reduce-x-to-zero",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of elements to remove from the ends of an array to make their sum equal to x.",
}

def solve(nums: list[int], x: int) -> int:
    """
    Finds the minimum number of operations to reduce x to zero by removing elements from ends.

    The problem is equivalent to finding the longest contiguous subarray whose sum 
    is equal to (total_sum - x).

    Args:
        nums: A list of positive integers.
        x: The target value to reduce to zero.

    Returns:
        The minimum number of operations, or -1 if it is impossible.

    Examples:
        >>> solve([1, 1, 4, 2, 3], 5)
        2
        >>> solve([5, 6, 7, 8, 9], 4)
        -1
        >>> solve([3, 2, 20, 1, 1, 3], 10)
        5
    """
    total_sum = sum(nums)
    target_subarray_sum = total_sum - x

    # If target is 0, we must remove all elements
    if target_subarray_sum == 0:
        return len(nums)
    
    # If target is negative, it's impossible to reach x since all nums > 0
    if target_subarray_sum < 0:
        return -1

    max_subarray_length = -1
    current_window_sum = 0
    left_pointer = 0

    # Use a sliding window to find the longest subarray with sum == target_subarray_sum
    for right_pointer in range(len(nums)):
        current_window_sum += nums[right_pointer]

        # Shrink the window from the left if the sum exceeds the target
        while current_window_sum > target_subarray_sum and left_pointer <= right_pointer:
            current_window_sum -= nums[left_pointer]
            left_pointer += 1

        # Check if we found a valid window
        if current_window_sum == target_subarray_sum:
            max_subarray_length = max(max_subarray_length, right_pointer - left_pointer + 1)

    # If no valid subarray was found, return -1
    if max_subarray_length == -1:
        return -1

    # The answer is the total length minus the length of the longest internal subarray
    return len(nums) - max_subarray_length
