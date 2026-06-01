METADATA = {
    "id": 1604,
    "name": "Alert Using Same Key-Card Three or More Times in a One Hour Period",
    "slug": "alert_using_same_key_card_three_or_more_times_in_a_one_hour_period",
    "category": "hash_table",
    "aliases": [],
    "tags": ["sorting", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Return the list of names that used a key card three or more times within any one‑hour window.",
}


def solve(key_name: list[str], key_time: list[str]) -> list[str]:
    """Detect employees who used their key card three or more times within a one‑hour period.

    Args:
        key_name: List of employee names corresponding to each key‑card swipe.
        key_time: List of timestamps in "HH:MM" 24‑hour format matching `key_name`.

    Returns:
        A sorted list of unique employee names that triggered the alert.

    Examples:
        >>> solve(["daniel","daniel","daniel","luis","luis","luis"], ["10:00","10:40","11:00","09:00","09:20","09:50"])
        ['daniel', 'luis']
        >>> solve(["alice","alice","alice"], ["23:58","23:59","00:01"])
        ['alice']
    """
    # Convert each timestamp to minutes since midnight for easy arithmetic.
    def time_to_minutes(timestamp: str) -> int:
        hour_str, minute_str = timestamp.split(":")
        return int(hour_str) * 60 + int(minute_str)

    # Aggregate minutes per employee.
    employee_minutes: dict[str, list[int]] = {}
    for name, timestamp in zip(key_name, key_time):
        minutes = time_to_minutes(timestamp)
        employee_minutes.setdefault(name, []).append(minutes)

    alert_names: list[str] = []

    for name, minutes_list in employee_minutes.items():
        # Sort the swipe times to enable sliding‑window checks.
        minutes_list.sort()
        # Sliding window of size three: check if any three consecutive swipes fall within 60 minutes.
        for start_index in range(len(minutes_list) - 2):
            if minutes_list[start_index + 2] - minutes_list[start_index] <= 60:
                alert_names.append(name)
                break  # No need to check further windows for this employee.

    # Return names in lexicographical order as required by the problem.
    alert_names.sort()
    return alert_names