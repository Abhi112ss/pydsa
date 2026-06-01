METADATA = {
    "id": 3648,
    "name": "Minimum Sensors to Cover Grid",
    "slug": "minimum-sensors-to-cover-grid",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "set_cover", "grid"],
    "difficulty": "medium",
    "time_complexity": "O(N * M)",
    "space_complexity": "O(N * M)",
    "description": "Find the minimum number of sensors required to cover all target cells in a grid given a specific sensor range.",
}

def solve(grid: list[list[int]], sensor_range: int) -> int:
    """
    Calculates the minimum number of sensors needed to cover all target cells (1s) 
    in a grid. Each sensor covers a square area of (2 * sensor_range + 1) centered at its position.

    Note: This implementation assumes a greedy approach for a standard square-coverage 
    problem which is optimal for specific grid-based coverage patterns.

    Args:
        grid: A 2D list of integers where 1 represents a target cell and 0 represents empty.
        sensor_range: The radius of the sensor coverage.

    Returns:
        The minimum number of sensors required to cover all 1s.

    Examples:
        >>> solve([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1)
        1
        >>> solve([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 0)
        4
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    
    # Track which cells are already covered
    covered = [[False for _ in range(cols)] for _ in range(rows)]
    sensor_count = 0

    # Iterate through the grid to find uncovered target cells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not covered[r][c]:
                # When an uncovered cell is found, we place a sensor.
                # To maximize coverage greedily, we place the sensor such that 
                # the current cell is at the top-left corner of the sensor's range.
                # This is a standard greedy heuristic for covering points with squares.
                sensor_count += 1
                
                # Calculate the center of the sensor that covers this cell at its top-left
                # The sensor covers [r - sensor_range, r + sensor_range] and [c - sensor_range, c + sensor_range]
                # However, to cover (r, c) optimally, we place the sensor center at (r + sensor_range, c + sensor_range)
                center_r = min(r + sensor_range, rows - 1)
                center_c = min(c + sensor_range, cols - 1)
                
                # Define the boundaries of the sensor's coverage
                start_r = max(0, center_r - sensor_range)
                end_r = min(rows - 1, center_r + sensor_range)
                start_c = max(0, center_c - sensor_range)
                end_c = min(cols - 1, center_c + sensor_range)
                
                # Mark all cells within the sensor's range as covered
                for i in range(start_r, end_r + 1):
                    for j in range(start_c, end_c + 1):
                        if grid[i][j] == 1:
                            covered[i][j] = True
                            
    return sensor_count
