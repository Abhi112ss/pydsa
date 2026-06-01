METADATA = {
    "id": 3818,
    "name": "Minimum Prefix Removal to Make Array Strictly Increasing",
    "slug": "minimum-prefix-removal-to-make-array-strictly-increasing",
    "category": "Array",
    "aliases": [],
    "tags": ["binary_search", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of elements to remove from the front of an array such that the remaining suffix is strictly increasing.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the minimum number of elements to remove from the prefix of the array
    such that the remaining suffix is strictly increasing.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of elements to remove from the front.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        0
        >>> solve([5, 4, 3, 2, 1])
        4
        >>> solve([1, 3, 2, 4, 5])
        2
    """
    n = len(nums)
    if n <= 1:
        return 0

    # A suffix starting at index 'i' is strictly increasing if 
    # for all k in [i, n-2], nums[k] < nums[k+1].
    # We want to find the smallest 'i' such that the suffix nums[i:] is strictly increasing.
    # However, the problem asks for the minimum prefix removal, which means we want
    # the largest possible suffix.
    
    # First, identify the longest strictly increasing suffix.
    # We can do this by scanning from the end of the array backwards.
    
    # Find the first index 'break_point' from the right where the increasing property fails.
    # The suffix starting from 'break_point + 1' is the longest strictly increasing suffix.
    
    break_point = n - 2
    while break_point >= 0 and nums[break_point] < nums[break_point + 1]:
        break_point -= 1
    
    # The longest strictly increasing suffix starts at index 'break_point + 1'.
    # Any prefix removal that leaves a suffix starting at index <= break_point 
    # will result in a non-strictly increasing array.
    # Therefore, the minimum removal is the number of elements before the 
    # start of the longest strictly increasing suffix.
    
    # Wait, the logic above finds the longest suffix that is strictly increasing.
    # If the suffix starting at index 'i' is strictly increasing, then any suffix 
    # starting at index 'j > i' is also strictly increasing.
    # To minimize prefix removal, we want the smallest 'i' such that nums[i:] is strictly increasing.
    
    # Let's re-evaluate:
    # The condition is: nums[i] < nums[i+1] < ... < nums[n-1].
    # This is equivalent to saying there is no index k in [i, n-2] such that nums[k] >= nums[k+1].
    
    # We find the largest index 'k' such that nums[k] >= nums[k+1].
    # If no such 'k' exists, the whole array is strictly increasing (removal = 0).
    # If such 'k' exists, the suffix must start at least at index 'k+1'.
    
    last_violation_index = -1
    for i in range(n - 2, -1, -1):
        if nums[i] >= nums[i + 1]:
            last_violation_index = i
            break
            
    if last_violation_index == -1:
        return 0
    
    # The smallest valid suffix starts at last_violation_index + 1.
    # The number of elements to remove is the count of elements before this index.
    return last_violation_index + 1
