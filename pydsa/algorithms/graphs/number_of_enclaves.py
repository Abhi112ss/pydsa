METADATA = {
    "id": 1020,
    "name": "Number of Enclaves",
    "slug": "number-of-enclaves",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "flood_fill", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Count the number of land cells in a grid that cannot reach the boundary.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the number of land cells (1s) that cannot reach the boundary of the grid.

    Args:
        grid: A 2D list of integers where 1 represents land and 0 represents water.

    Returns:
        The total number of land cells that are 'enclaved' (cannot reach the edge).

    Examples:
        >>> solve([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
        3
        >>> solve([[0,1,1,0],[0,0,1,0],[0,0,0,0],[0,0,1,0]])
        3
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    def flood_fill(r: int, c: int) -> None:
        """Performs an iterative DFS to mark reachable land cells as water (0)."""
        stack = [(r, c)]
        grid[r][c] = 0  # Mark as visited by turning land to water
        
        while stack:
            curr_r, curr_c = stack.pop()
            # Check all 4 adjacent directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    stack.append((nr, nc))

    # Step 1: Traverse the boundaries. 
    # Any land cell on the boundary (or connected to it) is not an enclave.
    for r in range(rows):
        for c in range(cols):
            is_boundary = (r == 0 or r == rows - 1 or c == 0 or c == cols - 1)
            if is_boundary and grid[r][c] == 1:
                flood_fill(r, c)

    # Step 2: Count the remaining land cells.
    # Since we turned all boundary-connected land into 0, only enclaves remain as 1.
    enclave_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                enclave_count += 1

    return enclave_count
