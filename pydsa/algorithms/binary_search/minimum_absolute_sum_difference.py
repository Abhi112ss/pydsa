METADATA = {
    "id": 1818,
    "name": "Minimum Absolute Sum Difference",
    "slug": "minimum-absolute-sum-difference",
    "category": "Array",
    "aliases": [],
    "tags": ["binary_search", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Replace at most one element in an array to minimize the absolute difference between the sum of the array and a target value.",
}

import bisect

def solve(nums: list[int], target: int) -> int:
    """
    Calculates the minimum absolute difference between the sum of the array 
    and the target after replacing at most one element.

    Args:
        nums: A list of integers.
        target: The target integer value.

    Returns:
        The minimum absolute difference possible.

    Examples:
        >>> solve([4, 5, 2, 1], 4)
        0
        >>> solve([4, 5, 2, 1], 10)
        2
    """
    current_sum = sum(nums)
    # The difference we want to minimize is |(current_sum - nums[i] + replacement) - target|
    # This is equivalent to minimizing |(current_sum - target - nums[i]) + replacement|
    # Let diff_needed = target - (current_sum - nums[i])
    # We want to find a replacement in the original array closest to diff_needed.
    
    # Sort a copy of the array to perform binary search for the best replacement
    sorted_nums = sorted(nums)
    min_abs_diff = abs(current_sum - target)

    for i in range(len(nums)):
        # Calculate what the sum would be if we removed nums[i]
        sum_without_current = current_sum - nums[i]
        
        # We want: sum_without_current + replacement ≈ target
        # So: replacement ≈ target - sum_without_current
        ideal_replacement = target - sum_without_current
        
        # Use binary search to find the closest value to ideal_replacement in sorted_nums
        idx = bisect.bisect_left(sorted_nums, ideal_replacement)
        
        # Check the element at idx (the smallest element >= ideal_replacement)
        if idx < len(sorted_nums):
            replacement = sorted_nums[idx]
            current_diff = abs(sum_without_current + replacement - target)
            if current_diff < min_abs_diff:
                min_abs_diff = current_diff
                
        # Check the element at idx - 1 (the largest element < ideal_replacement)
        if idx > 0:
            replacement = sorted_nums[idx - 1]
            current_diff = abs(sum_without_current + replacement - target)
            if current_diff < min_abs_diff:
                min_abs_diff = current_diff
        
        # Early exit if we found the perfect match
        if min_abs_diff == 0:
            return 0

    return min_abs_diff
