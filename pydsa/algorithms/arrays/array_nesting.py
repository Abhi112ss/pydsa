METADATA = {
    "id": 565,
    "name": "Array Nesting",
    "slug": "array-nesting",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "dfs", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the largest set of indices that form a cycle in the given array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum length of a cycle in the array.

    The array represents a directed graph where each index points to the value 
    at that index. Since each number from 0 to n-1 appears exactly once, 
    the graph consists of several disjoint cycles.

    Args:
        nums: A list of integers where nums[i] is the next index in the cycle.

    Returns:
        The length of the longest cycle found in the array.

    Examples:
        >>> solve([5, 4, 0, 3, 1, 2])
        4
        >>> solve([0])
        1
        >>> solve([1, 0])
        2
    """
    max_cycle_length = 0
    n = len(nums)
    
    # We use the input array itself to mark visited elements to achieve O(1) space.
    # We can mark an element as visited by setting it to a value outside the range [0, n-1].
    # However, since we need to traverse, a common trick is to use a sentinel value 
    # or simply check if the value has been 'consumed'. 
    # To keep it clean and avoid modifying the array if it were read-only, 
    # we'd use a set, but the problem allows O(1) space by modifying the input.
    
    for start_index in range(n):
        # If nums[start_index] is -1, it means this index was already part of a cycle.
        if nums[start_index] == -1:
            continue
            
        current_cycle_length = 0
        current_index = start_index
        
        # Traverse the cycle starting from the current index
        while nums[current_index] != -1:
            next_index = nums[current_index]
            
            # Mark the current index as visited by setting it to -1
            nums[current_index] = -1
            
            # Move to the next index in the cycle
            current_index = next_index
            current_cycle_length += 1
            
        # Update the global maximum cycle length found so far
        if current_cycle_length > max_cycle_length:
            max_cycle_length = current_cycle_length
            
    return max_cycle_length
