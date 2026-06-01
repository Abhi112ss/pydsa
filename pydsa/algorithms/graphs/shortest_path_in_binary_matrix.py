METADATA = {
    "id": 1091,
    "name": "Shortest Path in Binary Matrix",
    "slug": "shortest-path-in-binary-matrix",
    "category": "Graphs",
    "aliases": [],
    "tags": ["bfs", "graphs", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(N^2)",
    "space_complexity": "O(N^2)",
    "description": "Find the length of the shortest clear path from the top-left cell to the bottom-right cell in a binary matrix.",
}

from collections import deque

def solve(grid: list[list[int]]) -> int:
    """
    Finds the shortest path in a binary matrix from (0,0) to (n-1, n-1).

    Args:
        grid: A square 2D list of integers where 0 represents an empty cell 
              and 1 represents an obstacle.

    Returns:
        The length of the shortest path if one exists, otherwise -1.

    Examples:
        >>> solve([[0,0,0],[1,1,0],[1,1,0]])
        4
        >>> solve([[0,1],[1,0]])
        -1
    """
    n = len(grid)
    
    # Edge case: start or end is blocked
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1

    # 8 possible directions: horizontal, vertical, and diagonal
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    # Queue stores (row, col, current_path_length)
    queue = deque([(0, 0, 1)])
    
    # Mark the starting cell as visited by modifying the grid in-place
    # or using a separate set. Modifying grid is O(1) extra space.
    grid[0][0] = 1 

    while queue:
        row, col, distance = queue.popleft()

        # If we reached the target cell
        if row == n - 1 and col == n - 1:
            return distance

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check boundaries and if the cell is traversable (0)
            if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0:
                # Mark as visited immediately to prevent redundant queue entries
                grid[new_row][new_col] = 1
                queue.append((new_row, new_col, distance + 1))

    return -1
