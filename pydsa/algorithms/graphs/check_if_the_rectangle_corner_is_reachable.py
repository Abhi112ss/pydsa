METADATA = {
    "id": 3235,
    "name": "Check if the Rectangle Corner Is Reachable",
    "slug": "check-if-the-rectangle-corner-is-reachable",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "bfs", "dfs", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Determine if a path exists from the top-left corner to the bottom-right corner of a grid where certain cells are blocked.",
}

def solve(grid: list[list[int]]) -> bool:
    """
    Determines if there is a path from the top-left corner (0, 0) to the 
    bottom-right corner (m-1, n-1) in a grid where 0 represents an empty 
    cell and 1 represents an obstacle.

    Args:
        grid: A 2D list of integers representing the grid.

    Returns:
        True if a path exists, False otherwise.

    Examples:
        >>> solve([[0, 0], [0, 0]])
        True
        >>> solve([[0, 1], [1, 0]])
        False
    """
    if not grid or not grid[0]:
        return False

    rows = len(grid)
    cols = len(grid[0])

    # If start or end is blocked, no path is possible
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return False

    # Using a deque for BFS to find the shortest path/reachability
    from collections import deque
    queue = deque([(0, 0)])
    
    # Use a set or modify grid to track visited cells to avoid cycles
    visited = set([(0, 0)])

    # Directions for moving: Up, Down, Left, Right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        current_row, current_col = queue.popleft()

        # Check if we reached the target corner
        if current_row == rows - 1 and current_col == cols - 1:
            return True

        for dr, dc in directions:
            next_row, next_col = current_row + dr, current_col + dc

            # Validate bounds, check if cell is not an obstacle, and not visited
            if (0 <= next_row < rows and 
                0 <= next_col < cols and 
                grid[next_row][next_col] == 0 and 
                (next_row, next_col) not in visited):
                
                visited.add((next_row, next_col))
                queue.append((next_row, next_col))

    return False
