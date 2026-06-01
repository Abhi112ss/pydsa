METADATA = {
    "id": 539,
    "name": "Minimum Time Difference",
    "slug": "minimum-time-difference",
    "category": "Math",
    "aliases": [],
    "tags": ["sorting", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum difference in minutes between any two time strings in a list.",
}

def solve(timePoints: list[str]) -> int:
    """
    Calculates the minimum difference in minutes between any two time points.

    Args:
        timePoints: A list of strings representing time in "HH:MM" format.

    Returns:
        The minimum difference in minutes between any two time points.

    Examples:
        >>> solve(["23:59", "00:00"])
        1
        >>> solve(["00:00", "23:59", "00:00"])
        0
        >>> solve(["01:01", "02:01"])
        60
    """
    # Convert all "HH:MM" strings into total minutes from 00:00
    minutes_list = []
    for time in timePoints:
        hours, minutes = map(int, time.split(':'))
        minutes_list.append(hours * 60 + minutes)

    # Sort the minutes to easily find the smallest difference between neighbors
    minutes_list.sort()

    # Initialize min_diff with a large value
    min_diff = float('inf')

    # Check the difference between all adjacent time points
    for i in range(len(minutes_list) - 1):
        diff = minutes_list[i + 1] - minutes_list[i]
        if diff < min_diff:
            min_diff = diff
            
    # Handle the wrap-around case (difference between the last and first time point)
    # Total minutes in a day is 24 * 60 = 1440
    wrap_around_diff = (1440 - minutes_list[-1]) + minutes_list[0]
    if wrap_around_diff < min_diff:
        min_diff = wrap_around_diff

    return int(min_diff)
