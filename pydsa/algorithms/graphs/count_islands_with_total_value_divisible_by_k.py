METADATA = {
    "id": 3619,
    "name": "Count Islands With Total Value Divisible by K",
    "slug": "count-islands-with-total-value-divisible-by-k",
    "category": "Matrix",
    "aliases": [],
    "tags": ["dfs", "bfs", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(R * C)",
    "space_complexity": "O(R * C)",
    "description": "Count the number of islands in a grid where the sum of the values of all cells in the island is divisible by k.",
}

def solve(grid: list[list[int]], k: int) -> int:
    """
    Counts the number of islands whose total sum of cell values is divisible by k.
    An island is a group of connected 1s (or non-zero values) in a grid.
    
    Args:
        grid: A 2D list of integers representing the grid.
        k: The divisor to check against the island's total sum.

    Returns:
        The count of islands whose sum % k == 0.

    Examples:
        >>> solve([[1, 1, 0], [0, 1, 0], [0, 0, 2]], 2)
        1
        # Island 1: sum = 1+1+1 = 3 (3%2 != 0)
        # Island 2: sum = 2 (2%2 == 0)
        # Result: 1
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    island_count = 0

    def get_island_sum(start_r: int, start_c: int) -> int:
        """Performs iterative BFS to find the sum of an island."""
        total_sum = 0
        queue = [(start_r, start_c)]
        visited[start_r][start_c] = True
        
        idx = 0
        while idx < len(queue):
            r, c = queue[idx]
            idx += 1
            total_sum += grid[r][c]

            # Check all 4 neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                # If neighbor is within bounds, not visited, and part of an island (non-zero)
                if (0 <= nr < rows and 0 <= nc < cols and 
                    not visited[nr][nc] and grid[nr][nc] != 0):
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        
        return total_sum

    # Iterate through every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If we find an unvisited non-zero cell, it's a new island
            if grid[r][c] != 0 and not visited[r][c]:
                current_island_sum = get_island_sum(r, c)
                # Check if the accumulated sum satisfies the divisibility condition
                if current_island_sum % k == 0:
                    island_count += 1

    return island_count
