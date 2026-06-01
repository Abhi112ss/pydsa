METADATA = {
    "id": 2446,
    "name": "Determine if Two Events Have Conflict",
    "slug": "determine_if_two_events_have_conflict",
    "category": "array",
    "aliases": [],
    "tags": ["arrays"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Check whether two time intervals overlap.",
}


def solve(event1: list[int], event2: list[int]) -> bool:
    """Determine if two events have a conflict.

    Args:
        event1: A list of two integers [start1, end1] representing the first event.
        event2: A list of two integers [start2, end2] representing the second event.

    Returns:
        True if the events overlap (i.e., there exists a time point that belongs to both
        intervals), otherwise False.

    Examples:
        >>> solve([1, 5], [5, 10])
        True
        >>> solve([1, 2], [3, 4])
        False
    """
    start1, end1 = event1
    start2, end2 = event2

    # The intervals overlap if the later start is not after the earlier end.
    latest_start = max(start1, start2)
    earliest_end = min(end1, end2)

    return latest_start <= earliest_end