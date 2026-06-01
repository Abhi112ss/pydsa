METADATA = {
    "id": 1746,
    "name": "Maximum Subarray Sum After One Operation",
    "slug": "maximum-subarray-sum-after-one-operation",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "kadane_algorithm", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum subarray sum after choosing exactly one element and increasing it by 1.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum subarray sum possible after increasing exactly one 
    element in the array by 1.

    This implementation uses a modified Kadane's algorithm. We maintain two 
    states for each position:
    1. current_max_no_op: The maximum subarray sum ending at the current index 
       without having used the '+1' operation.
    2. current_max_with_op: The maximum subarray sum ending at the current index 
       where the '+1' operation has been applied to exactly one element in the 
       subarray.

    Args:
        nums: A list of integers.

    Returns:
        The maximum subarray sum possible after one operation.

    Examples:
        >>> solve([1, -1, 1, 3, 2])
        7
        >>> solve([2, -1, -2, 1, 3])
        4
        >>> solve([-1, -2, -3])
        -1
    """
    # Initialize global maximum with a very small value
    global_max = float('-inf')
    
    # current_max_no_op tracks the standard Kadane's state (max sum ending here)
    current_max_no_op = 0
    
    # current_max_with_op tracks the max sum ending here where one element was +1
    current_max_with_op = 0

    for num in nums:
        # Option 1: Apply the +1 to the current element itself.
        # This is either (current_max_no_op + num + 1) or just (num + 1).
        # Option 2: The +1 was already applied to a previous element in the subarray.
        # This is (current_max_with_op + num).
        current_max_with_op = max(current_max_no_op + num + 1, current_max_with_op + num)
        
        # Standard Kadane's: either extend the existing subarray or start fresh from current num
        current_max_no_op = max(num, current_max_no_op + num)
        
        # Update the global maximum found so far
        global_max = max(global_max, current_max_with_op)

    return int(global_max)
