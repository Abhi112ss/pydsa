METADATA = {
    "id": 2837,
    "name": "Total Traveled Distance",
    "slug": "total-traveled-distance",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total distance traveled by a particle given its velocity function and time intervals.",
}

def solve(time: list[int], velocity: list[int]) -> int:
    """
    Calculates the total distance traveled by a particle based on velocity intervals.

    The velocity is constant within each time interval [time[i], time[i+1]].
    The distance traveled in an interval is (time[i+1] - time[i]) * velocity[i].

    Args:
        time: A list of integers representing the time points at which velocity changes.
        velocity: A list of integers representing the velocity during the interval 
                  starting at time[i].

    Returns:
        The total distance traveled as an integer.

    Examples:
        >>> solve([0, 1, 2], [1, 2])
        3
        >>> solve([0, 1, 2, 3], [1, 2, 3])
        6
    """
    total_distance = 0
    num_intervals = len(velocity)

    # Iterate through each velocity interval
    for i in range(num_intervals):
        # The duration of the current interval is the difference between 
        # the current time point and the next time point.
        # If it's the last velocity, the interval ends at the last time point.
        
        # Note: The problem implies velocity[i] is active from time[i] to time[i+1].
        # The length of the interval is time[i+1] - time[i].
        
        duration = time[i + 1] - time[i]
        
        # Distance = velocity * time
        total_distance += duration * velocity[i]

    return total_distance

# Note: The problem description for 2837 on LeetCode actually refers to 
# a specific problem involving a particle moving on a line with 
# velocity changing at specific time points. 
# The implementation above follows the standard integration logic.
