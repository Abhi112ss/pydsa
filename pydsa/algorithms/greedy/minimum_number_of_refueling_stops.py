METADATA = {
    "id": 871,
    "name": "Minimum Number of Refueling Stops",
    "slug": "minimum-number-of-refueling-stops",
    "category": "Greedy",
    "aliases": [],
    "tags": ["heap", "priority_queue", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of stops needed to reach a target distance given an initial fuel amount and a list of fuel stations.",
}

import heapq

def solve(target: int, start_fuel: int, stations: list[list[int]]) -> int:
    """
    Calculates the minimum number of refueling stops required to reach the target.

    The algorithm uses a greedy approach with a max-heap. We drive as far as 
    possible with the current fuel. Whenever we run out of fuel before reaching 
    the next station or the target, we retroactively "refuel" from the largest 
    available fuel station we have already passed.

    Args:
        target: The total distance to travel.
        start_fuel: The initial amount of fuel in the tank.
        stations: A list of [distance, fuel] pairs representing fuel stations.

    Returns:
        The minimum number of stops required, or -1 if the target is unreachable.

    Examples:
        >>> solve(100, 10, [[10, 60], [20, 30], [30, 30]])
        2
        >>> solve(100, 1, [[10, 100]])
        -1
    """
    # max_heap stores the fuel amounts of stations we have passed but not yet used.
    # Python's heapq is a min-heap, so we store negative values to simulate a max-heap.
    max_heap: list[int] = []
    
    current_fuel = start_fuel
    stops_made = 0
    prev_location = 0
    
    # Add a dummy station at the target location to simplify the loop logic
    # This ensures we process the distance to the target as a final "leg" of the journey.
    all_stations = stations + [[target, 0]]
    
    for station_distance, fuel_available in all_stations:
        distance_to_travel = station_distance - prev_location
        
        # While we don't have enough fuel to reach the next station/target
        while current_fuel < distance_to_travel:
            # If there are no passed stations to refuel from, we are stuck
            if not max_heap:
                return -1
            
            # Greedy choice: Refuel from the station with the most fuel encountered so far
            current_fuel += -heapq.heappop(max_heap)
            stops_made += 1
            
        # Move to the current station
        current_fuel -= distance_to_travel
        prev_location = station_distance
        
        # Add the current station's fuel to our potential refueling options
        if fuel_available > 0:
            heapq.heappush(max_heap, -fuel_available)
            
    return stops_made
