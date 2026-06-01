METADATA = {
    "id": 252,
    "name": "Meeting Rooms",
    "slug": "meeting_rooms",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "intervals"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Given an array of meeting time intervals, determine if a person could attend all meetings.",
}

def solve(intervals: list[list[int]]) -> bool:
    """Determine if a person can attend all meetings without overlap.

    Args:
        intervals: A list of [start, end] pairs representing meeting times.

    Returns:
        True if no two meetings overlap, False otherwise.

    Examples:
        >>> solve([[0, 30], [5, 10], [15, 20]])
        False
        >>> solve([[7, 10], [2, 4]])
        True
        >>> solve([])
        True
        >>> solve([[1, 5]])
        True
    """
    # Sort intervals by start time so we can check adjacent pairs
    intervals.sort(key=lambda interval: interval[0])

    # Check each consecutive pair: if a meeting starts before the previous ends, there's overlap
    for index in range(1, len(intervals)):
        current_start = intervals[index][0]
        previous_end = intervals[index - 1][1]
        if current_start < previous_end:
            return False

    return True