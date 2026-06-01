METADATA = {
    "id": 1118,
    "name": "Number of Days in a Month",
    "slug": "number-of-days-in-a-month",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Given a month and a year, return the number of days in that month.",
}

def solve(month: int, year: int) -> int:
    """
    Calculates the number of days in a given month and year.

    Args:
        month (int): The month of the year (1-indexed, 1 to 12).
        year (int): The year.

    Returns:
        int: The number of days in the specified month.

    Examples:
        >>> solve(1, 2023)
        31
        >>> solve(2, 2024)
        29
        >>> solve(2, 2023)
        28
    """
    # Lookup table for days in months (index 0 is a placeholder for 1-based indexing)
    # Months: Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
    days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Handle February leap year logic
    if month == 2:
        # A year is a leap year if it is divisible by 4 but not by 100,
        # OR if it is divisible by 400.
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        return 29 if is_leap_year else 28

    # For all other months, return the value from the lookup table
    return days_in_months[month]
