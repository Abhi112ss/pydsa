METADATA = {
    "id": 2494,
    "name": "Merge Overlapping Events in the Same Hall",
    "slug": "merge-overlapping-events-in-the-same-hall",
    "category": "Intervals",
    "aliases": [],
    "tags": ["intervals", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Merge overlapping intervals into a single continuous interval representing the total time span.",
}

def solve(events: list[list[int]]) -> list[list[int]]:
    """
    Merges overlapping intervals into a list of disjoint intervals.

    Args:
        events: A list of intervals where each interval is [start, end].

    Returns:
        A list of merged intervals sorted by their start times.

    Examples:
        >>> solve([[1, 3], [2, 6], [8, 10], [15, 18]])
        [[1, 6], [8, 10], [15, 18]]
        >>> solve([[1, 4], [4, 5]])
        [[1, 5]]
    """
    if not events:
        return []

    # Sort intervals based on the start time to ensure we process them chronologically
    events.sort(key=lambda x: x[0])

    merged_intervals: list[list[int]] = []
    
    # Initialize with the first interval
    current_start, current_end = events[0]

    for i in range(1, len(events)):
        next_start, next_end = events[i]

        # If the next interval starts before or exactly when the current one ends, they overlap
        if next_start <= current_end:
            # Extend the current interval to the maximum end time seen so far
            current_end = max(current_end, next_end)
        else:
            # No overlap: push the completed interval and move to the next one
            merged_intervals.append([current_start, current_end])
            current_start, current_end = next_start, next_end

    # Append the last interval processed
    merged_intervals.append([current_start, current_end])

    return merged_intervals
