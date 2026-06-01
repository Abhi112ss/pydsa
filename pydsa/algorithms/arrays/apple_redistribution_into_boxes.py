METADATA = {
    "id": 3074,
    "name": "Apple Redistribution into Boxes",
    "slug": "apple-redistribution-into-boxes",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum number of moves to redistribute apples such that each box has an equal number of apples.",
}

def solve(apples: list[int], target: int) -> int:
    """
    Calculates the minimum number of moves to redistribute apples so each box has 'target' apples.
    
    A move consists of taking one apple from a box and moving it to an adjacent box.
    The total moves is the sum of the absolute cumulative differences between the 
    current apple count and the target count at each boundary.

    Args:
        apples: A list of integers representing the number of apples in each box.
        target: The desired number of apples in each box.

    Returns:
        The minimum number of moves required.

    Examples:
        >>> solve([1, 2, 3], 2)
        2
        >>> solve([0, 0, 0], 0)
        0
        >>> solve([1, 1, 1], 1)
        0
    """
    total_moves = 0
    current_balance = 0
    
    # We iterate through the boxes (except the last one, as the last box 
    # doesn't need to push/pull to a next neighbor to satisfy the target).
    # The 'current_balance' tracks the net surplus or deficit of apples 
    # that must be moved across the boundary between box i and box i+1.
    for i in range(len(apples) - 1):
        # Calculate how many apples must cross the boundary between box i and i+1
        # to eventually reach the target state.
        current_balance += apples[i] - target
        
        # The absolute value of the balance represents the number of apples 
        # that must pass through this specific boundary.
        total_moves += abs(current_balance)
        
    return total_moves
