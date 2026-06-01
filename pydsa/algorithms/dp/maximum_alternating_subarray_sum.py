METADATA = {
    "id": 2036,
    "name": "Maximum Alternating Subarray Sum",
    "slug": "maximum_alternating_subarray_sum",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "kadane_algorithm", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum sum of an alternating subarray where elements are added and subtracted alternately.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum alternating subarray sum using a variation of Kadane's algorithm.
    
    An alternating subarray sum is defined as: nums[i] - nums[i+1] + nums[i+2] - ...
    
    Args:
        nums: A list of integers.
        
    Returns:
        The maximum alternating subarray sum found.
        
    Examples:
        >>> solve([2, -1, 2])
        5
        >>> solve([4, -2, 5, 1])
        11
        >>> solve([-5, -2, -1])
        -1
    """
    if not nums:
        return 0

    # max_pos[i] is the max alternating sum ending at index i where nums[i] is added (+)
    # max_neg[i] is the max alternating sum ending at index i where nums[i] is subtracted (-)
    # We only need the previous state, so we use variables instead of arrays to achieve O(1) space.
    
    # Initialize with the first element. 
    # A subarray of length 1 starting at index 0 must have the first element as positive.
    max_pos = nums[0]
    max_neg = float('-inf')
    
    global_max = nums[0]

    for i in range(1, len(nums)):
        current_val = nums[i]
        
        # To have nums[i] as a positive term in an alternating sum:
        # 1. It starts a new subarray: current_val
        # 2. It follows a subarray where the previous element was subtracted: max_neg + current_val
        new_max_pos = max(current_val, max_neg + current_val)
        
        # To have nums[i] as a negative term in an alternating sum:
        # 1. It follows a subarray where the previous element was added: max_pos - current_val
        # Note: A subarray cannot start with a negative term based on the problem definition 
        # (alternating sum starts with +).
        new_max_neg = max_pos - current_val
        
        max_pos = new_max_pos
        max_neg = new_max_neg
        
        # Update the global maximum found so far
        global_max = max(global_max, max_pos, max_neg)

    return int(global_max)
