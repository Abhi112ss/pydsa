METADATA = {
    "id": 1142,
    "name": "User Activity for the Past 30 Days II",
    "slug": "user-activity-for-the-past-30-days-ii",
    "category": "Database",
    "aliases": [],
    "tags": ["hash_map", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the average number of unique sessions per user for the last 30 days.",
}

def solve(user_sessions: list[dict]) -> float:
    """
    Calculates the average number of unique sessions per user for the last 30 days.

    Args:
        user_sessions: A list of dictionaries where each dictionary contains 
            'user_id', 'session_id', and 'activity_date'.

    Returns:
        The average number of unique sessions per user, rounded to 2 decimal places.

    Examples:
        >>> data = [
        ...     {"user_id": 1, "session_id": 1, "activity_date": "2019-01-01"},
        ...     {"user_id": 1, "session_id": 1, "activity_date": "2019-01-01"},
        ...     {"user_id": 1, "session_id": 2, "activity_date": "2019-01-02"},
        ...     {"user_id": 2, "session_id": 3, "activity_date": "2019-01-01"}
        ... ]
        >>> solve(data)
        1.5
    """
    if not user_sessions:
        return 0.0

    # Find the maximum date to determine the 30-day window
    # In a real SQL environment, this is handled by the database engine
    max_date_str = ""
    for entry in user_sessions:
        if entry["activity_date"] > max_date_str:
            max_date_str = entry["activity_date"]

    from datetime import datetime, timedelta
    max_date = datetime.strptime(max_date_str, "%Y-%m-%d")
    start_date = max_date - timedelta(days=29)

    # Maps user_id -> set of unique session_ids
    user_to_sessions = {}

    for entry in user_sessions:
        current_date = datetime.strptime(entry["activity_date"], "%Y-%m-%d")
        
        # Filter for the last 30 days (inclusive of max_date)
        if start_date <= current_date <= max_date:
            user_id = entry["user_id"]
            session_id = entry["session_id"]
            
            if user_id not in user_to_sessions:
                user_to_sessions[user_id] = set()
            
            # Using a set automatically handles duplicate session_id entries for the same user
            user_to_sessions[user_id].add(session_id)

    if not user_to_sessions:
        return 0.0

    # Calculate total unique sessions across all users in the window
    total_unique_sessions = sum(len(sessions) for sessions in user_to_sessions.values())
    
    # Calculate total unique users in the window
    total_unique_users = len(user_to_sessions)

    # The result is the average: total sessions / total users
    return round(total_unique_sessions / total_unique_users, 2)
