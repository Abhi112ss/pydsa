METADATA = {
    "id": 3030,
    "name": "Find the Grid of Region Average",
    "slug": "find-the-grid-of-region-average",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "bfs", "dfs", "connected components"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the average value of connected components in a grid where cells with the same value are considered connected.",
}

def solve(grid: list[list[int]]) -> list[list[int]]:
    """
    Computes a grid where each cell contains the average value of its connected component.
    A connected component consists of adjacent cells (up, down, left, right) 
    that have the same value.

    Args:
        grid: A 2D list of integers representing the input grid.

    Returns:
        A 2D list of integers where each cell is the floor of the average 
        of its connected component.

    Examples:
        >>> solve([[1, 1, 2], [1, 2, 2], [3, 3, 3]])
        [[1, 1, 2], [1, 2, 2], [3, 3, 3]]
    """
    if not grid or not grid[0]:
        return []

    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                # Start a new BFS to find the connected component
                target_value = grid[r][c]
                component_cells = []
                queue = [(r, c)]
                visited[r][c] = True
                
                # Standard BFS traversal
                idx = 0
                while idx < len(queue):
                    curr_r, curr_c = queue[idx]
                    idx += 1
                    component_cells.append((curr_r, curr_c))
                    
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        if (0 <= nr < rows and 0 <= nc < cols and 
                            not visited[nr][nc] and grid[nr][nc] == target_value):
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                
                # Calculate the average of the identified component
                total_sum = sum(grid[cell_r][cell_c] for cell_r, cell_c in component_cells)
                average_value = total_sum // len(component_cells)
                
                # Fill the result grid with the calculated average
                for cell_r, cell_c in component_cells:
                    result[cell_r][cell_c] = average_value
                    
    return result
