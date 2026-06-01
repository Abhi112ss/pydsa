METADATA = {
    "id": 1391,
    "name": "Check if There is a Valid Path in a Grid",
    "slug": "check-if-there-is-a-valid-path-in-a-grid",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "dfs", "union_find", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Determine if there is a valid path from the top-left cell to the bottom-right cell in a grid of connected pipes.",
}

def solve(grid: list[list[int]]) -> bool:
    """
    Determines if a valid path exists from (0, 0) to (rows-1, cols-1) using BFS.

    Args:
        grid: A 2D list of integers representing pipe types.
            1: vertical, 2: horizontal, 3: L-shape (top-left), 
            4: L-shape (top-right), 5: L-shape (bottom-left), 6: L-shape (bottom-right).

    Returns:
        True if a valid path exists, False otherwise.

    Examples:
        >>> solve([[1,1],[1,1]])
        True
        >>> solve([[1,1],[3,1]])
        False
    """
    rows = len(grid)
    cols = len(grid[0])

    # Mapping pipe types to the directions they can connect to:
    # Directions: 0: Up, 1: Down, 2: Left, 3: Right
    # pipe_connections[type] = set of directions the pipe allows
    pipe_connections = {
        1: {0, 1},             # Vertical: Up, Down
        2: {2, 3},             # Horizontal: Left, Right
        3: {1, 3},             # L-shape (top-left): Down, Right
        4: {1, 2},             # L-shape (top-right): Down, Left
        5: {0, 3},             # L-shape (bottom-left): Up, Right
        6: {0, 2}              # L-shape (bottom-right): Up, Left
    }

    # Mapping directions to coordinate offsets (row_offset, col_offset)
    # and their corresponding "opposite" direction index
    # 0: Up (-1, 0), 1: Down (1, 0), 2: Left (0, -1), 3: Right (0, 1)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    opposite_direction = {0: 1, 1: 0, 2: 3, 3: 2}

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = [(0, 0)]
    visited[0][0] = True

    while queue:
        curr_r, curr_c = queue.pop(0)

        if curr_r == rows - 1 and curr_c == cols - 1:
            return True

        current_pipe_type = grid[curr_r][curr_c]
        allowed_dirs = pipe_connections[current_pipe_type]

        for direction_idx in allowed_dirs:
            dr, dc = directions[direction_idx]
            next_r, next_c = curr_r + dr, curr_c + dc

            # Check boundaries and if already visited
            if 0 <= next_r < rows and 0 <= next_c < cols and not visited[next_r][next_c]:
                next_pipe_type = grid[next_r][next_c]
                
                # Key logic: The neighbor must allow a connection back to the current cell
                # via the opposite direction of the movement we just made.
                required_dir_from_neighbor = opposite_direction[direction_idx]
                
                if required_dir_from_neighbor in pipe_connections[next_pipe_type]:
                    visited[next_r][next_c] = True
                    queue.append((next_r, next_c))

    return False
