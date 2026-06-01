METADATA = {
    "id": 2777,
    "name": "Date Range Generator",
    "slug": "date-range-generator",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "date_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(d)",
    "space_complexity": "O(d)",
    "description": "Generate a list of dates in YYYY-MM-DD format between a start and end date inclusive.",
}

from datetime import datetime, timedelta

def solve(start_date_str: str, end_date_str: str) -> list[str]:
    """
    Generates a list of dates in 'YYYY-MM-DD' format from start_date to end_date inclusive.

    Args:
        start_date_str: The starting date in 'YYYY-MM-DD' format.
        end_date_str: The ending date in 'YYYY-MM-DD' format.

    Returns:
        A list of strings representing the sequence of dates.

    Examples:
        >>> solve("2023-01-01", "2023-01-03")
        ['2023-01-01', '2023-01-02', '2023-01-03']
        >>> solve("2023-12-31", "2024-01-01")
        ['2023-12-31', '2024-01-01']
    """
    # Parse the input strings into datetime objects for arithmetic operations
    date_format = "%Y-%m-%d"
    current_date = datetime.strptime(start_date_str, date_format)
    end_date = datetime.strptime(end_date_str, date_format)
    
    date_list: list[str] = []
    
    # Iterate from the start date to the end date, incrementing by one day at a time
    while current_date <= end_date:
        # Append the formatted string representation of the current date
        date_list.append(current_date.strftime(date_format))
        
        # Increment the current date by exactly one day
        current_date += timedelta(days=1)
        
    return date_list
