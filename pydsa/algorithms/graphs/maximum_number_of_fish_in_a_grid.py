METADATA = {
    "id": 2658,
    "name": "Maximum Number of Fish in a Grid",
    "slug": "maximum-number-of-fish-in-a-grid",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "union_find", "connected-components"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the largest connected component of cells containing fish in a 2D grid.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Finds the maximum number of fish in a single connected component.

    Args:
        grid: A 2D list of integers where grid[i][j] represents the number of fish.
              A value of 0 indicates no fish.

    Returns:
        The maximum number of fish in any connected component.

    Examples:
        >>> solve([[0, 2, 0], [0, 0, 3]])
        5
        >>> solve([[0, 0, 0], [0, 0, 0]])
        0
        >>> solve([[1, 0, 1], [0, 0, 0], [1, 0, 1]])
        1
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    max_fish = 0

    def get_component_fish(start_r: int, start_c: int) -> int:
        """Performs iterative DFS to find the sum of fish in a component."""
        stack = [(start_r, start_c)]
        visited[start_r][start_c] = True
        current_component_sum = 0
        
        while stack:
            r, c = stack.pop()
            current_component_sum += grid[r][c]
            
            # Check all 4 adjacent directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                # If neighbor is within bounds, has fish, and hasn't been visited
                if (0 <= nr < rows and 
                    0 <= nc < cols and 
                    grid[nr][nc] > 0 and 
                    not visited[nr][nc]):
                    visited[nr][nc] = True
                    stack.append((nr, nc))
                    
        return current_component_sum

    # Iterate through every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If we find a cell with fish that hasn't been visited, it's a new component
            if grid[r][c] > 0 and not visited[r][c]:
                component_sum = get_component_fish(r, c)
                max_fish = max(max_fish, component_sum)

    return max_fish
