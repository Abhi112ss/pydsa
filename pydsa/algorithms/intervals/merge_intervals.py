METADATA = {
    "id": 56,
    "name": "Merge Intervals",
    "slug": "merge-intervals",
    "category": "Arrays",
    "aliases": [],
    "tags": ["sorting", "array", "intervals"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Given an array of intervals, merge all overlapping intervals.",
}

def solve(intervals: list[list[int]]) -> list[list[int]]:
    """
    Merges all overlapping intervals in a given list.

    Args:
        intervals: A list of lists, where each inner list represents an interval [start, end].

    Returns:
        A list of merged intervals where no two intervals overlap.

    Examples:
        >>> solve([[1, 3], [2, 6], [8, 10], [15, 18]])
        [[1, 6], [8, 10], [15, 18]]
        >>> solve([[1, 4], [4, 5]])
        [[1, 5]]
    """
    if not intervals:
        return []

    # Sort intervals based on the start time to ensure we only need 
    # to compare the current interval with the last merged one.
    intervals.sort(key=lambda x: x[0])

    merged_intervals: list[list[int]] = []

    for current_interval in intervals:
        # If the list of merged intervals is empty or the current interval 
        # does not overlap with the previous one, append it.
        if not merged_intervals or merged_intervals[-1][1] < current_interval[0]:
            merged_intervals.append(current_interval)
        else:
            # There is an overlap, so merge the current interval with the 
            # previous one by updating the end time to the maximum end time.
            merged_intervals[-1][1] = max(merged_intervals[-1][1], current_interval[1])

    return merged_intervals
