METADATA = {
    "id": 417,
    "name": "Pacific Atlantic Water Flow",
    "slug": "pacific-atlantic-water-flow",
    "category": "Matrix",
    "aliases": [],
    "tags": ["dfs", "bfs", "matrix", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m*n)",
    "description": "Find all grid cells from which water can flow to both the Pacific and Atlantic oceans.",
}

def solve(heights: list[list[int]]) -> list[list[int]]:
    """
    Finds all cells in a grid that can flow to both the Pacific and Atlantic oceans.
    
    Water flows from a cell to an adjacent cell if the adjacent cell's height 
    is less than or equal to the current cell's height. The Pacific Ocean 
    touches the top and left edges, while the Atlantic Ocean touches the 
    bottom and right edges.

    Args:
        heights: A 2D list of integers representing the elevation of each cell.

    Returns:
        A list of lists where each inner list contains the [row, col] coordinates 
        of a cell that can reach both oceans.

    Examples:
        >>> solve([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
        [[0, 4], [1, 3], [1, 4]]
    """
    if not heights or not heights[0]:
        return []

    rows, cols = len(heights), len(heights[0])
    pacific_reachable = set[tuple[int, int]]()
    atlantic_reachable = set[tuple[int, int]]()

    def dfs(r: int, c: int, reachable_set: set[tuple[int, int]]):
        """
        Performs DFS starting from ocean boundaries moving 'uphill'.
        """
        reachable_set.add((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            # Check bounds, ensure not visited, and ensure water can flow 'uphill'
            # (i.e., the next cell is higher or equal to the current cell)
            if (0 <= nr < rows and 0 <= nc < cols and 
                (nr, nc) not in reachable_set and 
                heights[nr][nc] >= heights[r][c]):
                dfs(nr, nc, reachable_set)

    # Start DFS from the top and bottom edges
    for c in range(cols):
        # Top edge (Pacific)
        dfs(0, c, pacific_reachable)
        # Bottom edge (Atlantic)
        dfs(rows - 1, c, atlantic_reachable)

    # Start DFS from the left and right edges
    for r in range(rows):
        # Left edge (Pacific)
        dfs(r, 0, pacific_reachable)
        # Right edge (Atlantic)
        dfs(r, cols - 1, atlantic_reachable)

    # The result is the intersection of cells reachable by both oceans
    common_cells = pacific_reachable.intersection(atlantic_reachable)
    return [list(cell) for cell in common_cells]
