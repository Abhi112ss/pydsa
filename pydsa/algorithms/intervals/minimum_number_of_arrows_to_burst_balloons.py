METADATA = {
    "id": 452,
    "name": "Minimum Number of Arrows to Burst Balloons",
    "slug": "minimum-number-of-arrows-to-burst-balloons",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting", "intervals"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of arrows required to burst all balloons given their start and end coordinates.",
}

def solve(points: list[list[int]]) -> int:
    """
    Calculates the minimum number of arrows needed to burst all balloons.

    The algorithm uses a greedy approach: sort the balloons by their end coordinates.
    By placing an arrow at the end of the current balloon, we maximize the chance
    of hitting subsequent balloons that overlap with this end point.

    Args:
        points: A list of lists where each sub-list contains [start, end] coordinates.

    Returns:
        The minimum number of arrows required.

    Examples:
        >>> solve([[10,16],[2,8],[1,6],[7,12]])
        2
        >>> solve([[1,2],[3,4],[5,6],[7,8]])
        4
    """
    if not points:
        return 0

    # Sort balloons based on their end coordinates to facilitate greedy selection
    points.sort(key=lambda x: x[1])

    arrows_count = 1
    # Place the first arrow at the end of the first balloon
    current_arrow_position = points[0][1]

    for i in range(1, len(points)):
        start, end = points[i]

        # If the current balloon starts after the last arrow position,
        # it cannot be burst by the existing arrow.
        if start > current_arrow_position:
            arrows_count += 1
            # Place a new arrow at the end of this new balloon
            current_arrow_position = end

    return arrows_count
