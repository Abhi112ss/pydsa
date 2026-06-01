METADATA = {
    "id": 1992,
    "name": "Find All Groups of Farmland",
    "slug": "find-all-groups-of-farmland",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "union_find", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Identify all connected components of farmland cells in a grid where each component is a rectangular area.",
}

def solve(grid: list[list[int]]) -> list[list[list[int]]]:
    """
    Finds all groups of farmland in a grid using Breadth-First Search (BFS).

    Each group of farmland is a connected component of 1s. Since the problem 
    guarantees that each group is a rectangle, we can find all cells belonging 
    to a group by traversing its connected components.

    Args:
        grid: A 2D list of integers where 1 represents farmland and 0 represents non-farmland.

    Returns:
        A list of lists of lists, where each inner list contains the coordinates 
        [row, col] of the cells in a specific farmland group.

    Examples:
        >>> solve([[1, 0, 0], [0, 1, 1], [0, 1, 1]])
        [[[0, 0]], [[1, 1], [1, 2], [2, 1], [2, 2]]]
        >>> solve([[1, 1], [1, 1]])
        [[[0, 0], [0, 1], [1, 0], [1, 1]]]
    """
    if not grid or not grid[0]:
        return []

    rows = len(grid)
    cols = len(grid[0])
    visited = set[tuple[int, int]]()
    farmland_groups = []

    for r in range(rows):
        for c in range(cols):
            # If we find farmland that hasn't been visited, it's a new group
            if grid[r][c] == 1 and (r, c) not in visited:
                current_group = []
                queue = [(r, c)]
                visited.add((r, c))
                
                # Standard BFS to find all connected cells in the current component
                idx = 0
                while idx < len(queue):
                    curr_r, curr_c = queue[idx]
                    idx += 1
                    current_group.append([curr_r, curr_c])

                    # Check all 4 adjacent directions
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        
                        if (0 <= nr < rows and 0 <= nc < cols and 
                            grid[nr][nc] == 1 and (nr, nc) not in visited):
                            visited.add((nr, nc))
                            queue.append((nr, nc))
                
                farmland_groups.append(current_group)

    return farmland_groups
