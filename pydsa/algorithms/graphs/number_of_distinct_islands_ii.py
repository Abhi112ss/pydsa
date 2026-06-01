METADATA = {
    "id": 711,
    "name": "Number of Distinct Islands II",
    "slug": "number-of-distinct-islands-ii",
    "category": "Medium",
    "aliases": [],
    "tags": ["dfs", "bfs", "hash_table", "geometry"],
    "difficulty": "medium",
    "time_complexity": "O(R*C log(R*C))",
    "space_complexity": "O(R*C)",
    "description": "Count the number of distinct islands where two islands are considered the same if they can be rotated or reflected to match.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Counts the number of distinct islands in a grid, considering rotations and reflections.

    Args:
        grid: A 2D list of integers where 1 represents land and 0 represents water.

    Returns:
        The number of unique island shapes under 8-way symmetry.

    Examples:
        >>> solve([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,0,1],[0,0,0,1,1]])
        2
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    unique_islands = set()

    def get_island_cells(start_r: int, start_c: int) -> list[tuple[int, int]]:
        """Performs BFS to find all connected land cells of an island."""
        cells = []
        queue = [(start_r, start_c)]
        visited[start_r][start_c] = True
        
        idx = 0
        while idx < len(queue):
            r, c = queue[idx]
            idx += 1
            cells.append((r, c))
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and \
                   grid[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        return cells

    def normalize(cells: list[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
        """
        Generates all 8 transformations, normalizes each to (0,0) origin,
        and returns the lexicographically smallest representation.
        """
        transformations = []
        
        # The 8 symmetries of a square (D4 group):
        # (x, y), (x, -y), (-x, y), (-x, -y), (y, x), (y, -x), (-y, x), (-y, -x)
        for sx, sy, swap in [
            (1, 1, False), (1, -1, False), (-1, 1, False), (-1, -1, False),
            (1, 1, True), (1, -1, True), (-1, 1, True), (-1, -1, True)
        ]:
            transformed = []
            for r, c in cells:
                if swap:
                    transformed.append((c * sx, r * sy))
                else:
                    transformed.append((r * sx, c * sy))
            
            # Normalize the transformed shape so the top-left cell is (0, 0)
            transformed.sort()
            base_r, base_c = transformed[0]
            normalized_shape = tuple((r - base_r, c - base_c) for r, c in transformed)
            transformations.append(normalized_shape)
            
        # Return the canonical representation (the smallest tuple)
        return min(transformations)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                # 1. Extract all coordinates belonging to the current island
                island_cells = get_island_cells(r, c)
                # 2. Find the canonical form of this island shape
                canonical_shape = normalize(island_cells)
                # 3. Add to set to count unique shapes
                unique_islands.add(canonical_shape)

    return len(unique_islands)
