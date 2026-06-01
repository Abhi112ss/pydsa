METADATA = {
    "id": 3861,
    "name": "Minimum Capacity Box",
    "slug": "minimum_capacity_box",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log(sum(weights)))",
    "space_complexity": "O(1)",
    "description": "Find the minimum capacity required to transport all boxes within a given number of trips using binary search.",
}

def solve(weights: list[int], k: int) -> int:
    """
    Finds the minimum capacity of a box required to transport all items 
    within at most k trips.

    Args:
        weights: A list of integers representing the weight of each box.
        k: The maximum number of trips allowed.

    Returns:
        The minimum integer capacity required.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 3)
        6
        >>> solve([3, 2, 2, 4, 1], 3)
        4
    """
    
    def can_transport(capacity: int) -> bool:
        """Checks if it is possible to transport all weights with the given capacity."""
        trips_count = 1
        current_load = 0
        
        for weight in weights:
            # If a single weight exceeds capacity, this capacity is impossible
            if weight > capacity:
                return False
            
            if current_load + weight <= capacity:
                current_load += weight
            else:
                # Start a new trip
                trips_count += 1
                current_load = weight
                
        return trips_count <= k

    # The minimum possible capacity is the weight of the heaviest box
    # The maximum possible capacity is the sum of all weights (one trip)
    low = max(weights)
    high = sum(weights)
    result = high

    # Binary search on the capacity range
    while low <= high:
        mid = (low + high) // 2
        
        if can_transport(mid):
            # If mid works, try to find a smaller capacity
            result = mid
            high = mid - 1
        else:
            # If mid is too small, increase the capacity
            low = mid + 1
            
    return result
