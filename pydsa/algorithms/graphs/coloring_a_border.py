METADATA = {
    "id": 1034,
    "name": "Coloring A Border",
    "slug": "coloring-a-border",
    "category": "Matrix",
    "aliases": [],
    "tags": ["dfs", "bfs", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Color the border of a connected component of the same color with a new color.",
}

def solve(grid: list[list[int]], row: int, col: int, new_color: int) -> list[list[int]]:
    """
    Colors the border of a connected component with a new color.

    A border cell is defined as a cell belonging to the component that is either
    on the boundary of the grid or adjacent to a cell that does not belong to 
    the component.

    Args:
        grid: A 2D list of integers representing the grid.
        row: The starting row index.
        col: The starting column index.
        new_color: The integer color to apply to the border.

    Returns:
        The modified grid with the component's border colored.

    Examples:
        >>> grid = [[1, 1], [1, 2]]
        >>> solve(grid, 0, 0, 3)
        [[3, 3], [3, 2]]
    """
    rows_count = len(grid)
    cols_count = len(grid[0])
    original_color = grid[row][col]
    
    # If the target color is the same as the original, no changes needed
    if original_color == new_color:
        return grid

    visited = set()
    border_cells = []

    def get_neighbors(r: int, c: int) -> list[tuple[int, int]]:
        neighbors = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows_count and 0 <= nc < cols_count:
                neighbors.append((nr, nc))
        return neighbors

    # Use BFS to find all cells in the connected component
    queue = [(row, col)]
    visited.add((row, col))
    
    idx = 0
    while idx < len(queue):
        curr_r, curr_c = queue[idx]
        idx += 1
        
        is_border = False
        
        # A cell is on the grid boundary
        if curr_r == 0 or curr_r == rows_count - 1 or curr_c == 0 or curr_c == cols_count - 1:
            is_border = True
        
        for nr, nc in get_neighbors(curr_r, curr_c):
            if grid[nr][nc] == original_color:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
            else:
                # A cell is a border if it's adjacent to a different color
                is_border = True
        
        if is_border:
            border_cells.append((curr_r, curr_c))

    # Apply the new color only to the identified border cells
    for r, c in border_cells:
        grid[r][c] = new_color

    return grid
