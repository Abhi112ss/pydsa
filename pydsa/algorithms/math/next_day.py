METADATA = {
    "id": 2758,
    "name": "Next Day",
    "slug": "next-day",
    "category": "Simulation",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Given a date in the format [day, month, year], return the next day in the same format.",
}

def solve(date: list[int]) -> list[int]:
    """
    Calculates the next day given a current date [day, month, year].

    Args:
        date: A list of three integers representing [day, month, year].

    Returns:
        A list of three integers representing the next day [day, month, year].

    Examples:
        >>> solve([1, 1, 2024])
        [2, 1, 2024]
        >>> solve([31, 1, 2024])
        [1, 2, 2024]
        >>> solve([28, 2, 2024])
        [29, 2, 2024]
        >>> solve([29, 2, 2024])
        [1, 3, 2024]
    """
    day, month, year = date

    def is_leap_year(y: int) -> bool:
        """Checks if a year is a leap year."""
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    # Days in each month (index 0 is dummy, index 1 is Jan, etc.)
    # February is handled separately due to leap years
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Adjust February if it's a leap year
    if is_leap_year(year):
        days_in_month[2] = 29

    # Increment the day
    day += 1

    # Check if we have exceeded the number of days in the current month
    if day > days_in_month[month]:
        day = 1
        month += 1

        # Check if we have exceeded the number of months in a year
        if month > 12:
            month = 1
            year += 1

    return [day, month, year]
