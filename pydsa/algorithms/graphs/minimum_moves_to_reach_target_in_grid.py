METADATA = {
    "id": 3609,
    "name": "Minimum Moves to Reach Target in Grid",
    "slug": "minimum_moves_to_reach_target_in_grid",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["bfs", "matrix", "shortest_path"],
    "difficulty": "medium",
    "time_complexity": "O(R * C)",
    "space_complexity": "O(R * C)",
    "description": "Find the minimum number of moves to reach a target cell in a grid using BFS.",
}

from collections import deque

def solve(grid: list[list[int]], start: list[int], target: list[int]) -> int:
    """
    Finds the minimum number of moves to reach the target cell from the start cell.

    Args:
        grid: A 2D list representing the grid where 0 is traversable and 1 is a wall.
        start: A list of two integers [row, col] representing the starting position.
        target: A list of two integers [row, col] representing the target position.

    Returns:
        The minimum number of moves to reach the target, or -1 if unreachable.

    Examples:
        >>> solve([[0, 0, 0], [1, 1, 0], [0, 0, 0]], [0, 0], [2, 0])
        6
        >>> solve([[0, 1], [1, 0]], [0, 0], [1, 1])
        -1
    """
    rows = len(grid)
    cols = len(grid[0])
    start_row, start_col = start
    target_row, target_col = target

    # Edge case: start is target
    if start_row == target_row and start_col == target_col:
        return 0

    # Edge case: start or target is a wall
    if grid[start_row][start_col] == 1 or grid[target_row][target_col] == 1:
        return -1

    # BFS setup: queue stores (row, col, current_distance)
    queue = deque([(start_row, start_col, 0)])
    visited = set([(start_row, start_col)])

    # Directions for moving Up, Down, Left, Right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        curr_row, curr_col, dist = queue.popleft()

        for dr, dc in directions:
            next_row, next_col = curr_row + dr, curr_col + dc

            # Check boundaries and if the cell is traversable and not visited
            if (0 <= next_row < rows and 
                0 <= next_col < cols and 
                grid[next_row][next_col] == 0 and 
                (next_row, next_col) not in visited):
                
                # If target is reached, return distance + 1
                if next_row == target_row and next_col == target_col:
                    return dist + 1
                
                visited.add((next_row, next_col))
                queue.append((next_row, next_col, dist + 1))

    return -1
