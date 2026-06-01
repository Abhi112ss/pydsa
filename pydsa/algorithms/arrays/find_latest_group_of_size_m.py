METADATA = {
    "id": 1562,
    "name": "Find Latest Group of Size M",
    "slug": "find-latest-group-of-size-m",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the starting index of the last contiguous group of 1s with a length of at least m.",
}

def solve(nums: list[int], m: int) -> int:
    """
    Finds the starting index of the latest contiguous group of 1s with length at least m.

    Args:
        nums: A list of integers where each element is either 0 or 1.
        m: The minimum required length of the contiguous group of 1s.

    Returns:
        The starting index of the last group of 1s of length at least m. 
        Returns -1 if no such group exists.

    Examples:
        >>> solve([1, 1, 1, 0, 1, 1], 2)
        4
        >>> solve([0, 0, 0, 1, 0, 0], 1)
        3
        >>> solve([1, 0, 1, 0, 1], 2)
        -1
    """
    latest_start_index = -1
    current_streak_length = 0
    
    for current_index in range(len(nums)):
        if nums[current_index] == 1:
            # Increment the current streak of 1s
            current_streak_length += 1
            
            # If the current streak meets or exceeds m, 
            # the potential start index for this group is (current_index - m + 1)
            # However, we want the start of the *entire* contiguous block that is >= m.
            # Actually, the problem asks for the latest group of size M.
            # If we have [1, 1, 1] and m=2, the latest group of size 2 starts at index 1.
            if current_streak_length >= m:
                latest_start_index = current_index - m + 1
        else:
            # Reset the streak when a 0 is encountered
            current_streak_length = 0
            
    return latest_start_index
