METADATA = {
    "id": 2725,
    "name": "Interval Cancellation",
    "slug": "interval_cancellation",
    "category": "Greedy",
    "aliases": [],
    "tags": ["intervals", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of intervals to remove to make the rest of the intervals non-overlapping.",
}

def solve(intervals: list[list[int]]) -> int:
    """
    Calculates the minimum number of intervals to remove to make the remaining 
    intervals non-overlapping.

    This is a classic interval scheduling problem. To maximize the number of 
    non-overlapping intervals, we should always pick the interval that ends 
    the earliest. This leaves the maximum possible room for subsequent intervals.

    Args:
        intervals: A list of intervals where intervals[i] = [start_i, end_i].

    Returns:
        The minimum number of intervals to remove.

    Examples:
        >>> solve([[1, 2], [2, 3], [3, 4], [1, 3]])
        1
        >>> solve([[1, 2], [1, 2], [3, 4], [3, 4]])
        2
    """
    if not intervals:
        return 0

    # Sort intervals by their end times to apply the greedy strategy.
    # Sorting by end time allows us to always pick the interval that 
    # finishes earliest, leaving more space for others.
    intervals.sort(key=lambda x: x[1])

    count_removed = 0
    # Track the end time of the last interval added to our non-overlapping set.
    last_end_time = intervals[0][1]

    for i in range(1, len(intervals)):
        current_start = intervals[i][0]
        current_end = intervals[i][1]

        # If the current interval starts before the last one ended, they overlap.
        if current_start < last_end_time:
            # We must remove this interval to maintain non-overlapping property.
            count_removed += 1
        else:
            # No overlap: update the end time to the current interval's end.
            last_end_time = current_end

    return count_removed
