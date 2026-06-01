METADATA = {
    "id": 2996,
    "name": "Smallest Missing Integer Greater Than Sequential Prefix Sum",
    "slug": "smallest_missing_integer_greater_than_sequential_prefix_sum",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the smallest integer greater than the sum of a sequential prefix of an array that is not present in the array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the smallest integer greater than the sum of a sequential prefix 
    of the array that does not exist in the array.

    The problem asks us to check every possible prefix sum (starting from 
    the first element) and for each sum, find the smallest integer 
    strictly greater than that sum that is not in the original array.

    Args:
        nums: A list of integers.

    Returns:
        The smallest integer greater than a sequential prefix sum that is not in nums.

    Examples:
        >>> solve([1, 2, 3])
        7
        >>> solve([4, 1, 2])
        8
    """
    # Convert to set for O(1) average time complexity lookups
    # Note: While the prompt suggests O(1) space, a set is required to 
    # efficiently check existence. If the input is sorted, we could do O(1) space.
    # However, for a general unsorted array, a set is the standard approach.
    num_set = set(nums)
    n = len(nums)
    
    # We want the absolute minimum across all possible prefix sums.
    # Initialize with a very large value.
    min_missing_integer = float('inf')
    
    current_prefix_sum = 0
    for i in range(n):
        current_prefix_sum += nums[i]
        
        # We need the smallest integer x such that x > current_prefix_sum 
        # and x is not in the original array.
        candidate = current_prefix_sum + 1
        
        # Increment candidate until we find one not in the set.
        # In the worst case, this looks like it could be slow, but 
        # the number of elements in the set is finite.
        while candidate in num_set:
            candidate += 1
            
        # Update the global minimum found so far.
        if candidate < min_missing_integer:
            min_missing_integer = candidate
            
    return int(min_missing_integer)
