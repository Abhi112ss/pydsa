METADATA = {
    "id": 3903,
    "name": "Smallest Stable Index I",
    "slug": "smallest_stable_index_i",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "prefix_sum"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the smallest index such that the sum of elements before it equals the sum of elements after it.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the smallest index 'i' such that the sum of elements in nums[0...i-1] 
    is equal to the sum of elements in nums[i+1...n-1].

    Args:
        nums: A list of integers.

    Returns:
        The smallest index satisfying the stability condition, or -1 if no such index exists.

    Examples:
        >>> solve([1, 7, 3, 6, 5, 6])
        3
        >>> solve([1, 2, 3])
        -1
        >>> solve([2, 1, 1])
        0
    """
    total_sum = sum(nums)
    left_sum = 0
    
    for index, current_value in enumerate(nums):
        # The right sum is the total sum minus the left sum and the current element
        right_sum = total_sum - left_sum - current_value
        
        # Check if the stability condition is met
        if left_sum == right_sum:
            return index
        
        # Update the running left sum for the next iteration
        left_sum += current_value
        
    return -1
