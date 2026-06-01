METADATA = {
    "id": 2187,
    "name": "Minimum Time to Complete Trips",
    "slug": "minimum-time-to-complete-trips",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log(max_time))",
    "space_complexity": "O(1)",
    "description": "Find the minimum time required for a set of buses to complete a given number of trips.",
}

def solve(time: list[int], total_trips: int) -> int:
    """
    Calculates the minimum time required to complete the specified number of trips.

    Args:
        time: A list of integers where time[i] is the time taken by the i-th bus to complete one trip.
        total_trips: The total number of trips that must be completed.

    Returns:
        The minimum integer time required to complete at least total_trips.

    Examples:
        >>> solve([1, 2, 3], 5)
        3
        >>> solve([3, 5, 10], 1)
        3
    """
    # The minimum possible time is 1 (assuming all times >= 1)
    # The maximum possible time is the time taken by the fastest bus to do all trips
    fastest_bus_time = min(time)
    low = 1
    high = fastest_bus_time * total_trips
    
    ans = high

    while low <= high:
        mid = (low + high) // 2
        
        # Calculate how many trips all buses can complete in 'mid' time
        current_total_trips = 0
        for bus_time in time:
            current_total_trips += mid // bus_time
            # Optimization: if we already met the requirement, stop counting
            if current_total_trips >= total_trips:
                break
        
        # If the current time allows for enough trips, try to find a smaller time
        if current_total_trips >= total_trips:
            ans = mid
            high = mid - 1
        else:
            # If not enough trips, we need more time
            low = mid + 1
            
    return ans
