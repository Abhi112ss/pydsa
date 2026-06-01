METADATA = {
    "id": 2651,
    "name": "Calculate Delayed Arrival Time",
    "slug": "calculate_delayed_arrival_time",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the actual arrival time given a scheduled time, a delay, and a travel duration.",
}

def solve(scheduled_time: int, delay: int, travel_duration: int) -> int:
    """
    Calculates the actual arrival time by adding the delay and travel duration 
    to the scheduled time.

    Args:
        scheduled_time (int): The time the journey was originally supposed to start.
        delay (int): The amount of time (in minutes/units) the start is delayed.
        travel_duration (int): The time required to complete the journey.

    Returns:
        int: The actual time of arrival.

    Examples:
        >>> solve(10, 5, 20)
        35
        >>> solve(100, 0, 50)
        150
    """
    # The actual departure time is the scheduled time plus the delay.
    actual_departure_time = scheduled_time + delay
    
    # The arrival time is the actual departure time plus the time spent traveling.
    actual_arrival_time = actual_departure_time + travel_duration
    
    return actual_arrival_time
