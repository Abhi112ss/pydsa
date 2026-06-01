METADATA = {
    "id": 1094,
    "name": "Car Pooling",
    "slug": "car_pooling",
    "category": "Array",
    "aliases": [],
    "tags": ["difference_array", "sorting", "sweep_line"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Determine if a car can pick up and drop off all passengers at their designated locations without exceeding capacity.",
}

def solve(num_passengers: int, trips: list[list[int]]) -> bool:
    """
    Determines if the car can complete all trips without exceeding capacity.

    Args:
        num_passengers: The maximum capacity of the car.
        trips: A list of trips where each trip is [num_passengers, start_location, end_location].

    Returns:
        True if all trips can be completed, False otherwise.

    Examples:
        >>> solve(5, [[2, 1, 5], [3, 3, 7]])
        False
        >>> solve(5, [[2, 1, 5], [3, 5, 7]])
        True
    """
    # We use a sweep-line algorithm. 
    # We track the net change in passengers at every point where a trip starts or ends.
    events = []
    for count, start, end in trips:
        # At 'start', passengers increase
        events.append((start, count))
        # At 'end', passengers decrease
        events.append((end, -count))

    # Sort events by location. 
    # If two events have the same location, we must process the drop-offs (negative count) 
    # before the pick-ups (positive count) to avoid false capacity violations.
    # However, the problem states passengers are dropped off AT the end location, 
    # meaning they are no longer in the car at that exact coordinate.
    # Sorting by location first, then by the change in passengers (negative values first)
    # ensures we free up seats before taking new people at the same stop.
    events.sort()

    current_load = 0
    for _, passenger_change in events:
        current_load += passenger_change
        
        # If at any point the load exceeds capacity, return False
        if current_load > num_passengers:
            return False

    return True
