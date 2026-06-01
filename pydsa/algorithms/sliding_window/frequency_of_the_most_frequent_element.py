METADATA = {
    "id": 1838,
    "name": "Frequency of the Most Frequent Element",
    "slug": "frequency-of-the-most-frequent-element",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sorting", "sliding_window", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum frequency of an element after performing at most k operations where an element can be incremented by 1.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the maximum frequency of an element after at most k increments.

    Args:
        nums: A list of integers representing the initial frequencies.
        k: The maximum number of operations allowed.

    Returns:
        The maximum possible frequency of any element after at most k operations.

    Examples:
        >>> solve([1, 2, 4], 5)
        3
        >>> solve([1, 4, 8, 13], 5)
        2
    """
    # Sort the array to ensure that for any window [left, right], 
    # the target value to make all elements equal is nums[right].
    nums.sort()
    
    max_frequency = 0
    window_sum = 0
    left = 0
    
    # Iterate through the array with the 'right' pointer as the target element
    for right in range(len(nums)):
        window_sum += nums[right]
        
        # The condition for a valid window is:
        # (target_value * window_size) - actual_sum <= k
        # where target_value is nums[right] and window_size is (right - left + 1)
        while (nums[right] * (right - left + 1)) - window_sum > k:
            # If the condition is violated, shrink the window from the left
            window_sum -= nums[left]
            left += 1
            
        # Update the maximum frequency found so far
        max_frequency = max(max_frequency, right - left + 1)
        
    return max_frequency
