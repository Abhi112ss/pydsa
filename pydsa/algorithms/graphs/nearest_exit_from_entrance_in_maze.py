METADATA = {
    "id": 1926,
    "name": "Nearest Exit from Entrance in Maze",
    "slug": "nearest-exit-from-entrance-in-maze",
    "category": "Graphs",
    "aliases": [],
    "tags": ["bfs", "graphs", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the minimum number of steps to reach any boundary cell that is not the starting cell using BFS.",
}

from collections import deque

def solve(maze: list[list[str]], entrance: list[int]) -> int:
    """
    Finds the shortest distance from the entrance to the nearest exit in a maze.

    An exit is defined as any empty cell ('.') located on the boundary of the maze
    that is not the entrance itself.

    Args:
        maze: A 2D grid of strings where '.' is an empty cell and '+' is a wall.
        entrance: A list of two integers [row, col] representing the starting position.

    Returns:
        The minimum number of steps to reach an exit, or -1 if no exit is reachable.

    Examples:
        >>> solve([["."],["+","."],["+","."]], [0,0])
        2
        >>> solve([["."],["+","."],["+","."]], [0,0]) # (Example 2)
        -1
    """
    rows = len(maze)
    cols = len(maze[0])
    start_row, start_col = entrance[0], entrance[1]

    # Queue stores tuples of (row, col, current_distance)
    queue = deque([(start_row, start_col, 0)])
    
    # Mark the entrance as visited by changing it to a wall to avoid revisiting
    maze[start_row][start_col] = "+"

    # Directions for moving Up, Down, Left, Right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        curr_row, curr_col, distance = queue.popleft()

        for dr, dc in directions:
            next_row, next_col = curr_row + dr, curr_col + dc

            # Check if the next cell is within bounds and is an empty cell
            if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == ".":
                
                # Check if this empty cell is on the boundary
                # If it is, it's an exit (since we only move to '.' cells, 
                # and we already marked the entrance as '+', any boundary '.' is an exit)
                if (next_row == 0 or next_row == rows - 1 or 
                    next_col == 0 or next_col == cols - 1):
                    return distance + 1

                # Mark as visited and add to queue for further exploration
                maze[next_row][next_col] = "+"
                queue.append((next_row, next_col, distance + 1))

    return -1
