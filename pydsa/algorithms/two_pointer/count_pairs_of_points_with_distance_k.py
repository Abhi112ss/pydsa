METADATA = {
    "id": 2857,
    "name": "Count Pairs of Points With Distance k",
    "slug": "count-pairs-of-points-with-distance-k",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "sorting", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Count the number of pairs of points whose Euclidean distance is less than or equal to k.",
}

def solve(points: list[list[int]], k: int) -> int:
    """
    Counts the number of pairs of points (i, j) such that the Euclidean distance 
    between points[i] and points[j] is less than or equal to k.

    Args:
        points: A list of points where each point is represented as [x, y].
        k: The maximum allowed Euclidean distance.

    Returns:
        The total count of pairs satisfying the distance condition.

    Examples:
        >>> solve([[1, 1], [2, 2], [3, 3]], 2)
        2
        >>> solve([[0, 0], [1, 1], [10, 10]], 1)
        0
    """
    # Sort points primarily by x-coordinate to allow a sliding window/two-pointer approach
    # If x is same, sorting by y doesn't strictly matter for the distance logic, 
    # but it provides a deterministic order.
    points.sort()
    
    n = len(points)
    count = 0
    k_squared = k * k
    
    for i in range(n):
        x1, y1 = points[i]
        # We only need to check points j > i because the distance is symmetric
        for j in range(i + 1, n):
            x2, y2 = points[j]
            
            # Since points are sorted by x, if the horizontal distance exceeds k,
            # no subsequent points in the sorted list can satisfy the condition.
            dx = x2 - x1
            if dx > k:
                break
            
            # Calculate squared Euclidean distance to avoid expensive sqrt() calls
            dy = y2 - y1
            dist_squared = dx * dx + dy * dy
            
            if dist_squared <= k_squared:
                count += 1
                
    return count
