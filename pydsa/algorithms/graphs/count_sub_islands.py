METADATA = {
    "id": 1905,
    "name": "Count Sub Islands",
    "slug": "count-sub-islands",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "grid", "union-find"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Count the number of islands in grid2 that are entirely contained within islands in grid1.",
}

def solve(grid1: list[list[int]], grid2: list[list[int]]) -> int:
    """
    Counts the number of islands in grid2 that are sub-islands of islands in grid1.
    
    An island in grid2 is a sub-island if every cell of that island is also 
    part of an island in grid1.

    Args:
        grid1: A 2D grid representing the parent land/water.
        grid2: A 2D grid representing the potential sub-islands.

    Returns:
        The total count of sub-islands found in grid2.

    Examples:
        >>> solve([[0,0,1,0,0],[0,1,1,0,0],[0,0,1,0,0],[1,1,0,0,1],[0,1,1,0,1]], 
        ...       [[0,0,0,0,0],[1,0,1,0,0],[0,1,1,0,0],[0,0,0,0,0],[0,1,1,0,0]])
        1
    """
    rows = len(grid2)
    cols = len(grid2[0])
    sub_island_count = 0

    def traverse_island(r: int, c: int) -> bool:
        """
        Performs a DFS to traverse an island in grid2 and checks if it's a sub-island.
        
        Args:
            r: Current row index.
            c: Current column index.
            
        Returns:
            True if all cells in this island are also land in grid1, False otherwise.
        """
        # Mark current cell as visited by turning it into water
        grid2[r][c] = 0
        
        # Check if the current cell in grid2 is also land in grid1
        is_sub_island = grid1[r][c] == 1
        
        # Explore 4-directional neighbors
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid2[nr][nc] == 1:
                # We use bitwise AND to ensure we visit the entire island 
                # even if we already found a cell that isn't in grid1.
                # This is crucial to mark the whole island as visited.
                res = traverse_island(nr, nc)
                is_sub_island = is_sub_island and res
                
        return is_sub_island

    for r in range(rows):
        for c in range(cols):
            # If we find land in grid2, it's a new island to evaluate
            if grid2[r][c] == 1:
                # If the entire traversal returns True, it's a sub-island
                if traverse_island(r, c):
                    sub_island_count += 1
                    
    return sub_island_count
