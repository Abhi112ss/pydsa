METADATA = {
    "id": 1890,
    "name": "The Latest Login in 2020",
    "slug": "the-latest-login-in-2020",
    "category": "Database/Algorithm",
    "aliases": [],
    "tags": ["hash_map", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the latest login date for each user that occurred within the year 2020.",
}

def solve(logins: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    Finds the latest login date for each user that occurred in the year 2020.

    Args:
        logins: A list of dictionaries, where each dictionary contains 
                'user_id' (str) and 'login_date' (str in 'YYYY-MM-DD' format).

    Returns:
        A list of dictionaries containing 'user_id' and 'last_login' for 
        each user who logged in during 2020.

    Examples:
        >>> data = [
        ...     {"user_id": "1", "login_date": "2020-01-01"},
        ...     {"user_id": "1", "login_date": "2020-05-20"},
        ...     {"user_id": "2", "login_date": "2019-12-31"},
        ...     {"user_id": "2", "login_date": "2020-02-15"},
        ...     {"user_id": "3", "login_date": "2021-01-01"}
        ... ]
        >>> solve(data)
        [{'user_id': '1', 'last_login': '2020-05-20'}, {'user_id': '2', 'last_login': '2020-02-15'}]
    """
    # Map to store the maximum date found for each user_id
    latest_logins_map: dict[str, str] = {}

    for entry in logins:
        user_id = entry["user_id"]
        login_date = entry["login_date"]

        # Check if the login occurred within the year 2020
        if login_date.startswith("2020"):
            # If user is new or this date is later than the stored date, update map
            # String comparison works for ISO 8601 dates (YYYY-MM-DD)
            if user_id not in latest_logins_map or login_date > latest_logins_map[user_id]:
                latest_logins_map[user_id] = login_date

    # Format the result as a list of dictionaries
    result: list[dict[str, str]] = []
    for user_id, last_login in latest_logins_map.items():
        result.append({
            "user_id": user_id,
            "last_login": last_login
        })

    return result
