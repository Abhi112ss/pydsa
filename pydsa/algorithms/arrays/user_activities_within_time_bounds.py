METADATA = {
    "id": 3060,
    "name": "User Activities within Time Bounds",
    "slug": "user_activities_within_time_bounds",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "sorting", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count the number of user activities that fall within a specific time interval [start, end].",
}

from bisect import bisect_left, bisect_right

def solve(activities: list[int], start_time: int, end_time: int) -> int:
    """
    Calculates the number of activities that occur within the inclusive range [start_time, end_time].

    Args:
        activities: A list of integers representing timestamps of user activities.
        start_time: The beginning of the time interval (inclusive).
        end_time: The end of the time interval (inclusive).

    Returns:
        The count of activities that fall within the specified time bounds.

    Examples:
        >>> solve([1, 5, 10, 15, 20], 5, 15)
        3
        >>> solve([1, 2, 3], 4, 6)
        0
        >>> solve([10, 20, 30], 5, 35)
        3
    """
    if not activities:
        return 0

    # Sort the activities to enable efficient range searching via binary search
    sorted_activities = sorted(activities)

    # Find the first index where the activity timestamp is >= start_time
    # bisect_left returns the leftmost insertion point to maintain order
    left_index = bisect_left(sorted_activities, start_time)

    # Find the first index where the activity timestamp is > end_time
    # bisect_right returns the rightmost insertion point to maintain order
    right_index = bisect_right(sorted_activities, end_time)

    # The number of elements in the range [start_time, end_time] is the difference
    # between the two indices found.
    return right_index - left_index
