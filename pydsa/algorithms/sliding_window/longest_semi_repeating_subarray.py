METADATA = {
    "id": 3641,
    "name": "Longest Semi-Repeating Subarray",
    "slug": "longest_semi_repeating_subarray",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest subarray where at most one element repeats exactly twice.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest subarray that contains at most one element 
    appearing exactly twice, and all other elements appearing at most once.
    
    Note: The problem definition for 'semi-repeating' in this context implies 
    that we can have at most one element with a frequency of 2, and all 
    other elements must have a frequency of 1.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest valid semi-repeating subarray.

    Examples:
        >>> solve([1, 2, 1, 2, 3])
        4
        >>> solve([1, 1, 1, 2, 2])
        3
    """
    if not nums:
        return 0

    max_length = 0
    left = 0
    counts = {}
    # tracks how many elements currently violate the 'at most one element repeats twice' rule
    # specifically, we track elements with frequency > 1
    # and we track how many elements have frequency > 2
    elements_with_freq_gt_1 = 0
    elements_with_freq_gt_2 = 0

    for right in range(len(nums)):
        val = nums[right]
        counts[val] = counts.get(val, 0) + 1
        
        # Update violation counters based on the new frequency of the current element
        if counts[val] == 2:
            elements_with_freq_gt_1 += 1
        elif counts[val] == 3:
            elements_with_freq_gt_2 += 1
            
        # Shrink the window if:
        # 1. Any element appears more than twice (elements_with_freq_gt_2 > 0)
        # 2. More than one element appears twice (elements_with_freq_gt_1 > 1)
        while elements_with_freq_gt_2 > 0 or elements_with_freq_gt_1 > 1:
            left_val = nums[left]
            if counts[left_val] == 3:
                elements_with_freq_gt_2 -= 1
            elif counts[left_val] == 2:
                elements_with_freq_gt_1 -= 1
            
            counts[left_val] -= 1
            left += 1
            
        # The window [left, right] is now valid
        max_length = max(max_length, right - left + 1)

    return max_length
