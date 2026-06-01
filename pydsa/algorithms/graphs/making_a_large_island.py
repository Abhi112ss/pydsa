METADATA = {
    "id": 827,
    "name": "Making A Large Island",
    "slug": "making-a-large-island",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "union_find", "hash_map", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the largest island possible by changing at most one 0 to a 1 in a binary matrix.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Finds the maximum area of an island that can be formed by changing one 0 to a 1.

    Args:
        grid: A 2D list of integers where 0 represents water and 1 represents land.

    Returns:
        The size of the largest possible island.

    Examples:
        >>> solve([[1, 0], [0, 1]])
        3
        >>> solve([[1, 1], [1, 0]])
        4
    """
    n = len(grid)
    island_areas = {0: 0}  # Maps island_id to its area
    island_id_counter = 2  # Start IDs from 2 to distinguish from 0 and 1
    
    def get_neighbors(r: int, c: int) -> list[tuple[int, int]]:
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                yield nr, nc

    def dfs(r: int, c: int, current_id: int) -> int:
        """Calculates area of an island using DFS and marks it with current_id."""
        stack = [(r, c)]
        grid[r][c] = current_id
        area = 0
        while stack:
            curr_r, curr_c = stack.pop()
            area += 1
            for nr, nc in get_neighbors(curr_r, curr_c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = current_id
                    stack.append((nr, nc))
        return area

    # Step 1: Identify all existing islands and calculate their areas
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                area = dfs(r, c, island_id_counter)
                island_areas[island_id_counter] = area
                island_id_counter += 1

    # If the grid is all 1s, return the total area
    if not island_areas or max(island_areas.values(), default=0) == n * n:
        return n * n if n > 0 else 0

    # Initialize max_area with the largest existing island (in case we can't bridge anything)
    max_area = max(island_areas.values(), default=0)

    # Step 2: Iterate through every 0 and calculate potential area if flipped to 1
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                seen_islands = set()
                potential_area = 1  # The flipped 0 itself
                
                for nr, nc in get_neighbors(r, c):
                    neighbor_id = grid[nr][nc]
                    # If neighbor is part of an island and not already counted for this 0
                    if neighbor_id > 1 and neighbor_id not in seen_islands:
                        potential_area += island_areas[neighbor_id]
                        seen_islands.add(neighbor_id)
                
                max_area = max(max_area, potential_area)

    # Handle edge case where grid is all 0s
    return max_area if max_area > 0 else 1 if n > 0 else 0
