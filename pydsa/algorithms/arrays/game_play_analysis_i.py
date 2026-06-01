METADATA = {
    "id": 511,
    "name": "Game Play Analysis I",
    "slug": "game_play_analysis_i",
    "category": "database",
    "aliases": [],
    "tags": ["hash_map", "group_by"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the player ID whose earliest game timestamp is the smallest.",
}


def solve(playerId: list[int], timestamp: list[int]) -> int:
    """Find the player whose earliest game timestamp is the smallest.

    Args:
        playerId: List of player IDs, where playerId[i] is the ID of the player
            who played a game at timestamp[i].
        timestamp: List of timestamps corresponding to each game play.

    Returns:
        The player ID with the minimum earliest timestamp. If multiple players
        share the same earliest timestamp, the smallest player ID among them
        is returned.

    Examples:
        >>> solve([1,2,3,1,2], [5,3,4,2,1])
        2
        >>> solve([5,5,5], [10,5,7])
        5
    """
    # Map each player to their earliest timestamp.
    earliest_timestamp_by_player: dict[int, int] = {}
    for pid, ts in zip(playerId, timestamp):
        if pid not in earliest_timestamp_by_player:
            earliest_timestamp_by_player[pid] = ts
        else:
            # Keep the smaller (earlier) timestamp for this player.
            if ts < earliest_timestamp_by_player[pid]:
                earliest_timestamp_by_player[pid] = ts

    # Determine the player with the smallest earliest timestamp.
    result_player: int = -1
    smallest_timestamp: int = float('inf')
    for pid, earliest_ts in earliest_timestamp_by_player.items():
        if earliest_ts < smallest_timestamp:
            smallest_timestamp = earliest_ts
            result_player = pid
        elif earliest_ts == smallest_timestamp and pid < result_player:
            # Tie‑break by smaller player ID.
            result_player = pid

    return result_player