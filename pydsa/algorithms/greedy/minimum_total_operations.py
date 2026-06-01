METADATA = {
    "id": 3353,
    "name": "Minimum Total Operations",
    "slug": "minimum-total-operations",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make an array non-decreasing by incrementing elements.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to make the array non-decreasing.
    An operation consists of incrementing an element by 1.

    Args:
        nums: A list of integers representing the initial state of the array.

    Returns:
        The minimum total number of operations required.

    Examples:
        >>> solve([1, 2, 3])
        0
        >>> solve([3, 2, 1])
        3
        >>> solve([1, 5, 2, 4, 1])
        11
    """
    total_operations = 0
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is smaller than the previous one,
        # it violates the non-decreasing condition.
        if nums[i] < nums[i - 1]:
            # Calculate the difference needed to make nums[i] equal to nums[i-1]
            diff = nums[i - 1] - nums[i]
            total_operations += diff
            
            # Update the current element to reflect the increment operation
            # This ensures the next comparison is against the new value
            nums[i] = nums[i - 1]
            
    return total_operations
