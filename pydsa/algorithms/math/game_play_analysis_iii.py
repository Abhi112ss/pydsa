METADATA = {
    "id": 534,
    "name": "Game Play Analysis III",
    "slug": "game-play-analysis-iii",
    "category": "Database/SQL Simulation",
    "aliases": [],
    "tags": ["prefix_sum", "sorting", "grouping"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the fraction of players that logged in again on the day immediately after their first login.",
}

def solve(player_logins: list[dict[str, int]]) -> float:
    """
    Calculates the fraction of players who logged in on the day immediately 
    following their very first login day.

    Args:
        player_logins: A list of dictionaries where each dictionary represents 
            a login event with 'player_id' and 'event_date' (as integer timestamps).

    Returns:
        The fraction of players who logged in on the day after their first login.

    Examples:
        >>> logs = [
        ...     {"player_id": 1, "event_date": 1},
        ...     {"player_id": 1, "event_date": 2},
        ...     {"player_id": 2, "event_date": 1},
        ...     {"player_id": 3, "event_date": 1},
        ...     {"player_id": 3, "event_date": 3}
        ... ]
        >>> solve(logs)
        0.3333333333333333
    """
    if not player_logins:
        return 0.0

    # Sort logs by player_id then by event_date to easily find first login
    # and subsequent logins for each player.
    player_logins.sort(key=lambda x: (x["player_id"], x["event_date"]))

    first_login_dates: dict[int, int] = {}
    all_players: set[int] = set()
    
    # Identify the first login date for every unique player
    for entry in player_logins:
        p_id = entry["player_id"]
        date = entry["event_date"]
        all_players.add(p_id)
        if p_id not in first_login_dates:
            first_login_dates[p_id] = date

    # Count how many players logged in exactly one day after their first login
    consecutive_login_count = 0
    
    # We use a set of (player_id, date) to handle potential duplicate logs 
    # in the input, though the problem implies unique entries.
    unique_logins = set((entry["player_id"], entry["event_date"]) for entry in player_logins)

    for p_id, first_date in first_login_dates.items():
        # Check if the player has a record for the day immediately following the first login
        if (p_id, first_date + 1) in unique_logins:
            consecutive_login_count += 1

    return consecutive_login_count / len(all_players)
