METADATA = {
    "id": 2276,
    "name": "Count Integers in Intervals",
    "slug": "count-integers-in-intervals",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "intervals"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Given a list of intervals, count the total number of unique integers contained within them.",
}

def solve(intervals: list[list[int]], query_left: int, query_right: int) -> int:
    """
    Counts the number of unique integers in the union of given intervals 
    that fall within the range [query_left, query_right].

    Args:
        intervals: A list of intervals where each interval is [start, end].
        query_left: The lower bound of the query range.
        query_right: The upper bound of the query range.

    Returns:
        The count of unique integers in the intersection of the union of 
        intervals and the range [query_left, query_right].

    Examples:
        >>> solve([[1, 4], [4, 10]], 2, 5)
        4
        >>> solve([[1, 2], [3, 4], [5, 6]], 1, 6)
        6
    """
    if not intervals:
        return 0

    # Step 1: Sort intervals by start time to facilitate merging
    intervals.sort(key=lambda x: x[0])

    # Step 2: Merge overlapping intervals
    merged_intervals: list[list[int]] = []
    for current_start, current_end in intervals:
        if not merged_intervals or current_start > merged_intervals[-1][1]:
            # No overlap with the last merged interval
            merged_intervals.append([current_start, current_end])
        else:
            # Overlap exists, extend the end of the last interval
            merged_intervals[-1][1] = max(merged_intervals[-1][1], current_end)

    total_count = 0
    # Step 3: Calculate intersection of merged intervals with [query_left, query_right]
    for start, end in merged_intervals:
        # Find the effective range within the query bounds
        effective_start = max(start, query_left)
        effective_end = min(end, query_right)

        if effective_start <= effective_end:
            # Count integers in the valid intersection
            total_count += (effective_end - effective_start + 1)

    return total_count
