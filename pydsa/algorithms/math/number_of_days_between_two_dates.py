METADATA = {
    "id": 1360,
    "name": "Number of Days Between Two Dates",
    "slug": "number_of_days_between_two_dates",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "calendar"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Return the absolute number of days between two dates.",
}


def solve(date1: str, date2: str) -> int:
    """Calculate the absolute number of days between two dates.

    Args:
        date1: A date string in the format "YYYY-MM-DD".
        date2: A date string in the same format as ``date1``.

    Returns:
        The absolute difference in days between ``date1`` and ``date2``.

    Examples:
        >>> solve("2019-06-29", "2019-06-30")
        1
        >>> solve("2020-01-15", "2019-12-31")
        15
    """
    def is_leap_year(year: int) -> bool:
        """Return True if ``year`` is a leap year in the Gregorian calendar."""
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    # Days in each month for a non‑leap year; February will be adjusted later.
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def days_since_reference(date: str) -> int:
        """Convert a date to the number of days since 1900‑01‑01."""
        year, month, day = map(int, date.split("-"))

        # Count days contributed by full years before ``year``.
        days = 0
        for past_year in range(1900, year):
            days += 366 if is_leap_year(past_year) else 365

        # Count days contributed by full months before ``month`` in the current year.
        for past_month in range(1, month):
            days += month_lengths[past_month - 1]
            if past_month == 2 and is_leap_year(year):
                days += 1  # add leap day for February

        # Add days of the current month.
        days += day - 1  # subtract 1 because 1900‑01‑01 is day 0
        return days

    days1 = days_since_reference(date1)
    days2 = days_since_reference(date2)
    return abs(days1 - days2)