METADATA = {
    "id": 3557,
    "name": "Find Maximum Number of Non Intersecting Substrings",
    "slug": "find-maximum-number-of-non-intersecting-substrings",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "interval_scheduling", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of non-overlapping substrings given a set of intervals.",
}

def solve(intervals: list[list[int]]) -> int:
    """
    Finds the maximum number of non-intersecting substrings using the 
    Greedy Interval Scheduling algorithm.

    The optimal strategy for maximizing the number of non-overlapping 
    intervals is to always pick the interval that finishes earliest. 
    This leaves the maximum amount of time available for subsequent intervals.

    Args:
        intervals: A list of lists where each sub-list contains two integers 
                   [start, end] representing the boundaries of a substring.

    Returns:
        The maximum number of non-intersecting substrings.

    Examples:
        >>> solve([[1, 2], [2, 3], [3, 4]])
        3
        >>> solve([[1, 5], [2, 3], [3, 4]])
        2
        >>> solve([[1, 10], [2, 3], [4, 5], [6, 7]])
        3
    """
    if not intervals:
        return 0

    # Sort intervals based on their end positions.
    # This is the core of the greedy approach for interval scheduling.
    sorted_intervals = sorted(intervals, key=lambda x: x[1])

    count = 0
    last_end_time = float('-inf')

    for start, end in sorted_intervals:
        # If the current interval starts after or at the moment the 
        # previous selected interval ended, we can pick it.
        # Note: Depending on problem definition, if [1,2] and [2,3] 
        # are considered intersecting, use 'start > last_end_time'.
        # Standard interval scheduling usually allows start == end.
        if start >= last_end_time:
            count += 1
            last_end_time = end

    return count
