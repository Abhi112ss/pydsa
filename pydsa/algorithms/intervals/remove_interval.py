METADATA = {
    "id": 1272,
    "name": "Remove Interval",
    "slug": "remove-interval",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given a list of non-overlapping intervals, remove a given interval and return the remaining intervals.",
}

def solve(intervals: list[list[int]], remove_interval: list[int]) -> list[list[int]]:
    """
    Removes a specific interval from a list of non-overlapping intervals.

    The algorithm iterates through each interval and determines how it interacts
    with the removal range. An interval can be completely removed, partially 
    trimmed, or split into two separate intervals.

    Args:
        intervals: A list of non-overlapping intervals [start, end].
        remove_interval: The interval [start, end] to be removed.

    Returns:
        A list of remaining non-overlapping intervals.

    Examples:
        >>> solve([[0, 2], [5, 10], [12, 15]], [4, 10])
        [[0, 2], [12, 15]]
        >>> solve([[0, 5]], [2, 3])
        [[0, 2], [3, 5]]
    """
    result = []
    remove_start, remove_end = remove_interval

    for start, end in intervals:
        # Case 1: The current interval is completely before the removal range
        if end <= remove_start:
            result.append([start, end])
        
        # Case 2: The current interval is completely after the removal range
        elif start >= remove_end:
            result.append([start, end])
        
        # Case 3: There is an overlap
        else:
            # If there's a part of the interval before the removal range, keep it
            if start < remove_start:
                result.append([start, remove_start])
            
            # If there's a part of the interval after the removal range, keep it
            if end > remove_end:
                result.append([remove_end, end])

    return result
