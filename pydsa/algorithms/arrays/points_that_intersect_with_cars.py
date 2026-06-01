METADATA = {
    "id": 2848,
    "name": "Points That Intersect With Cars",
    "slug": "points-that-intersect-with-cars",
    "category": "Array",
    "aliases": [],
    "tags": ["difference_array", "sweep-line", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n + max_coord)",
    "space_complexity": "O(max_coord)",
    "description": "Count how many points in a given list intersect with at least one car range.",
}

def solve(cars: list[list[int]], points: list[int]) -> int:
    """
    Counts the number of points that fall within the range of at least one car.

    Args:
        cars: A list of lists where each sub-list [start, end] represents 
              the range covered by a car.
        points: A list of integers representing the points to check.

    Returns:
        The count of points that intersect with at least one car.

    Examples:
        >>> solve([[1, 4], [5, 8]], [1, 2, 5, 10])
        3
        >>> solve([[1, 2], [2, 3]], [2])
        1
    """
    if not cars or not points:
        return 0

    # Find the maximum coordinate to define the size of our difference array.
    # The problem constraints usually imply a reasonable upper bound.
    max_coord = 0
    for start, end in cars:
        if end > max_coord:
            max_coord = end
    
    # We use a difference array to mark the intervals.
    # diff[i] stores the change in the number of cars covering coordinate i.
    # Size is max_coord + 2 to handle end + 1 safely.
    diff = [0] * (max_coord + 2)

    for start, end in cars:
        diff[start] += 1
        diff[end + 1] -= 1

    # Transform the difference array into a prefix sum array.
    # is_covered[i] will be > 0 if coordinate i is covered by at least one car.
    is_covered = [0] * (max_coord + 1)
    current_coverage = 0
    for i in range(max_coord + 1):
        current_coverage += diff[i]
        if current_coverage > 0:
            is_covered[i] = 1
        else:
            is_covered[i] = 0

    # Count how many points are marked as covered.
    intersecting_count = 0
    for point in points:
        # Check if the point is within the bounds of our coverage array.
        if 0 <= point <= max_coord:
            if is_covered[point] == 1:
                intersecting_count += 1

    return intersecting_count
