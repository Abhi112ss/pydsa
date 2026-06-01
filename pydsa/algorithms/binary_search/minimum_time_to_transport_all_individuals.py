METADATA = {
    "id": 3594,
    "name": "Minimum Time to Transport All Individuals",
    "slug": "minimum-time-to-transport-all-individuals",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log max_time)",
    "space_complexity": "O(1)",
    "description": "Find the minimum time required to transport all individuals given constraints on vehicle capacity and travel time.",
}

def solve(capacities: list[int], travel_times: list[int], individuals: int) -> int:
    """
    Calculates the minimum time required to transport all individuals using binary search.

    Args:
        capacities: A list of integers representing the capacity of each vehicle.
        travel_times: A list of integers representing the time taken by each vehicle for one trip.
        individuals: The total number of individuals that need to be transported.

    Returns:
        The minimum time required to transport all individuals.

    Examples:
        >>> solve([2, 3], [5, 10], 10)
        20
        >>> solve([1], [1], 5)
        5
    """
    
    def can_transport_in_time(limit_time: int) -> bool:
        """
        Checks if it is possible to transport all individuals within the given time limit.
        
        Args:
            limit_time: The maximum time allowed.
            
        Returns:
            True if all individuals can be transported, False otherwise.
        """
        total_transported = 0
        for capacity, time in zip(capacities, travel_times):
            if time <= 0:
                # If time is 0, this vehicle can transport infinite people in any time > 0
                # However, based on typical problem constraints, time is usually >= 1.
                # If time is 0, we treat it as a very large capacity.
                return True
            
            # Number of trips a vehicle can make within limit_time
            # Each trip takes 'time' units.
            num_trips = limit_time // time
            total_transported += num_trips * capacity
            
            if total_transported >= individuals:
                return True
        return total_transported >= individuals

    # Binary search range:
    # Minimum time could be 1 (or 0 if individuals is 0)
    # Maximum time could be the time taken by the slowest vehicle to transport everyone alone
    # To be safe, we use a large upper bound.
    low = 0
    high = max(travel_times) * individuals if individuals > 0 else 0
    # If individuals is 0, the answer is 0.
    if individuals == 0:
        return 0
        
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            # Avoid division by zero or logic errors with 0 time
            if can_transport_in_time(0):
                ans = 0
                high = -1
            else:
                low = 1
            continue

        if can_transport_in_time(mid):
            # If feasible, try to find a smaller time
            ans = mid
            high = mid - 1
        else:
            # If not feasible, we need more time
            low = mid + 1
            
    return ans
