METADATA = {
    "id": 1154,
    "name": "Day of the Year",
    "slug": "day_of_the_year",
    "category": "Math",
    "aliases": ["dayOfYear"],
    "tags": ["math", "date_processing"],
    "difficulty": "Easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Convert a date string (YYYY-MM-DD) to its day-of-year number.",
}


def solve(date: str) -> int:
    """Convert a date string to its day-of-year number.

    Args:
        date: A string representing a date in the format "YYYY-MM-DD".

    Returns:
        An integer representing the day of the year (1 through 365 or 366).

    Examples:
        >>> solve("2019-01-09")
        9
        >>> solve("2019-02-10")
        41
        >>> solve("2003-03-01")
        60
        >>> solve("2004-03-01")
        61
    """
    # Parse year, month, and day as integers.
    year_str, month_str, day_str = date.split("-")
    year: int = int(year_str)
    month: int = int(month_str)
    day: int = int(day_str)

    # Determine if the given year is a leap year.
    is_leap_year: bool = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    # Days in each month; February is adjusted for leap years.
    days_in_month: list[int] = [31, 29 if is_leap_year else 28, 31, 30, 31, 30,
                                31, 31, 30, 31, 30, 31]

    # Sum days of all preceding months.
    days_before_current_month: int = sum(days_in_month[: month - 1])

    # Day of year is days before current month plus the current day.
    day_of_year: int = days_before_current_month + day
    return day_of_year