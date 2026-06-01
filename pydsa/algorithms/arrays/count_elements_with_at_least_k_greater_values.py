METADATA = {
    "id": 3759,
    "name": "Count Elements With at Least K Greater Values",
    "slug": "count_elements_with_at_least_k_greater_values",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count how many elements in an array have at least k elements strictly greater than them.",
}

import bisect

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of elements in the array that have at least k elements 
    strictly greater than them.

    Args:
        nums: A list of integers.
        k: The minimum number of elements that must be strictly greater than the current element.

    Returns:
        The count of elements satisfying the condition.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        3
        >>> solve([1, 1, 1, 1], 1)
        0
        >>> solve([5, 4, 3, 2, 1], 2)
        3
    """
    if not nums or k <= 0:
        # If k is 0 or less, every element technically has at least 0 greater values.
        # However, based on standard problem constraints, k is usually >= 1.
        # If k=0, the answer is len(nums).
        return len(nums) if k <= 0 else 0

    n = len(nums)
    # Sort the array to allow for efficient binary search of greater elements
    sorted_nums = sorted(nums)
    count = 0

    for val in nums:
        # Find the index of the first element strictly greater than 'val'
        # bisect_right returns the insertion point which is the index of 
        # the first element > val in a sorted list.
        first_greater_idx = bisect.bisect_right(sorted_nums, val)
        
        # The number of elements strictly greater than 'val' is the total 
        # number of elements minus the index of the first element > val.
        num_greater = n - first_greater_idx
        
        if num_greater >= k:
            count += 1
            
    return count
