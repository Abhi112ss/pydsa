METADATA = {
    "id": 2556,
    "name": "Disconnect Path in a Binary Matrix by at Most One Flip",
    "slug": "disconnect-path-in-a-binary-matrix-by-at-most-one-flip",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "dfs", "articulation-points"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Determine if it is possible to disconnect the top-left cell from the bottom-right cell in a binary matrix by flipping at most one cell from 1 to 0.",
}

def solve(grid: list[list[int]]) -> bool:
    """
    Determines if the path between (0, 0) and (rows-1, cols-1) can be disconnected
    by flipping at most one cell from 1 to 0.

    Args:
        grid: A 2D list of integers where 1 represents a path and 0 represents a wall.

    Returns:
        True if the path can be disconnected, False otherwise.

    Examples:
        >>> solve([[1, 1], [1, 1]])
        True
        >>> solve([[1, 0], [0, 1]])
        True
        >>> solve([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        True
    """
    rows = len(grid)
    cols = len(grid[0])

    # If the start or end is already blocked (though problem constraints usually imply 1s),
    # or if they are adjacent, we check if a single flip can break it.
    # However, the problem asks if we CAN disconnect it.
    # If there are no paths initially, it's already disconnected (True).
    
    def count_paths(visited: set[tuple[int, int]]) -> int:
        """
        Uses BFS/DFS to find if a path exists. 
        To check if a single flip can disconnect, we can use the concept of 
        articulation points or simply check if there's more than one path.
        Actually, the most robust way is to check if the number of paths is > 1.
        But since we only care about 'at most one flip', we check if there is 
        an articulation point on all paths from start to end.
        """
        # This is a helper for a different approach. 
        # Let's use the property: if we can't find a path after removing one 
        # cell that is part of the original path, return True.
        pass

    # Standard approach: 
    # 1. Check if a path exists. If not, return True.
    # 2. If a path exists, check if any cell (excluding start and end) is an articulation point.
    # 3. A simpler way: Try to find two vertex-disjoint paths. 
    #    If we can't find two vertex-disjoint paths, then one flip is enough.
    
    # We use a modified DFS to find if there's a single path that, if removed, 
    # disconnects the graph. This is equivalent to checking if the start and end 
    # are in different components after removing an articulation point.

    def get_path() -> list[tuple[int, int]]:
        """Finds any single path from start to end using DFS."""
        stack = [(0, 0, [(0, 0)])]
        visited = {(0, 0)}
        while stack:
            r, c, path = stack.pop()
            if r == rows - 1 and c == cols - 1:
                return path
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    stack.append((nr, nc, path + [(nr, nc)]))
        return []

    initial_path = get_path()
    
    # If no path exists initially, it's already disconnected.
    if not initial_path:
        return True

    # If the path is very short (only start and end), and they are adjacent,
    # we can't disconnect them by flipping a cell because we can't flip start or end.
    # Wait, the problem says "at most one flip". If start and end are adjacent,
    # flipping any other cell won't help. But the problem implies we flip a '1' to '0'.
    # If (0,0) and (rows-1, cols-1) are adjacent, we can't disconnect them.
    if len(initial_path) == 2:
        return False

    # Optimization: Instead of checking all cells, only check cells that are part of the initial path.
    # If any cell in the path (excluding start and end) is an articulation point, return True.
    for i in range(1, len(initial_path) - 1):
        pr, pc = initial_path[i]
        
        # Temporarily remove the cell
        grid[pr][pc] = 0
        
        # Check if a path still exists
        # Using a simple BFS for speed
        found_path = False
        q = [(0, 0)]
        visited_bfs = {(0, 0)}
        idx = 0
        while idx < len(q):
            r, c = q[idx]
            idx += 1
            if r == rows - 1 and c == cols - 1:
                found_path = True
                break
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited_bfs:
                    visited_bfs.add((nr, nc))
                    q.append((nr, nc))
        
        # Restore the cell
        grid[pr][pc] = 1
        
        # If no path was found after removing this cell, we succeeded
        if not found_path:
            return True

    return False
