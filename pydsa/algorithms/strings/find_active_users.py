METADATA = {
    "id": 2688,
    "name": "Find Active Users",
    "slug": "find_active_users",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Identify users who have activity on every day of the last 7 days.",
}


def solve(activity: list[tuple[int, str]]) -> list[int]:
    """Identify users who performed an activity on each of the last 7 days.

    Args:
        activity: A list of tuples where each tuple contains a user ID (int)
            and an activity date (ISO‑format string, e.g., "2023-01-07").

    Returns:
        A sorted list of user IDs that have activity records for every day in the
        most recent 7‑day window (including the latest date present in the data).

    Examples:
        >>> records = [
        ...     (1, "2023-01-01"), (1, "2023-01-02"), (1, "2023-01-03"),
        ...     (1, "2023-01-04"), (1, "2023-01-05"), (1, "2023-01-06"),
        ...     (1, "2023-01-07"),
        ...     (2, "2023-01-01"), (2, "2023-01-03"),
        ... ]
        >>> solve(records)
        [1]
    """
    from datetime import datetime, timedelta

    if not activity:
        return []

    # Convert date strings to date objects and track the maximum date.
    max_date = datetime.min.date()
    user_dates: dict[int, set[datetime.date]] = {}
    for user_id, date_str in activity:
        activity_date = datetime.fromisoformat(date_str).date()
        if activity_date > max_date:
            max_date = activity_date
        # Aggregate dates per user.
        if user_id not in user_dates:
            user_dates[user_id] = set()
        user_dates[user_id].add(activity_date)

    # Build the required 7‑day window ending at max_date.
    required_dates = {max_date - timedelta(days=offset) for offset in range(7)}

    # Select users whose date set covers the entire required window.
    active_users = [
        user_id
        for user_id, dates in user_dates.items()
        if required_dates.issubset(dates)
    ]

    return sorted(active_users)