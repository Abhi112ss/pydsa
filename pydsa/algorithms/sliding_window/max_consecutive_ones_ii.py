METADATA = {
    "id": 487,
    "name": "Max Consecutive Ones II",
    "slug": "max-consecutive-ones-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of consecutive 1s in a binary array if you can flip at most one 0 to 1.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum number of consecutive 1s in a binary array after flipping at most one 0.

    Args:
        nums: A list of integers containing only 0s and 1s.

    Returns:
        The maximum length of consecutive 1s possible after flipping one 0.

    Examples:
        >>> solve([1, 0, 1, 1, 0])
        4
        >>> solve([1, 1, 1, 1, 1])
        5
        >>> solve([0, 0, 0, 0, 0])
        1
    """
    max_length = 0
    left_pointer = 0
    zero_count = 0

    # Iterate through the array using a sliding window approach
    for right_pointer in range(len(nums)):
        # If we encounter a zero, increment our zero counter
        if nums[right_pointer] == 0:
            zero_count += 1

        # If the window contains more than one zero, shrink it from the left
        # until we have at most one zero in the current window
        while zero_count > 1:
            if nums[left_pointer] == 0:
                zero_count -= 1
            left_pointer += 1

        # Calculate the current window size and update the global maximum
        current_window_size = right_pointer - left_pointer + 1
        if current_window_size > max_length:
            max_length = current_window_size

    return max_length
