METADATA = {
    "id": 2437,
    "name": "Number of Valid Clock Times",
    "slug": "number-of-valid-clock-times",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the total number of unique valid clock times in a 24-hour format.",
}

def solve(hour_limit: int, minute_limit: int) -> int:
    """
    Calculates the number of valid clock times given the maximum hour and minute limits.

    A valid clock time is defined as (h, m) where 0 <= h < hour_limit and 0 <= m < minute_limit.
    The problem specifically asks for the count of valid times in a standard 24-hour format
    context, but provides limits for the calculation.

    Args:
        hour_limit (int): The upper bound (exclusive) for the hour component.
        minute_limit (int): The upper bound (exclusive) for the minute component.

    Returns:
        int: The total number of valid combinations of hours and minutes.

    Examples:
        >>> solve(24, 60)
        1440
        >>> solve(12, 60)
        720
    """
    # The total number of valid combinations is the product of the 
    # number of possible hour values and the number of possible minute values.
    # Since both limits are exclusive (0 <= h < hour_limit), 
    # there are exactly 'hour_limit' choices for h and 'minute_limit' choices for m.
    return hour_limit * minute_limit
