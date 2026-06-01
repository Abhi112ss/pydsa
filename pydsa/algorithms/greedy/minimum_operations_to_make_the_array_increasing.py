METADATA = {
    "id": 1827,
    "name": "Minimum Operations to Make the Array Increasing",
    "slug": "minimum-operations-to-make-the-array-increasing",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make an array strictly increasing, where an operation consists of increasing an element.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to make the array strictly increasing.
    
    An operation consists of increasing an element by 1. To make the array 
    strictly increasing, each element nums[i] must be at least nums[i-1] + 1.

    Args:
        nums: A list of integers.

    Returns:
        The total number of operations performed.

    Examples:
        >>> solve([1, 1, 1])
        2
        >>> solve([1, 5, 2, 4, 1])
        14
        >>> solve([1, 2, 3, 4])
        0
    """
    total_operations = 0
    
    # Start from the second element and compare it with the previous one
    for i in range(1, len(nums)):
        # If the current element is not greater than the previous element
        if nums[i] <= nums[i - 1]:
            # Calculate the target value needed to make it strictly increasing
            target_value = nums[i - 1] + 1
            
            # The number of operations is the difference between target and current
            diff = target_value - nums[i]
            total_operations += diff
            
            # Update the current element in the array to reflect the operation
            nums[i] = target_value
            
    return total_operations
