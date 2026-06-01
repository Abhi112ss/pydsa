METADATA = {
    "id": 1454,
    "name": "Active Users",
    "slug": "active_users",
    "category": "Database/Logic",
    "aliases": [],
    "tags": ["math", "logic", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Identify users who logged in for five or more consecutive days.",
}

from datetime import datetime, timedelta

def solve(logins: list[dict]) -> list[int]:
    """
    Identifies users who have at least one sequence of 5 or more consecutive login days.

    Args:
        logins: A list of dictionaries, where each dictionary represents a login 
                event with 'user_id' (int) and 'login_date' (str in 'YYYY-MM-DD' format).

    Returns:
        A list of unique user IDs who meet the consecutive login criteria, 
        sorted in ascending order.

    Examples:
        >>> data = [
        ...     {"user_id": 1, "login_date": "2023-01-01"},
        ...     {"user_id": 1, "login_date": "2023-01-02"},
        ...     {"user_id": 1, "login_date": "2023-01-03"},
        ...     {"user_id": 1, "login_date": "2023-01-04"},
        ...     {"user_id": 1, "login_date": "2023-01-05"},
        ...     {"user_id": 2, "login_date": "2023-01-01"}
        ... ]
        >>> solve(data)
        [1]
    """
    # Group unique login dates by user_id
    user_logins: dict[int, set[datetime]] = {}
    for entry in logins:
        uid = entry["user_id"]
        # Parse date string into datetime object for arithmetic
        date_obj = datetime.strptime(entry["login_date"], "%Y-%m-%d")
        
        if uid not in user_logins:
            user_logins[uid] = set()
        user_logins[uid].add(date_obj)

    active_users: list[int] = []

    for user_id, dates_set in user_logins.items():
        # Sort unique dates to check for continuity
        sorted_dates = sorted(list(dates_set))
        
        # A sequence of 5 consecutive days means:
        # date[i+4] - date[i] == 4 days
        is_active = False
        if len(sorted_dates) >= 5:
            for i in range(len(sorted_dates) - 4):
                # Check if the date 4 steps ahead is exactly 4 days after current date
                if (sorted_dates[i + 4] - sorted_dates[i]).days == 4:
                    is_active = True
                    break
        
        if is_active:
            active_users.append(user_id)

    # Return sorted list of user IDs as per standard requirements
    return sorted(active_users)
