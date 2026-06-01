METADATA = {
    "id": 910,
    "name": "Smallest Range II",
    "slug": "smallest-range-ii",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the smallest possible difference between the maximum and minimum elements of an array after adding or subtracting k from each element.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the smallest possible difference between the maximum and minimum 
    elements of an array after adding or subtracting k from each element.

    Args:
        nums: A list of integers.
        k: An integer representing the value to be added or subtracted.

    Returns:
        The minimum possible difference between the maximum and minimum elements.

    Examples:
        >>> solve([1, 3, 6], 3)
        0
        >>> solve([-1, 0, 1, 2], 5)
        1
    """
    # Sort the array to handle elements in increasing order.
    # This allows us to pick a split point where elements to the left 
    # are increased and elements to the right are decreased.
    nums.sort()
    n = len(nums)
    
    # Initial range is the difference between the current max and min.
    # This covers the case where we add k to all or subtract k from all.
    min_diff = nums[-1] - nums[0]
    
    # Iterate through the array, treating each index i as the last element 
    # that will be increased by k.
    for i in range(n - 1):
        # If we split at index i:
        # Elements [0...i] are increased by k.
        # Elements [i+1...n-1] are decreased by k.
        
        # The potential new maximum will be the larger of:
        # 1. The last element decreased by k.
        # 2. The current element increased by k.
        current_max = max(nums[-1] - k, nums[i] + k)
        
        # The potential new minimum will be the smaller of:
        # 1. The first element increased by k.
        # 2. The next element decreased by k.
        current_min = min(nums[0] + k, nums[i + 1] - k)
        
        # Update the global minimum difference.
        min_diff = min(min_diff, current_max - current_min)
        
    return min_diff
