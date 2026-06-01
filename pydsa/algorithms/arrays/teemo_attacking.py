METADATA = {
    "id": 495,
    "name": "Teemo Attacking",
    "slug": "teemo_attacking",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate total poisoned time given attack timestamps and poison duration.",
}


def solve(time_series: list[int], duration: int) -> int:
    """Calculate the total time Ashe is poisoned.

    Args:
        time_series: A list of ascending integers representing the times at which
            Teemo attacks.
        duration: An integer representing the duration of poison effect for each attack.

    Returns:
        The total number of seconds Ashe is poisoned.

    Examples:
        >>> solve([1, 4], 2)
        4
        >>> solve([1, 2], 2)
        3
    """
    if not time_series:
        return 0

    total_poisoned_time = 0
    for index in range(len(time_series) - 1):
        # Add the smaller of the fixed duration and the gap to the next attack
        time_gap = time_series[index + 1] - time_series[index]
        total_poisoned_time += min(duration, time_gap)

    # Add duration for the final attack (no following attack to truncate it)
    total_poisoned_time += duration
    return total_poisoned_time