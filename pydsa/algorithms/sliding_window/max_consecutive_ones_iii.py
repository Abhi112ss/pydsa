METADATA = {
    "id": 1004,
    "name": "Max Consecutive Ones III",
    "slug": "max_consecutive_ones_iii",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of consecutive 1s in a binary array if you can flip at most k zeros.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the maximum number of consecutive 1s in a binary array after flipping at most k zeros.

    Args:
        nums: A list of integers containing only 0s and 1s.
        k: The maximum number of 0s that can be flipped to 1s.

    Returns:
        The length of the longest subarray containing only 1s after at most k flips.

    Examples:
        >>> solve([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
        6
        >>> solve([0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1], 2)
        5
    """
    left_pointer = 0
    max_length = 0
    zero_count = 0

    # Iterate through the array with the right pointer to expand the window
    for right_pointer in range(len(nums)):
        # If we encounter a zero, increment our zero counter
        if nums[right_pointer] == 0:
            zero_count += 1

        # If the number of zeros in the current window exceeds k, 
        # shrink the window from the left until zero_count is within limits
        while zero_count > k:
            if nums[left_pointer] == 0:
                zero_count -= 1
            left_pointer += 1

        # Calculate the current window size and update the maximum length found
        current_window_size = right_pointer - left_pointer + 1
        if current_window_size > max_length:
            max_length = current_window_size

    return max_length
