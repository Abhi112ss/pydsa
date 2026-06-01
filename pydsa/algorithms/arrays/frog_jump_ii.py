METADATA = {
    "id": 2498,
    "name": "Frog Jump II",
    "slug": "frog-jump-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum distance a frog can jump given a set of stones and a maximum jump distance k.",
}

def solve(stones: list[int], k: int) -> int:
    """
    Calculates the maximum distance the frog can jump using a greedy approach.
    
    The strategy is to always jump to the furthest possible stone within range k
    to maximize the reach of the next jump.

    Args:
        stones: A sorted list of integers representing stone positions.
        k: The maximum distance the frog can jump.

    Returns:
        The maximum distance (last stone position - first stone position) 
        the frog can travel.

    Examples:
        >>> solve([0, 1, 3, 5, 8, 12, 15], 3)
        15
        >>> solve([0, 2, 4, 7, 10], 1)
        0
    """
    n = len(stones)
    if n == 0:
        return 0
    
    # current_index tracks the stone the frog is currently on
    current_index = 0
    
    # We iterate through the stones. In each step, we try to find the 
    # furthest stone that is within distance k from the current stone.
    while current_index < n - 1:
        next_index = current_index
        
        # Look ahead to find the furthest stone within range k
        # We start checking from the furthest possible stone index
        # that could be within range.
        search_idx = current_index + 1
        
        # Greedy step: find the furthest stone reachable from current_index
        # that is <= stones[current_index] + k
        # Since stones are sorted, we can just scan forward.
        # To optimize, we look for the largest index i such that 
        # stones[i] - stones[current_index] <= k
        
        # We use a simple pointer to find the furthest reachable stone
        # because the total number of increments across all iterations is O(n)
        temp_idx = current_index + 1
        while temp_idx < n and stones[temp_idx] - stones[current_index] <= k:
            next_index = temp_idx
            temp_idx += 1
            
        # If we couldn't move forward at all, the frog is stuck
        if next_index == current_index:
            return 0
            
        current_index = next_index
        
    # The total distance is the position of the last stone reached minus the start
    return stones[current_index] - stones[0]
