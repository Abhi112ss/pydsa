METADATA = {
    "id": 3124,
    "name": "Find Longest Calls",
    "slug": "find-longest-calls",
    "category": "Greedy",
    "aliases": [],
    "tags": ["sorting", "greedy", "intervals"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of non-overlapping intervals that can be selected from a given set.",
}

def solve(intervals: list[list[int]]) -> int:
    """
    Finds the maximum number of non-overlapping intervals using a greedy approach.

    The strategy is to always pick the interval that ends the earliest. This 
    leaves the maximum possible room for subsequent intervals.

    Args:
        intervals: A list of intervals where each interval is [start, end].

    Returns:
        The maximum number of non-overlapping intervals.

    Examples:
        >>> solve([[1, 2], [2, 3], [3, 4]])
        3
        >>> solve([[1, 5], [2, 3], [3, 4]])
        2
    """
    if not intervals:
        return 0

    # Sort intervals based on their end times.
    # This is the core of the greedy strategy: finishing as early as possible
    # maximizes the remaining time available for other intervals.
    sorted_intervals = sorted(intervals, key=lambda x: x[1])

    count = 0
    last_end_time = float('-inf')

    for start, end in sorted_intervals:
        # If the current interval starts after or at the moment the last 
        # selected interval ended, we can include it.
        if start >= last_end_time:
            count += 1
            last_end_time = end

    return count
