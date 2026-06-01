METADATA = {
    "id": 550,
    "name": "Game Play Analysis IV",
    "slug": "game-play-analysis-iv",
    "category": "Database/Logic",
    "aliases": [],
    "tags": ["logic", "data_processing", "sql-equivalent"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the fraction of players that logged in again on the day immediately after their first login.",
}

from datetime import datetime, timedelta

def solve(player_logins: list[dict[str, str]]) -> float:
    """
    Calculates the fraction of players that logged in on the day immediately 
    after their very first login date.

    Args:
        player_logins: A list of dictionaries where each dictionary represents 
            a login record with 'player_id' (int) and 'event_date' (str in 'YYYY-MM-DD').

    Returns:
        float: The fraction of players who logged in the day after their first login.

    Examples:
        >>> logs = [
        ...     {"player_id": 1, "event_date": "2016-03-01"},
        ...     {"player_id": 1, "event_date": "2016-03-02"},
        ...     {"player_id": 2, "event_date": "2016-03-01"},
        ...     {"player_id": 3, "event_date": "2017-06-25"},
        ...     {"player_id": 3, "event_date": "2017-06-26"}
        ... ]
        >>> solve(logs)
        0.6666666666666666
    """
    if not player_logins:
        return 0.0

    # Map to store the earliest login date for each player
    first_login_map: dict[int, datetime] = {}
    # Set to store all unique login dates for each player for O(1) lookup
    # We use a set of (player_id, date) tuples to represent the existence of a login
    all_logins: set[tuple[int, datetime]] = set()

    for record in player_logins:
        player_id = record["player_id"]
        # Convert string date to datetime object for arithmetic
        current_date = datetime.strptime(record["event_date"], "%Y-%m-%d")
        
        all_logins.add((player_id, current_date))

        # Track the minimum (first) login date per player
        if player_id not in first_login_map or current_date < first_login_map[player_id]:
            first_login_map[player_id] = current_date

    total_players = len(first_login_map)
    consecutive_login_players = 0

    # Iterate through each player's first login and check if they logged in the next day
    for player_id, first_date in first_login_map.items():
        next_day = first_date + timedelta(days=1)
        
        # Check if the (player, first_date + 1) tuple exists in our set of all logins
        if (player_id, next_day) in all_logins:
            consecutive_login_players += 1

    return consecutive_login_players / total_players
