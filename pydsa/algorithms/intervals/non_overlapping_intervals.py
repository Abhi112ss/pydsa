METADATA = {
    "id": 435,
    "name": "Non-overlapping Intervals",
    "slug": "non-overlapping-intervals",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of intervals to remove to make the rest of the intervals non-overlapping.",
}

def solve(intervals: list[list[int]]) -> int:
    """
    Calculates the minimum number of intervals to remove to make the rest non-overlapping.

    The strategy is to use a greedy approach: always pick the interval that ends 
    the earliest. This leaves the maximum possible room for subsequent intervals.

    Args:
        intervals: A list of intervals where intervals[i] = [start_i, end_i].

    Returns:
        The minimum number of intervals to remove.

    Examples:
        >>> solve([[1, 2], [2, 3], [3, 4], [1, 3]])
        1
        >>> solve([[1, 2], [1, 2], [1, 2]])
        2
    """
    if not intervals:
        return 0

    # Sort intervals by their end times. 
    # This is the core of the greedy strategy.
    intervals.sort(key=lambda x: x[1])

    remove_count = 0
    # Keep track of the end time of the last interval added to the non-overlapping set
    last_end_time = intervals[0][1]

    for i in range(1, len(intervals)):
        current_start = intervals[i][0]
        current_end = intervals[i][1]

        if current_start < last_end_time:
            # If the current interval starts before the previous one ends, 
            # they overlap. We must remove one. 
            # Greedily, we "remove" the one that ends later (which is the current one
            # because we sorted by end times).
            remove_count += 1
        else:
            # No overlap: update the last_end_time to the current interval's end
            last_end_time = current_end

    return remove_count
