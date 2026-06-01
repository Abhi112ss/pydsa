METADATA = {
    "id": 2824,
    "name": "Count Pairs Whose Sum is Less than Target",
    "slug": "count-pairs-whose-sum-is-less-than-target",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Count the number of pairs (i, j) such that 0 <= i < j < nums.length and nums[i] + nums[j] < target.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Counts the number of pairs in the array whose sum is strictly less than the target.

    Args:
        nums: A list of integers.
        target: The integer threshold for the sum of pairs.

    Returns:
        The total count of pairs (i, j) where i < j and nums[i] + nums[j] < target.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 5)
        3
        >>> solve([1, 1, 1, 1], 2)
        0
        >>> solve([5, 1, 2, 3, 4], 10)
        10
    """
    # Sorting allows us to use the two-pointer technique effectively.
    # If nums[left] + nums[right] < target, then all elements between 
    # left and right will also satisfy the condition when paired with nums[left].
    nums.sort()
    
    count = 0
    left = 0
    right = len(nums) - 1
    
    while left < right:
        if nums[left] + nums[right] < target:
            # If the sum is less than target, then nums[left] paired with 
            # any element from index (left + 1) to right is valid.
            count += (right - left)
            # Move the left pointer to try a larger value for the first element.
            left += 1
        else:
            # If the sum is too large, we must decrease the sum by 
            # moving the right pointer to a smaller value.
            right -= 1
            
    return count
