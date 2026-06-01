METADATA = {
    "id": 1141,
    "name": "User Activity for the Past 30 Days I",
    "slug": "user_activity_for_the_past_30_days_i",
    "category": "Database",
    "aliases": [],
    "tags": ["hash_map", "date_processing"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count distinct active users for each of the past 30 days.",
}


def solve(activity: list[tuple[int, str]]) -> list[int]:
    """Count distinct users for each of the past 30 days.

    Args:
        activity: A list of tuples where each tuple contains a user ID (int)
            and an activity date string in the format "YYYY-MM-DD".

    Returns:
        A list of 30 integers. The first element corresponds to today,
        the second to yesterday, and so on up to 29 days ago. Each integer
        is the number of unique users who were active on that day.

    Examples:
        >>> logs = [
        ...     (1, "2023-04-01"),
        ...     (2, "2023-04-01"),
        ...     (1, "2023-04-02"),
        ... ]
        >>> # Assuming today is 2023-04-02
        >>> solve(logs)
        [1, 2] + [0]*28
    """
    import datetime

    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=29)  # inclusive 30‑day window

    # Map each date to a set of unique user IDs seen on that date.
    users_per_day: dict[datetime.date, set[int]] = {}

    for user_id, date_str in activity:
        # Parse the date string; ignore records that cannot be parsed.
        try:
            activity_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            continue

        # Only consider dates within the 30‑day window.
        if start_date <= activity_date <= today:
            if activity_date not in users_per_day:
                users_per_day[activity_date] = set()
            users_per_day[activity_date].add(user_id)

    # Build the result list: counts for today, yesterday, ..., 29 days ago.
    distinct_counts: list[int] = []
    for offset in range(30):
        day = today - datetime.timedelta(days=offset)
        distinct_counts.append(len(users_per_day.get(day, set())))

    return distinct_counts