METADATA = {
    "id": 317,
    "name": "Shortest Distance from All Buildings",
    "slug": "shortest-distance-from-all-buildings",
    "category": "BFS",
    "aliases": [],
    "tags": ["bfs", "matrix", "shortest path"],
    "difficulty": "hard",
    "time_complexity": "O(k * m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find an empty land such that the total distance to all buildings is minimized.",
}

from collections import deque

def solve(grid: list[list[int]]) -> int:
    """
    Finds the empty land that minimizes the total distance to all buildings.

    Args:
        grid: A 2D grid where 1 is building, 0 is empty land, and -1 is obstacle.

    Returns:
        The minimum total distance to all buildings, or -1 if no such land exists.

    Examples:
        >>> solve([[0,0,1,0,0],[0,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,0,1,0,0]])
        5
        >>> solve([[1,0,0],[0,0,0],[0,0,1]])
        4
    """
    if not grid or not grid[0]:
        return -1

    rows = len(grid)
    cols = len(grid[0])

    # total_dist[r][c] stores the sum of distances from all buildings to (r, c)
    total_dist = [[0] * cols for _ in range(rows)]
    # reachable_count[r][c] stores how many buildings can reach (r, c)
    reachable_count = [[0] * cols for _ in range(rows)]
    
    num_buildings = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                num_buildings += 1
                # Perform BFS from each building to find distances to all reachable empty lands
                queue = deque([(r, c, 0)])
                visited = [[False] * cols for _ in range(rows)]
                visited[r][c] = True
                
                while queue:
                    curr_r, curr_c, dist = queue.popleft()
                    
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        
                        # Only traverse to empty land (0)
                        if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 0:
                            visited[nr][nc] = True
                            reachable_count[nr][nc] += 1
                            total_dist[nr][nc] += dist + 1
                            queue.append((nr, nc, dist + 1))

    min_distance = float('inf')
    found = False

    # Check all empty lands that were reached by all buildings
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and reachable_count[r][c] == num_buildings:
                found = True
                if total_dist[r][c] < min_distance:
                    min_distance = total_dist[r][c]

    return int(min_distance) if found else -1
