METADATA = {
    "id": 1493,
    "name": "Longest Subarray of 1's After Deleting One Element",
    "slug": "longest-subarray-of-1s-after-deleting-one-element",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the longest subarray containing only 1's after deleting exactly one element from the given binary array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest subarray containing only 1's after deleting one element.

    The algorithm uses a sliding window approach where the window is allowed to 
    contain at most one zero. The length of the window minus one (representing 
    the deleted element) gives the count of 1's.

    Args:
        nums: A list of integers representing a binary array.

    Returns:
        The length of the longest subarray of 1's after deleting one element.

    Examples:
        >>> solve([1, 1, 0, 1])
        3
        >>> solve([0, 1, 1, 1, 0, 1, 1, 0])
        5
        >>> solve([1, 1, 1])
        2
    """
    left_pointer = 0
    zero_count = 0
    max_length = 0

    # Iterate through the array with the right pointer
    for right_pointer in range(len(nums)):
        # If we encounter a zero, increment our zero counter
        if nums[right_pointer] == 0:
            zero_count += 1

        # If we have more than one zero, shrink the window from the left
        # until we have at most one zero again
        while zero_count > 1:
            if nums[left_pointer] == 0:
                zero_count -= 1
            left_pointer += 1

        # The window size is (right - left + 1). 
        # Since we MUST delete one element, the number of 1's is (window_size - 1).
        # This handles the case where the array is all 1's correctly.
        max_length = max(max_length, right_pointer - left_pointer)

    return max_length
