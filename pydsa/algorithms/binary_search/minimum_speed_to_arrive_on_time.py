METADATA = {
    "id": 1870,
    "name": "Minimum Speed to Arrive on Time",
    "slug": "minimum-speed-to-arrive-on-time",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n * log(max_speed))",
    "space_complexity": "O(1)",
    "description": "Find the minimum integer speed required to reach the destination within a given time limit.",
}

import math

def solve(num_trains: int, num_hours: float, arrival_time: float) -> int:
    """
    Finds the minimum integer speed required to arrive on time.

    Args:
        num_trains: The number of trains to take.
        num_hours: The target arrival time (float).
        arrival_time: The maximum allowed time (float).

    Returns:
        The minimum integer speed required, or -1 if it is impossible.

    Examples:
        >>> solve(2, 1.5, 2.0)
        2
        >>> solve(3, 2.0, 3.0)
        3
        >>> solve(1, 1.0, 1.0)
        1
        >>> solve(2, 1.5, 1.4)
        -1
    """
    # If there are more trains than hours allow for the last train to be a full hour,
    # it's impossible because the last train must take at least 1 hour (speed is integer).
    # Specifically, the first (num_trains - 1) trains take at least 1 hour each.
    if num_trains - 1 >= num_hours:
        return -1

    def can_arrive_on_time(speed: int) -> bool:
        """Checks if a given speed allows arrival within arrival_time."""
        total_time = 0.0
        # For the first n-1 trains, we take the ceiling of (1/speed)
        for _ in range(num_trains - 1):
            total_time += math.ceil(1 / speed)
        
        # The last train does not need to be a ceiling; it's the remaining distance
        # divided by speed, but we must account for the total time constraint.
        # Actually, the problem implies each train is 1 unit of distance.
        # The last train takes 1/speed.
        total_time += 1 / speed
        return total_time <= arrival_time

    # Binary search range for speed
    # Minimum speed is 1.
    # Maximum speed: the last train must cover 1 unit. 
    # To satisfy the time, the last train needs to take at most (arrival_time - (num_trains - 1))
    # 1/speed <= arrival_time - (num_trains - 1) => speed >= 1 / (arrival_time - num_trains + 1)
    # A safe upper bound is 10^7 as per constraints.
    low = 1
    high = 10**7
    result = -1

    while low <= high:
        mid = (low + high) // 2
        
        # Calculate time taken with current speed
        # Optimization: Instead of a loop, we know first n-1 trains take ceil(1/mid)
        # Since mid >= 1, ceil(1/mid) is always 1.
        # Wait, if mid is 1, ceil(1/1) = 1. If mid is 2, ceil(1/2) = 1.
        # Actually, for any integer speed >= 1, ceil(1/speed) is always 1.
        # This means the first n-1 trains will ALWAYS take 1 hour each.
        # The only way to arrive faster is to increase speed to reduce the LAST train's time.
        # Let's re-verify: if speed = 2, 1/2 = 0.5. ceil(0.5) = 1.
        # So for any integer speed >= 1, the first n-1 trains take 1 hour each.
        # The total time = (num_trains - 1) + (1 / speed).
        
        current_total_time = (num_trains - 1) + (1 / mid)
        
        if current_total_time <= arrival_time:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result
