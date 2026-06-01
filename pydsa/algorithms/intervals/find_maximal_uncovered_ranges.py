METADATA = {
    "id": 2655,
    "name": "Find Maximal Uncovered Ranges",
    "slug": "find-maximal-uncovered-ranges",
    "category": "Intervals",
    "aliases": [],
    "tags": ["intervals", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest gap between a set of intervals within a given range [left, right].",
}

def solve(left: int, right: int, intervals: list[list[int]]) -> int:
    """
    Finds the length of the maximal uncovered range within [left, right].

    Args:
        left: The start of the target range.
        right: The end of the target range.
        intervals: A list of [start, end] intervals that cover parts of the range.

    Returns:
        The length of the largest gap (uncovered range) within [left, right].

    Examples:
        >>> solve(1, 10, [[2, 3], [5, 8]])
        2
        >>> solve(1, 10, [[1, 5], [6, 10]])
        0
        >>> solve(1, 10, [[1, 10]])
        0
    """
    # Sort intervals by start time to process them linearly
    intervals.sort()

    max_gap = 0
    current_pos = left

    for start, end in intervals:
        # If the interval starts after our current position, there is a gap
        if start > current_pos:
            # The gap is the distance between current_pos and the start of this interval
            # We must ensure we don't count gaps beyond the 'right' boundary
            gap_end = min(start, right + 1)
            if gap_end > current_pos:
                max_gap = max(max_gap, gap_end - current_pos)
        
        # Update current_pos to the end of the current interval, 
        # but only if it actually extends our coverage.
        # We also clip it to the 'right' boundary.
        if end >= current_pos:
            current_pos = max(current_pos, end + 1)
        
        # If we have already covered up to or past 'right', we can stop
        if current_pos > right:
            break

    # After checking all intervals, check if there is a gap between 
    # the last interval's end and the 'right' boundary.
    if current_pos <= right:
        max_gap = max(max_gap, right - current_pos + 1)

    return max_gap
