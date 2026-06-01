METADATA = {
    "id": 3009,
    "name": "Maximum Number of Intersections on the Chart",
    "slug": "maximum-number-of-intersections-on-the-chart",
    "category": "Algorithms",
    "aliases": [],
    "tags": ["sorting", "sweep_line"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of overlapping intervals on a 1D chart.",
}

def solve(paths: list[list[int]]) -> int:
    """
    Calculates the maximum number of overlapping intervals using a sweep-line algorithm.

    Args:
        paths: A list of intervals where each interval is represented as [start, end].

    Returns:
        The maximum number of intersections (overlaps) at any point on the chart.

    Examples:
        >>> solve([[1, 5], [2, 6], [3, 7]])
        3
        >>> solve([[1, 2], [2, 3], [3, 4]])
        2
        >>> solve([[1, 10], [2, 3], [4, 5], [6, 7]])
        2
    """
    events = []

    # Create events: +1 for a start point, -1 for an end point.
    # To handle the case where an interval ends at the same point another starts,
    # we must process 'start' events before 'end' events if they share the same coordinate.
    # However, the problem implies intervals are inclusive [start, end].
    # If an interval is [1, 2] and another is [2, 3], they intersect at 2.
    # Therefore, at coordinate 2, we should count the start of the second interval 
    # before we count the end of the first interval to capture the maximum overlap.
    for start, end in paths:
        # Use -1 for start and 1 for end to ensure that when sorting by coordinate,
        # if coordinates are equal, the 'start' event comes first.
        # Wait, if we want to maximize intersections, and [1, 2] and [2, 3] intersect,
        # we want the count to be 2 at point 2.
        # Sorting (coord, type): if type for start is -1 and end is 1, 
        # then at coord 2: (2, -1) comes before (2, 1).
        events.append((start, -1))
        events.append((end, 1))

    # Sort events by coordinate. If coordinates are equal, the -1 (start) 
    # will come before 1 (end) due to the second element in the tuple.
    events.sort()

    max_intersections = 0
    current_intersections = 0

    for _, event_type in events:
        if event_type == -1:
            # It's a start event
            current_intersections += 1
        else:
            # It's an end event
            # We check max before decrementing? No, the start event already 
            # incremented it. If we process all starts at a coordinate 
            # before ends, current_intersections will peak correctly.
            pass
        
        # Update the global maximum
        if current_intersections > max_intersections:
            max_intersections = current_intersections
            
        if event_type == 1:
            # It's an end event, decrement after checking max
            current_intersections -= 1

    return max_intersections

# Refined logic for the loop to be cleaner:
def solve(paths: list[list[int]]) -> int:
    """
    Calculates the maximum number of overlapping intervals using a sweep-line algorithm.

    Args:
        paths: A list of intervals where each interval is represented as [start, end].

    Returns:
        The maximum number of intersections (overlaps) at any point on the chart.
    """
    events = []
    for start, end in paths:
        # We use type -1 for start and type 1 for end.
        # When sorting, for the same coordinate, -1 comes before 1.
        # This ensures that if an interval starts where another ends, 
        # the overlap is counted.
        events.append((start, -1))
        events.append((end, 1))

    # Sort by coordinate primarily, and by type secondarily.
    events.sort()

    max_intersections = 0
    current_intersections = 0

    for _, event_type in events:
        if event_type == -1:
            current_intersections += 1
            # Update max when a new interval starts
            if current_intersections > max_intersections:
                max_intersections = current_intersections
        else:
            # An interval ends. We decrement after checking max 
            # because the intersection is inclusive of the end point.
            current_intersections -= 1

    return max_intersections