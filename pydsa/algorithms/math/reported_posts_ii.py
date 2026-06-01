METADATA = {
    "id": 1132,
    "name": "Reported Posts II",
    "slug": "reported_posts_ii",
    "category": "Aggregation",
    "aliases": [],
    "tags": ["array", "math", "prefix sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the average removal rate of reported posts across multiple days.",
}

def solve(reports: list[int], removals: list[int]) -> float:
    """
    Calculates the average removal rate across all days.
    
    The removal rate for a single day is defined as (removals[i] / reports[i]).
    The final answer is the average of these daily rates.

    Args:
        reports: A list of integers representing the number of reported posts each day.
        removals: A list of integers representing the number of removed posts each day.

    Returns:
        float: The average removal rate across all days.

    Examples:
        >>> solve([10, 20, 30], [2, 4, 6])
        0.2
        >>> solve([100, 50], [10, 25])
        0.35
    """
    if not reports:
        return 0.0

    total_daily_rate_sum = 0.0
    num_days = len(reports)

    for i in range(num_days):
        # Calculate the rate for the current day. 
        # We assume reports[i] > 0 based on problem constraints for valid rates.
        daily_rate = removals[i] / reports[i]
        total_daily_rate_sum += daily_rate

    # The average is the sum of all daily rates divided by the number of days.
    return total_daily_rate_sum / num_days
