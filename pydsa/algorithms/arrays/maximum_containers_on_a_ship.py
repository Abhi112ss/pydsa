METADATA = {
    "id": 3492,
    "name": "Maximum Containers on a Ship",
    "slug": "maximum-containers-on-a-ship",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of containers that can be placed on a ship given its capacity and container weights using a greedy approach.",
}

def solve(capacity: int, weights: list[int]) -> int:
    """
    Calculates the maximum number of containers that can fit on a ship.

    The algorithm uses a greedy approach by sorting the containers from lightest 
    to heaviest to maximize the count of containers that can fit within the 
    given capacity.

    Args:
        capacity: The maximum total weight the ship can carry.
        weights: A list of integers representing the weight of each container.

    Returns:
        The maximum number of containers that can be loaded onto the ship.

    Examples:
        >>> solve(10, [5, 2, 3, 1, 7])
        4
        >>> solve(5, [10, 20, 30])
        0
        >>> solve(15, [5, 5, 5, 5, 5])
        3
    """
    # Sort weights to pick the smallest containers first (Greedy Strategy)
    # This ensures we maximize the count of items for a fixed capacity.
    sorted_weights = sorted(weights)
    
    total_weight = 0
    container_count = 0
    
    for weight in sorted_weights:
        # Check if adding the current lightest container exceeds capacity
        if total_weight + weight <= capacity:
            total_weight += weight
            container_count += 1
        else:
            # Since weights are sorted, no subsequent container will fit
            break
            
    return container_count
