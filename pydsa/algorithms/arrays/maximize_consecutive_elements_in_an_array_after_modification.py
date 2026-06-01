METADATA = {
    "id": 3041,
    "name": "Maximize Consecutive Elements in an Array After Modification",
    "slug": "maximize-consecutive-elements-in-an-array-after-modification",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "sliding window", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of consecutive elements that can be formed by modifying at most k elements.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the maximum number of consecutive elements that can be formed.
    
    The strategy is to sort the array and use a sliding window. For a window 
    [left, right], the number of elements we need to 'fill in' to make the 
    range consecutive is (nums[right] - nums[left]) - (right - left).
    If this value is <= k, the window is valid.

    Args:
        nums: A list of integers.
        k: The maximum number of modifications allowed.

    Returns:
        The maximum length of a consecutive sequence possible.

    Examples:
        >>> solve([1, 1, 1, 1], 0)
        1
        >>> solve([1, 3, 5], 1)
        2
        >>> solve([1, 10, 100], 1)
        1
    """
    if not nums:
        return 0

    # Sort to allow sliding window approach on value ranges
    nums.sort()
    
    max_consecutive = 0
    left = 0
    
    # Iterate through the array with the right pointer
    for right in range(len(nums)):
        # The number of gaps between nums[left] and nums[right] is:
        # (Total distance) - (Number of existing elements in the window - 1)
        # Formula: (nums[right] - nums[left]) - (right - left)
        
        # While the required modifications exceed k, shrink the window from the left
        while (nums[right] - nums[left]) - (right - left) > k:
            left += 1
            
        # Update the maximum window size found so far
        current_window_size = right - left + 1
        if current_window_size > max_consecutive:
            max_consecutive = current_window_size
            
    return max_consecutive
