METADATA = {
    "id": 335,
    "name": "Self Crossing",
    "slug": "self-crossing",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "geometry"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a spiral path of line segments crosses itself.",
}

def solve(distance: list[int]) -> bool:
    """
    Determines if the path described by the distance array crosses itself.

    The path is formed by moving in a spiral pattern (North, West, South, East, ...).
    A crossing can occur in three distinct geometric scenarios relative to the 
    current segment and segments drawn previously.

    Args:
        distance: A list of integers representing the length of each segment.

    Returns:
        True if the path crosses itself, False otherwise.

    Examples:
        >>> solve([2, 1, 1, 2])
        True
        >>> solve([8, 3, 1, 1, 1, 10])
        True
        >>> solve([1, 1, 1, 1])
        False
    """
    n = len(distance)
    if n <= 3:
        return False

    for i in range(3, n):
        # Case 1: Fourth segment crosses the first segment (Standard spiral inward/outward)
        # This happens if the current segment is >= the segment 2 steps back 
        # and the segment 1 step back is <= the segment 3 steps back.
        if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
            return True

        # Case 2: Fifth segment crosses the first segment (The "tightening" spiral)
        # This occurs when the spiral starts expanding or contracting in a way 
        # that the 5th segment meets the 1st segment.
        if (i >= 4 and 
            distance[i - 1] == distance[i - 3] and 
            distance[i] + distance[i - 4] >= distance[i - 2]):
            return True

        # Case 3: Sixth segment crosses the first segment (The "overlap" case)
        # This is the most complex case where the 6th segment intersects the 1st 
        # due to a specific alignment of the 2nd, 3rd, 4th, and 5th segments.
        if (i >= 5 and 
            distance[i - 2] >= distance[i - 4] and 
            distance[i - 3] >= distance[i - 1] and 
            distance[i] + distance[i - 4] >= distance[i - 2] and 
            distance[i - 1] + distance[i - 5] >= distance[i - 3]):
            return True

    return False
