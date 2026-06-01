METADATA = {
    "id": 1099,
    "name": "Two Sum Less Than K",
    "slug": "two-sum-less-than-k",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum sum of two elements in an array such that the sum is strictly less than a given integer k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the maximum sum of two elements in the array that is strictly less than k.

    Args:
        nums: A list of integers.
        k: The target integer threshold.

    Returns:
        The maximum sum found that is less than k. Returns -1 if no such sum exists.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 7)
        6
        >>> solve([1, 2, 3, 4, 5], 3)
        -1
        >>> solve([10, 20, 30, 40], 50)
        30
    """
    # Sort the array to enable the two-pointer approach
    nums.sort()
    
    left_index = 0
    right_index = len(nums) - 1
    max_sum = -1

    # Use two pointers moving towards each other
    while left_index < right_index:
        current_sum = nums[left_index] + nums[right_index]
        
        if current_sum < k:
            # If sum is valid, update max_sum and try to find a larger sum
            # by moving the left pointer to the right
            max_sum = max(max_sum, current_sum)
            left_index += 1
        else:
            # If sum is too large (>= k), we must decrease the sum
            # by moving the right pointer to the left
            right_index -= 1
            
    return max_sum
