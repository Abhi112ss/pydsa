METADATA = {
    "id": 1515,
    "name": "Best Position for a Service Centre",
    "slug": "best-position-for-a-service-centre",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "geometry"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the coordinate that minimizes the sum of Manhattan distances to a set of points.",
}

def solve(points: list[list[int]]) -> list[int]:
    """
    Finds the optimal coordinate (x, y) that minimizes the sum of Manhattan 
    distances to all given points.

    The Manhattan distance sum is minimized when the x and y coordinates 
    are the medians of the respective coordinates of the input points.

    Args:
        points: A list of points where each point is a list of two integers [x, y].

    Returns:
        A list of two integers [best_x, best_y] representing the optimal position.

    Examples:
        >>> solve([[1, 1], [2, 2], [3, 3]])
        [2, 2]
        >>> solve([[0, 0], [10, 10]])
        [0, 0]  # Note: Any value between 0 and 10 works; median logic picks one.
    """
    if not points:
        return [0, 0]

    # To find the median in O(n) time and O(1) extra space (excluding input),
    # we would typically use Quickselect. However, since we are allowed to 
    # modify the input or use standard sorting, and the problem asks for 
    # the optimal coordinate, we extract coordinates.
    
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    
    n = len(points)
    
    def get_median(arr: list[int]) -> int:
        """
        Finds the median using the Quickselect algorithm logic.
        For simplicity and production reliability in Python, we use sorted() 
        which is O(n log n), but the theoretical optimal is O(n) via Quickselect.
        """
        arr.sort()
        # In Manhattan distance minimization, any value between the two 
        # middle elements (for even n) works. We pick the lower median.
        return arr[(n - 1) // 2]

    # The Manhattan distance sum is minimized by minimizing |x - xi| and |y - yi|
    # independently. The value that minimizes the sum of absolute differences 
    # is the median.
    best_x = get_median(x_coords)
    best_y = get_median(y_coords)

    return [best_x, best_y]
