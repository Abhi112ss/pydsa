METADATA = {
    "id": 3733,
    "name": "Minimum Time to Complete All Deliveries",
    "slug": "minimum-time-to-complete-all-deliveries",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log(max_time))",
    "space_complexity": "O(1)",
    "description": "Find the minimum time required to complete all deliveries using binary search on the answer and a greedy feasibility check.",
}

def solve(deliveries: list[int], capacity: int) -> int:
    """
    Calculates the minimum time required to complete all deliveries given a vehicle capacity.

    Args:
        deliveries: A list of integers where each element represents the weight of a delivery.
        capacity: The maximum weight a vehicle can carry in one trip.

    Returns:
        The minimum time (number of trips) required to complete all deliveries.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 5)
        3
        >>> solve([10, 20, 30], 15)
        3
    """
    
    def can_complete(max_trips: int) -> bool:
        """
        Checks if it is possible to complete all deliveries within the given max_trips.
        
        Args:
            max_trips: The maximum number of trips allowed.
            
        Returns:
            True if possible, False otherwise.
        """
        current_trips = 1
        current_load = 0
        
        for weight in deliveries:
            # If a single delivery exceeds capacity, it's impossible
            if weight > capacity:
                return False
            
            # If adding this weight exceeds capacity, start a new trip
            if current_load + weight > capacity:
                current_trips += 1
                current_load = weight
            else:
                current_load += weight
                
            # If we exceed the allowed number of trips, return False early
            if current_trips > max_trips:
                return False
                
        return True

    # Edge case: if there are no deliveries
    if not deliveries:
        return 0

    # Binary search range: 
    # Minimum trips: at least 1 (or len(deliveries) if capacity is small)
    # Maximum trips: one trip per delivery
    low = 1
    high = len(deliveries)
    ans = len(deliveries)

    while low <= high:
        mid = (low + high) // 2
        
        # Check if the current 'mid' number of trips is feasible
        if can_complete(mid):
            ans = mid
            high = mid - 1  # Try to find a smaller number of trips
        else:
            low = mid + 1   # Need more trips to satisfy capacity constraints

    return ans
