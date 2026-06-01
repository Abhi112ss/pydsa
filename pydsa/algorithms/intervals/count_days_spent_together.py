METADATA = {
    "id": 2409,
    "name": "Count Days Spent Together",
    "slug": "count_days_spent_together",
    "category": "Date",
    "aliases": [],
    "tags": ["intervals", "date", "math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Return the number of days two date intervals overlap.",
}


def solve(start_date1: str, end_date1: str, start_date2: str, end_date2: str) -> int:
    """Calculate the number of days two date intervals overlap.

    Args:
        start_date1: Start of the first interval in "YYYY-MM-DD" format.
        end_date1: End of the first interval in "YYYY-MM-DD" format.
        start_date2: Start of the second interval in "YYYY-MM-DD" format.
        end_date2: End of the second interval in "YYYY-MM-DD" format.

    Returns:
        The count of overlapping days (inclusive). Returns 0 if there is no overlap.

    Examples:
        >>> solve("2021-01-01", "2021-01-31", "2021-01-15", "2021-02-15")
        17
        >>> solve("2021-03-01", "2021-03-10", "2021-04-01", "2021-04-10")
        0
    """
    import datetime

    # Convert ISO strings to date objects.
    first_start = datetime.date.fromisoformat(start_date1)
    first_end = datetime.date.fromisoformat(end_date1)
    second_start = datetime.date.fromisoformat(start_date2)
    second_end = datetime.date.fromisoformat(end_date2)

    # Determine the intersection interval.
    overlap_start = max(first_start, second_start)
    overlap_end = min(first_end, second_end)

    # If the intervals intersect, compute inclusive day count; otherwise return 0.
    if overlap_start <= overlap_end:
        return (overlap_end - overlap_start).days + 1
    return 0