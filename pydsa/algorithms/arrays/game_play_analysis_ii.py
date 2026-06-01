METADATA = {
    "id": 512,
    "name": "Game Play Analysis II",
    "slug": "game-play-analysis-ii",
    "category": "Database",
    "aliases": [],
    "tags": ["hash_map", "filtering"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the device ID of the first login for each player.",
}

def solve(player_logins: list[dict[str, any]]) -> list[dict[str, int]]:
    """
    Args:
        player_logins: A list of dictionaries where each dictionary represents a login event 
                       containing 'player_id', 'device_id', and 'event_date'.

    Returns:
        A list of dictionaries containing the 'player_id' and the 'device_id' of their first login.
    """
    first_login_map = {}

    for record in player_logins:
        player_id = record["player_id"]
        device_id = record["device_id"]
        event_date = record["event_date"]

        if player_id not in first_login_map:
            first_login_map[player_id] = {"date": event_date, "device_id": device_id}
        else:
            if event_date < first_login_map[player_id]["date"]:
                first_login_map[player_id] = {"date": event_date, "device_id": device_id}

    result = []
    for player_id, data in first_login_map.items():
        result.append({
            "player_id": player_id,
            "device_id": data["device_id"]
        })

    return result