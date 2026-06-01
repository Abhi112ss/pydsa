METADATA = {
    "id": 980,
    "name": "Unique Paths III",
    "slug": "unique-paths-iii",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["dfs", "backtracking", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(3^N)",
    "space_complexity": "O(N)",
    "description": "Find the number of paths from the starting square to the ending square that walk over every non-obstacle square exactly once.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Finds the number of unique paths that visit every non-obstacle square exactly once.

    Args:
        grid: A 2D integer array where:
            0: empty square,
            1: obstacle square,
            2: starting square,
            3: ending square.

    Returns:
        The total number of unique paths that cover all 0s.

    Examples:
        >>> solve([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
        0
        >>> solve([[1,0,0,0],[0,0,0,0],[0,0,2,3]])
        2
    """
    rows = len(grid)
    cols = len(grid[0])
    
    start_pos = (0, 0)
    empty_squares_count = 0
    
    # Pre-process the grid to find start position and count required steps
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                continue
            if grid[r][c] == 2:
                start_pos = (r, c)
                empty_squares_count += 1
            elif grid[r][c] == 3:
                empty_squares_count += 1
            else:
                empty_squares_count += 1
                
    # Note: The problem defines 'empty squares' as 0s. 
    # We need to visit all 0s, plus the start (2) and end (3).
    # Let's refine the count: we need to visit all cells that are NOT 1.
    target_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 1:
                target_count += 1

    def backtrack(r: int, c: int, visited_count: int) -> int:
        # Base Case: If we reached the end square
        if grid[r][c] == 3:
            # Check if we have visited all required non-obstacle squares
            return 1 if visited_count == target_count else 0
        
        paths_found = 0
        original_val = grid[r][c]
        
        # Mark current cell as visited using an obstacle value to avoid extra space
        grid[r][c] = 1
        
        # Explore 4-directional neighbors
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1:
                paths_found += backtrack(nr, nc, visited_count + 1)
        
        # Backtrack: restore the cell's original value
        grid[r][c] = original_val
        return paths_found

    return backtrack(start_pos[0], start_pos[1], 1)
