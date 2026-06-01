METADATA = {
    "id": 3046,
    "name": "Split the Array",
    "slug": "split_the_array",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if an array can be split into two non-empty parts with equal sums.",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if the array can be split into two non-empty parts with equal sums.

    Args:
        nums: A list of integers representing the array.

    Returns:
        True if the array can be split into two parts with equal sums, False otherwise.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 5])
        True
        >>> solve([1, 2, 3, 4, 5])
        False
    """
    total_sum = sum(nums)
    
    # If the total sum is odd, it cannot be split into two equal integer sums
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    running_prefix_sum = 0
    
    # Iterate through the array up to the second to last element
    # to ensure the second part is non-empty.
    for i in range(len(nums) - 1):
        running_prefix_sum += nums[i]
        
        # If the current prefix sum matches exactly half of the total sum,
        # the remaining elements must also sum to the other half.
        if running_prefix_sum == target_sum:
            return True
            
    return False
