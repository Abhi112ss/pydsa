METADATA = {
    "id": 1709,
    "name": "Biggest Window Between Visits",
    "slug": "biggest_window_between_visits",
    "category": "array",
    "aliases": [],
    "tags": ["array", "string", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the largest time gap in minutes between consecutive visits after sorting timestamps.",
}

def solve(timestamps: list[str]) -> int:
    """Calculate the biggest window between consecutive visits.

    Args:
        timestamps: A list of strings representing visit times in "HH:MM" format.

    Returns:
        The maximum difference in minutes between any two consecutive visits after
        sorting. Returns 0 if there are duplicate timestamps or fewer than two visits.

    Examples:
        >>> solve(["23:59","00:00"])
        1439
        >>> solve(["12:30","12:30"])
        0
        >>> solve(["01:00","02:00","04:00"])
        120
    """
    # There are only 24*60 possible minutes in a day.
    minutes_in_day = 24 * 60
    visited = [False] * minutes_in_day

    # Convert each timestamp to minutes and detect duplicates.
    for ts in timestamps:
        hour_str, minute_str = ts.split(":")
        total_minutes = int(hour_str) * 60 + int(minute_str)
        if visited[total_minutes]:
            return 0  # duplicate timestamp found
        visited[total_minutes] = True

    # Need at least two distinct timestamps to have a window.
    if sum(visited) < 2:
        return 0

    previous_minute = None
    max_gap = 0

    # Scan the boolean array to find gaps between visited minutes.
    for current_minute, is_visited in enumerate(visited):
        if not is_visited:
            continue
        if previous_minute is not None:
            gap = current_minute - previous_minute
            if gap > max_gap:
                max_gap = gap
        previous_minute = current_minute

    return max_gap