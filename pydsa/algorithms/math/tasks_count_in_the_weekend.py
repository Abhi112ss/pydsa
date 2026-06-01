METADATA = {
    "id": 2298,
    "name": "Tasks Count in the Weekend",
    "slug": "tasks-count-in-the-weekend",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of weekend days (Saturdays and Sundays) between two given dates.",
}

from datetime import date, timedelta

def solve(start_date_str: str, end_date_str: str) -> int:
    """
    Calculates the number of Saturdays and Sundays between two dates inclusive.

    Args:
        start_date_str: The starting date in 'YYYY-MM-DD' format.
        end_date_str: The ending date in 'YYYY-MM-DD' format.

    Returns:
        The total count of weekend days (Saturday and Sunday) in the range.

    Examples:
        >>> solve("2023-10-01", "2023-10-07")
        2
        >>> solve("2023-10-06", "2023-10-08")
        3
    """
    # Parse strings into date objects
    start_date = date.fromisoformat(start_date_str)
    end_date = date.fromisoformat(end_date_str)
    
    # Total number of days in the range (inclusive)
    total_days = (end_date - start_date).days + 1
    
    # Calculate how many full weeks are in the range
    full_weeks = total_days // 7
    weekend_count = full_weeks * 2
    
    # Calculate the remaining days after full weeks are accounted for
    remaining_days = total_days % 7
    
    # If there are remaining days, check each one to see if it's a weekend
    # weekday() returns 0 for Monday, 5 for Saturday, 6 for Sunday
    current_day = start_date + timedelta(days=full_weeks * 7)
    for _ in range(remaining_days):
        if current_day.weekday() >= 5:
            weekend_count += 1
        current_day += timedelta(days=1)
            
    return weekend_count
