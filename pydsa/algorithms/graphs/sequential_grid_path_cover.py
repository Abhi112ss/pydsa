METADATA = {
    "id": 3565,
    "name": "Sequential Grid Path Cover",
    "slug": "sequential_grid_path_cover",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["dfs", "backtracking", "grid"],
    "difficulty": "hard",
    "time_complexity": "O(2^(n*m))",
    "space_complexity": "O(n*m)",
    "description": "Find the minimum number of paths required to cover all cells in a grid such that each cell is visited exactly once.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Args:
        grid: A 2D list representing the grid where 1 indicates a traversable cell and 0 indicates an obstacle.

    Returns:
        The minimum number of paths needed to cover all traversable cells.
    """
    rows = len(grid)
    cols = len(grid[0])
    cells_to_cover = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                cells_to_cover.append((r, c))
    
    if not cells_to_cover:
        return 0

    total_cells = len(cells_to_cover)
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    min_paths = [total_cells]

    def backtrack(remaining_count: int, current_paths: int):
        if remaining_count == 0:
            if current_paths < min_paths[0]:
                min_paths[0] = current_paths
            return

        if current_paths >= min_paths[0]:
            return

        start_r, start_c = -1, -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    start_r, start_c = r, c
                    break
            if start_r != -1:
                break

        def find_path(r: int, c: int):
            visited[r][c] = True
            
            can_extend = False
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and not visited[nr][nc]:
                    can_extend = True
                    find_path(nr, nc)
            
            if not can_extend:
                backtrack(remaining_count - 1, current_paths + 1)
            
            visited[r][c] = False

        find_path(start_r, start_c)

    backtrack(total_cells, 0)
    return min_paths[0]