METADATA = {
    "id": 3344,
    "name": "Maximum Sized Array",
    "slug": "maximum_sized_array",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum length of a subarray where the sum of elements is less than or equal to a given target.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Finds the maximum length of a contiguous subarray such that the sum 
    of its elements is less than or equal to the target.

    Args:
        nums: A list of integers representing the array.
        target: The maximum allowed sum for the subarray.

    Returns:
        The length of the longest subarray satisfying the condition.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 11)
        4
        >>> solve([4, 3, 2, 1], 7)
        3
    """
    max_length = 0
    current_sum = 0
    left_pointer = 0

    # Iterate through the array using a right pointer to expand the window
    for right_pointer in range(len(nums)):
        current_sum += nums[right_pointer]

        # If the current sum exceeds the target, shrink the window from the left
        while current_sum > target and left_pointer <= right_pointer:
            current_sum -= nums[left_pointer]
            left_pointer += 1

        # Update the maximum length found so far
        # The current window size is (right_pointer - left_pointer + 1)
        current_window_size = right_pointer - left_pointer + 1
        if current_window_size > max_length:
            max_length = current_window_size

    return max_length
