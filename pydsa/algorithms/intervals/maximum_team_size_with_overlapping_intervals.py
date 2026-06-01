METADATA = {
    "id": 3893,
    "name": "Maximum Team Size with Overlapping Intervals",
    "slug": "maximum-team-size-with-overlapping-intervals",
    "category": "Intervals",
    "aliases": [],
    "tags": ["intervals", "sweep_line", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of overlapping intervals at any single point in time.",
}

def solve(intervals: list[list[int]]) -> int:
    """
    Calculates the maximum number of overlapping intervals using a sweep-line algorithm.

    Args:
        intervals: A list of intervals where each interval is represented as [start, end].

    Returns:
        The maximum number of intervals that overlap at any given point.

    Examples:
        >>> solve([[1, 5], [2, 3], [4, 6], [5, 8]])
        2
        >>> solve([[1, 10], [2, 3], [4, 5], [6, 7]])
        2
        >>> solve([[1, 2], [2, 3], [3, 4]])
        2
    """
    if not intervals:
        return 0

    # Create events: +1 for a start point, -1 for an end point.
    # Note: If an interval is [start, end], and they are considered overlapping 
    # at the boundary (e.g., [1, 2] and [2, 3] overlap at 2), 
    # we must process 'start' events before 'end' events for the same coordinate.
    # However, standard interval overlap problems usually define overlap 
    # as [start, end]. If the problem implies [start, end) (half-open), 
    # we process 'end' before 'start'. 
    # Given the prompt context, we assume standard closed interval overlap.
    
    events = []
    for start, end in intervals:
        # Use 0 for start and 1 for end to ensure that for the same coordinate,
        # the start event is processed first if we want to count the boundary.
        # If the problem implies [start, end) (half-open), we would swap these.
        # Most "maximum overlap" problems treat [1, 2] and [2, 3] as overlapping at 2.
        events.append((start, -1))  # -1 ensures start comes before end in sort if using (coord, type)
        events.append((end, 1))

    # Sort events by coordinate. 
    # If coordinates are equal, the type (-1 for start, 1 for end) 
    # ensures we process starts before ends to capture the maximum overlap at that point.
    events.sort()

    max_overlap = 0
    current_overlap = 0

    for _, event_type in events:
        if event_type == -1:
            # A new interval has started
            current_overlap += 1
        else:
            # An interval has ended
            current_overlap -= 1
        
        # Update the global maximum encountered so far
        if current_overlap > max_overlap:
            max_overlap = current_overlap

    return max_overlap
