METADATA = {
    "id": 1210,
    "name": "Minimum Moves to Reach Target with Rotations",
    "slug": "minimum-moves-to-reach-target-with-rotations",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["bfs", "matrix", "simulation"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum number of moves to reach a target position and orientation using horizontal/vertical shifts and 90-degree rotations.",
}

from collections import deque


def solve(grid: list[list[int]], target: list[int]) -> int:
    """
    Finds the minimum moves to reach the target position and orientation.

    The state is defined by (row, col, orientation), where orientation 0 is 
    horizontal and orientation 1 is vertical.

    Args:
        grid: A 2D matrix where 1 represents a valid cell and 0 represents an obstacle.
        target: A list [target_row, target_col, target_orientation].

    Returns:
        The minimum number of moves to reach the target, or -1 if unreachable.

    Examples:
        >>> grid = [[1,1,1],[1,1,1],[1,1,1]]
        >>> target = [2,2,0]
        >>> solve(grid, target)
        4
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # target_row, target_col, target_orientation
    tr, tc, tor = target[0], target[1], target[2]
    
    # Initial state: row 0, col 0, orientation 0 (horizontal)
    # State representation: (r, c, orientation)
    # orientation: 0 for horizontal, 1 for vertical
    start_state = (0, 0, 0)
    
    # queue stores (r, c, orientation, moves)
    queue = deque([(0, 0, 0, 0)])
    
    # visited stores (r, c, orientation) to prevent cycles
    visited = set()
    visited.add(start_state)
    
    while queue:
        r, c, orientation, moves = queue.popleft()
        
        if r == tr and c == tc and orientation == tor:
            return moves
        
        # 1. Try moving in the current orientation
        if orientation == 0:  # Horizontal
            # Move Left
            if c > 0 and grid[r][c - 1] == 1 and (r, c - 1, 0) not in visited:
                visited.add((r, c - 1, 0))
                queue.append((r, c - 1, 0, moves + 1))
            # Move Right
            if c < cols - 1 and grid[r][c + 1] == 1 and (r, c + 1, 0) not in visited:
                visited.add((r, c + 1, 0))
                queue.append((r, c + 1, 0, moves + 1))
        else:  # Vertical
            # Move Up
            if r > 0 and grid[r - 1][c] == 1 and (r - 1, c, 1) not in visited:
                visited.add((r - 1, c, 1))
                queue.append((r - 1, c, 1, moves + 1))
            # Move Down
            if r < rows - 1 and grid[r + 1][c] == 1 and (r + 1, c, 1) not in visited:
                visited.add((r + 1, c, 1))
                queue.append((r + 1, c, 1, moves + 1))
                
        # 2. Try rotating 90 degrees
        # Rotation is only possible if the "L" shape formed by the current 
        # position and the perpendicular neighbor is valid.
        if orientation == 0:  # Horizontal -> Vertical
            # Check if we can rotate to vertical (downwards)
            # This requires the cell below (r+1, c) to be valid
            if r + 1 < rows and grid[r + 1][c] == 1:
                if (r, c, 1) not in visited:
                    visited.add((r, c, 1))
                    queue.append((r, c, 1, moves + 1))
            # Check if we can rotate to vertical (upwards)
            # This requires the cell above (r-1, c) to be valid
            if r - 1 >= 0 and grid[r - 1][c] == 1:
                if (r, c, 1) not in visited:
                    visited.add((r, c, 1))
                    queue.append((r, c, 1, moves + 1))
        else:  # Vertical -> Horizontal
            # Check if we can rotate to horizontal (rightwards)
            if c + 1 < cols and grid[r][c + 1] == 1:
                if (r, c, 0) not in visited:
                    visited.add((r, c, 0))
                    queue.append((r, c, 0, moves + 1))
            # Check if we can rotate to horizontal (leftwards)
            if c - 1 >= 0 and grid[r][c - 1] == 1:
                if (r, c, 0) not in visited:
                    visited.add((r, c, 0))
                    queue.append((r, c, 0, moves + 1))
                    
    return -1
