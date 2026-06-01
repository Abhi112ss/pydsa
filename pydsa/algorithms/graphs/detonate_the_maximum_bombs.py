METADATA = {
    "id": 2101,
    "name": "Detonate the Maximum Bombs",
    "slug": "detonate-the-maximum-bombs",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "dfs", "graph", "geometry"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the maximum number of bombs that can be detonated by choosing a single starting bomb, where a bomb detonates others within its radius.",
}

def solve(detonate: list[list[int]], bombs: list[list[int]]) -> int:
    """
    Calculates the maximum number of bombs that can be detonated starting from any single bomb.

    Args:
        detonate: A list of lists where detonate[i] is the radius of the i-th bomb.
        bombs: A list of lists where bombs[i] is the [x, y] coordinates of the i-th bomb.

    Returns:
        The maximum number of bombs detonated.

    Examples:
        >>> solve([[4,3],[2,3]], [[0,0],[1,1]])
        2
        >>> solve([[1,1],[1,1]], [[0,0],[1,1]])
        1
    """
    n = len(bombs)
    # adjacency_list[i] contains indices of bombs that bomb i can detonate
    adjacency_list: list[list[int]] = [[] for _ in range(n)]

    # Build the directed graph: O(n^2)
    for i in range(n):
        x1, y1 = bombs[i]
        r1 = detonate[i]
        for j in range(n):
            if i == j:
                continue
            x2, y2 = bombs[j]
            # Calculate squared Euclidean distance to avoid floating point issues
            dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
            # If distance is less than or equal to radius squared, bomb i hits bomb j
            if dist_sq <= r1 ** 2:
                adjacency_list[i].append(j)

    def get_detonation_count(start_node: int) -> int:
        """Performs BFS to count how many bombs are reached from start_node."""
        visited = {start_node}
        queue = [start_node]
        count = 0
        
        idx = 0
        while idx < len(queue):
            current = queue[idx]
            idx += 1
            count += 1
            
            for neighbor in adjacency_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return count

    max_bombs = 0
    # Try detonating each bomb as the starting point
    for i in range(n):
        max_bombs = max(max_bombs, get_detonation_count(i))
        # Optimization: if we found a way to detonate all bombs, return early
        if max_bombs == n:
            return n

    return max_bombs
