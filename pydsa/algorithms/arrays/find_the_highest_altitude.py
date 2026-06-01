METADATA = {
    "id": 1732,
    "name": "Find the Highest Altitude",
    "slug": "find_the_highest_altitude",
    "category": "array",
    "aliases": [],
    "tags": ["arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the highest altitude reached after applying the given gains.",
}


def solve(gain: list[int]) -> int:
    """Calculate the maximum altitude reached.

    Args:
        gain: A list of integers where gain[i] is the net change in altitude
              between point i and point i + 1.

    Returns:
        The highest altitude achieved starting from altitude 0.

    Examples:
        >>> solve([1, -3, 4])
        4
        >>> solve([-4, -3, -2, -1, 4, 3, 2])
        0
    """
    current_altitude = 0
    max_altitude = 0

    for change in gain:
        current_altitude += change          # update altitude after this segment
        if current_altitude > max_altitude:
            max_altitude = current_altitude  # track the highest altitude seen

    return max_altitude