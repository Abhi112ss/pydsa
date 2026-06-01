METADATA = {
    "id": 1288,
    "name": "Remove Covered Intervals",
    "slug": "remove_covered_intervals",
    "category": "Intervals",
    "aliases": [],
    "tags": ["sorting", "intervals"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Count the number of intervals that are not covered by another interval.",
}

def solve(intervals: list[list[int]]) -> int:
    """
    Counts the number of intervals that are not covered by any other interval.
    
    An interval [a, b] is covered by [c, d] if c <= a and b <= d.
    
    Args:
        intervals: A list of intervals where each interval is [start, end].
        
    Returns:
        The count of intervals that are not covered by another interval.
        
    Examples:
        >>> solve([[1,4], [3,6], [2,8]])
        1
        >>> solve([[1,4], [2,3]])
        1
    """
    if not intervals:
        return 0

    # Sort intervals:
    # 1. Primary key: start time ascending.
    # 2. Secondary key: end time descending.
    # This ensures that if two intervals have the same start, the longer one 
    # comes first, potentially covering the shorter one.
    intervals.sort(key=lambda x: (x[0], -x[1]))

    count = 0
    current_max_end = -1

    for _, end in intervals:
        # Because we sorted by start time ascending, we know the current 
        # interval's start is >= the previous interval's start.
        # Therefore, the current interval is covered if its end is <= 
        # the maximum end seen so far.
        if end > current_max_end:
            # This interval is NOT covered by any previous interval.
            count += 1
            current_max_end = end
        # Else: the current interval is covered because its end is <= current_max_end
        # and its start is >= the start of the interval that provided current_max_end.

    return count
