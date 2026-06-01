METADATA = {
    "id": 2919,
    "name": "Minimum Increment Operations to Make Array Beautiful",
    "slug": "minimum-increment-operations-to-make-array-beautiful",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of increment operations to make an array beautiful where each element is greater than the sum of all previous elements.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of increment operations to make the array beautiful.
    An array is beautiful if each element nums[i] is strictly greater than the 
    sum of all elements before it.

    Args:
        nums: A list of integers.

    Returns:
        The total number of increment operations performed.

    Examples:
        >>> solve([1, 2, 4, 8])
        0
        >>> solve([1, 1, 1, 1])
        11
        >>> solve([10, 1, 1, 1])
        11
    """
    # Sort the array to satisfy the condition greedily from smallest to largest
    nums.sort()
    
    total_increments = 0
    current_running_sum = 0
    
    for value in nums:
        # The condition for beauty is: value > current_running_sum
        # Therefore, the minimum required value is current_running_sum + 1
        target_value = current_running_sum + 1
        
        if value < target_value:
            # Calculate how many increments are needed to reach the target
            needed = target_value - value
            total_increments += needed
            # The element effectively becomes target_value
            actual_value = target_value
        else:
            # The element already satisfies the condition
            actual_value = value
            
        # Update the running sum with the value (original or incremented)
        current_running_sum += actual_value
        
    return total_increments
