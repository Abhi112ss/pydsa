METADATA = {
    "id": 1107,
    "name": "New Users Daily Count",
    "slug": "new-users-daily-count",
    "category": "Database/Algorithm",
    "aliases": [],
    "tags": ["hash_map", "arrays", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count the number of new users for each day based on their first login date.",
}

def solve(user_logins: list[list[int]]) -> list[list[int]]:
    """
    Calculates the number of new users for each day. A user is considered 'new' 
    on the day of their very first login.

    Args:
        user_logins: A list of lists where each inner list contains [user_id, login_date].
                     Note: login_date is represented as an integer (e.g., YYYYMMDD).

    Returns:
        A list of lists where each inner list contains [login_date, new_user_count],
        sorted by login_date in ascending order.

    Examples:
        >>> solve([[1, 20230101], [2, 20230101], [1, 20230102], [3, 20230102]])
        [[20230101, 2], [20230102, 1]]
        >>> solve([[1, 20230101], [1, 20230101]])
        [[20230101, 1]]
    """
    if not user_logins:
        return []

    # Step 1: Find the first login date for each user.
    # We use a dictionary to map user_id -> minimum_login_date.
    first_login_map: dict[int, int] = {}
    for user_id, login_date in user_logins:
        if user_id not in first_login_map or login_date < first_login_map[user_id]:
            first_login_map[user_id] = login_date

    # Step 2: Aggregate the counts of these first login dates.
    # We use a dictionary to map login_date -> count_of_new_users.
    daily_new_users: dict[int, int] = {}
    for first_date in first_login_map.values():
        daily_new_users[first_date] = daily_new_users.get(first_date, 0) + 1

    # Step 3: Format the result as a list of [date, count] and sort by date.
    # Sorting ensures the output meets the requirement of ascending order.
    sorted_dates = sorted(daily_new_users.keys())
    result: list[list[int]] = [[date, daily_new_users[date]] for date in sorted_dates]

    return result
