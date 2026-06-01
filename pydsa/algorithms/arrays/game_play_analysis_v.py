METADATA = {
    "id": 1097,
    "name": "Game Play Analysis V",
    "slug": "game-play-analysis-v",
    "category": "Database",
    "aliases": [],
    "tags": ["sql", "window_functions"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Identify players who logged in on two consecutive days starting from their very first login date.",
}

from datetime import datetime, timedelta

def solve(player_logins: list[dict[str, str]]) -> list[int]:
    """
    Identifies players who logged in on two consecutive days, 
    starting from their first recorded login date.

    Args:
        player_logins: A list of dictionaries where each dictionary 
            contains 'player_id' (int) and 'event_date' (str in 'YYYY-MM-DD' format).

    Returns:
        A list of player_ids who met the criteria.

    Examples:
        >>> data = [
        ...     {"player_id": 1, "event_date": "2016-03-01"},
        ...     {"player_id": 1, "event_date": "2016-03-02"},
        ...     {"player_id": 2, "event_date": "2017-06-25"},
        ...     {"player_id": 2, "event_date": "2017-06-26"},
        ...     {"player_id": 3, "event_date": "2017-06-25"}
        ... ]
        >>> solve(data)
        [1, 2]
    """
    if not player_logins:
        return []

    # Map to store the earliest login date for each player
    first_login_map: dict[int, datetime] = {}
    # Set to store all login dates for each player for O(1) lookup
    all_logins_map: dict[int, set[datetime]] = {}

    for record in player_logins:
        player_id = record["player_id"]
        current_date = datetime.strptime(record["event_date"], "%Y-%m-%d")

        # Track all login dates to check for consecutive days later
        if player_id not in all_logins_map:
            all_logins_map[player_id] = set()
        all_logins_map[player_id].add(current_date)

        # Track the absolute first login date for each player
        if player_id not in first_login_map or current_date < first_login_map[player_id]:
            first_login_map[player_id] = current_date

    result_players: list[int] = []

    # Iterate through players to check the consecutive day condition
    for player_id, first_date in first_login_map.items():
        # The requirement is: login on first_date AND login on (first_date + 1 day)
        next_day = first_date + timedelta(days=1)
        
        # Check if the next consecutive day exists in the player's login history
        if next_day in all_logins_map[player_id]:
            result_players.append(player_id)

    return result_players
