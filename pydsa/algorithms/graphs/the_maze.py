METADATA = {
    "id": 490,
    "name": "The Maze",
    "slug": "the-maze",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "dfs", "graph_traversal"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m*n)",
    "description": "Determine if a ball starting at a given position can reach a target position in a maze by rolling without stopping until it hits a wall.",
}

from collections import deque

def solve(maze: list[list[str]], start: list[int], target: list[int]) -> bool:
    """
    Determines if a ball can reach the target in a maze by rolling until it hits a wall.

    Args:
        maze: A 2D grid where '0' is empty space and '1' is a wall.
        start: The starting [row, col] coordinates.
        target: The target [row, col] coordinates.

    Returns:
        True if the target is reachable, False otherwise.

    Examples:
        >>> maze = [["0","0","0","0"],["1","1","0","1"],["0","0","0","0"],["0","1","1","0"]]
        >>> start = [0,0]
        >>> target = [3,3]
        >>> solve(maze, start, target)
        False
    """
    rows = len(maze)
    cols = len(maze[0])
    
    # Queue for BFS: stores (row, col)
    queue = deque([(start[0], start[1])])
    # Visited set to prevent redundant processing of the same resting positions
    visited = {(start[0], start[1])}
    
    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        curr_r, curr_c = queue.popleft()
        
        # Check if we have reached the target position
        if [curr_r, curr_c] == target:
            return True
            
        for dr, dc in directions:
            next_r, next_c = curr_r, curr_c
            
            # Simulate the ball rolling in the current direction until it hits a wall or boundary
            while 0 <= next_r + dr < rows and 0 <= next_c + dc < cols and maze[next_r + dr][next_c + dc] == "0":
                next_r += dr
                next_c += dc
            
            # If the final resting position hasn't been visited, add it to the queue
            if (next_r, next_c) not in visited:
                visited.add((next_r, next_c))
                queue.append((next_r, next_c))
                
    return False
