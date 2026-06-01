METADATA = {
    "id": 1459,
    "name": "Rectangles Area",
    "slug": "rectangles_area",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "geometry"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Calculate the total area covered by a set of rectangles, accounting for overlaps.",
}

def solve(rectangles: list[list[int]]) -> int:
    """
    Calculates the total area covered by a set of rectangles.
    
    The algorithm uses a coordinate compression / sweep-line style approach 
    by collecting all unique x and y coordinates to create a grid of 
    non-overlapping elementary rectangles.

    Args:
        rectangles: A list of rectangles where each rectangle is [x1, y1, x2, y2].

    Returns:
        The total area covered by the union of all rectangles.

    Examples:
        >>> solve([[0,0,2,2], [1,1,3,3]])
        7
        >>> solve([[0,0,1,1], [2,2,3,3]])
        2
    """
    if not rectangles:
        return 0

    # Collect all unique x and y coordinates to define the grid boundaries
    x_coords = set()
    y_coords = set()
    for x1, y1, x2, y2 in rectangles:
        x_coords.add(x1)
        x_coords.add(x2)
        y_coords.add(y1)
        y_coords.add(y2)

    # Sort coordinates to create discrete intervals
    sorted_x = sorted(list(x_coords))
    sorted_y = sorted(list(y_coords))

    # Map coordinate values to their index in the sorted list for fast lookup
    x_map = {val: i for i, val in enumerate(sorted_x)}
    y_map = {val: i for i, val in enumerate(sorted_y)}

    # Create a grid to track which elementary rectangles are covered
    # grid[i][j] represents the rectangle between sorted_x[i], sorted_x[i+1] 
    # and sorted_y[j], sorted_y[j+1]
    num_x = len(sorted_x)
    num_y = len(sorted_y)
    grid = [[False for _ in range(num_y - 1)] for _ in range(num_x - 1)]

    # Mark all elementary rectangles covered by the input rectangles
    for x1, y1, x2, y2 in rectangles:
        start_x_idx = x_map[x1]
        end_x_idx = x_map[x2]
        start_y_idx = y_map[y1]
        end_y_idx = y_map[y2]

        for i in range(start_x_idx, end_x_idx):
            for j in range(start_y_idx, end_y_idx):
                grid[i][j] = True

    # Sum the area of all marked elementary rectangles
    total_area = 0
    for i in range(num_x - 1):
        width = sorted_x[i + 1] - sorted_x[i]
        for j in range(num_y - 1):
            if grid[i][j]:
                height = sorted_y[j + 1] - sorted_y[j]
                total_area += width * height

    return total_area
