METADATA = {
    "id": 1552,
    "name": "Magnetic Force Between Two Balls",
    "slug": "magnetic-force-between-two-balls",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n + n log(max_dist))",
    "space_complexity": "O(1)",
    "description": "Find the maximum possible minimum magnetic force between m balls placed in n baskets.",
}

def solve(position: list[int], m: int) -> int:
    """
    Finds the maximum possible minimum magnetic force between m balls.

    Args:
        position: A list of integers representing the positions of the baskets.
        m: The number of balls to place in the baskets.

    Returns:
        The maximum possible minimum magnetic force.

    Examples:
        >>> solve([1, 2, 3, 4, 7], 3)
        3
        >>> solve([1, 1, 1], 3)
        0
    """
    # Sort positions to allow greedy placement and binary search on distance
    position.sort()
    
    def can_place_balls(min_distance: int) -> bool:
        """Checks if it is possible to place m balls with at least min_distance apart."""
        count = 1  # Place the first ball in the first basket
        last_position = position[0]
        
        for i in range(1, len(position)):
            # If the current basket is far enough from the last placed ball
            if position[i] - last_position >= min_distance:
                count += 1
                last_position = position[i]
                # If we have placed all m balls, the distance is feasible
                if count >= m:
                    return True
        return False

    # Binary search range: 
    # Low is 1 (minimum possible distance between two distinct baskets)
    # High is the distance between the first and last basket
    low = 1
    high = position[-1] - position[0]
    result = 0

    while low <= high:
        mid = (low + high) // 2
        
        # If it's possible to place balls with 'mid' distance, 
        # try to see if a larger distance is possible.
        if can_place_balls(mid):
            result = mid
            low = mid + 1
        else:
            # If not possible, we must reduce the required distance
            high = mid - 1
            
    return result
