METADATA = {
    "id": 3279,
    "name": "Maximum Total Area Occupied by Pistons",
    "slug": "maximum-total-area-occupied-by-pistons",
    "category": "Intervals",
    "aliases": [],
    "tags": ["intervals", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the total length covered by the union of a set of intervals.",
}

def solve(intervals: list[list[int]]) -> int:
    """
    Calculates the total area (length) occupied by the union of given intervals.

    Args:
        intervals: A list of intervals where each interval is represented as [start, end].

    Returns:
        The total length covered by the union of all intervals.

    Examples:
        >>> solve([[1, 4], [3, 6], [8, 10]])
        7
        >>> solve([[1, 2], [2, 3], [3, 4]])
        3
        >>> solve([[1, 10], [2, 5], [6, 7]])
        9
    """
    if not intervals:
        return 0

    # Sort intervals by their start time to allow linear merging
    intervals.sort(key=lambda x: x[0])

    total_area = 0
    # Initialize the current merging interval with the first interval
    current_start = intervals[0][0]
    current_end = intervals[0][1]

    for i in range(1, len(intervals)):
        next_start, next_end = intervals[i]

        if next_start < current_end:
            # If the next interval overlaps or touches, extend the current end
            current_end = max(current_end, next_end)
        else:
            # If there is a gap, add the length of the completed interval to total
            total_area += (current_end - current_start)
            # Start a new interval tracking
            current_start = next_start
            current_end = next_end

    # Add the final tracked interval to the total area
    total_area += (current_end - current_start)

    return total_area
