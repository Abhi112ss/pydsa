METADATA = {
    "id": 1584,
    "name": "Min Cost to Connect All Points",
    "slug": "min-cost-to-connect-all-points",
    "category": "Graph",
    "aliases": [],
    "tags": ["prim", "kruskal", "mst", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the minimum cost to connect all points in a 2D plane where the cost is the Manhattan distance.",
}

import heapq

def solve(points: list[list[int]]) -> int:
    """
    Calculates the minimum cost to connect all points using Prim's algorithm.

    The cost between two points is defined as the Manhattan distance: 
    |x1 - x2| + |y1 - y2|. We treat the points as a complete graph where 
    every point is connected to every other point.

    Args:
        points: A list of coordinates where points[i] = [xi, yi].

    Returns:
        The minimum total cost to connect all points.

    Examples:
        >>> solve([[0,0],[2,2],[3,10],[5,2],[7,0]])
        20
        >>> solve([[3,12],[-2,5],[-4,1]])
        18
    """
    n = len(points)
    if n <= 1:
        return 0

    # min_heap stores tuples of (cost, point_index)
    # We start from the first point (index 0) with a cost of 0
    min_heap: list[tuple[int, int]] = [(0, 0)]
    visited = [False] * n
    total_cost = 0
    edges_count = 0

    while edges_count < n:
        cost, curr_node = heapq.heappop(min_heap)

        # If the node is already in the MST, skip it
        if visited[curr_node]:
            continue

        # Add the node to the MST
        visited[curr_node] = True
        total_cost += cost
        edges_count += 1

        # Explore neighbors: in a complete graph, every unvisited node is a neighbor
        curr_x, curr_y = points[curr_node]
        for next_node in range(n):
            if not visited[next_node]:
                next_x, next_y = points[next_node]
                # Calculate Manhattan distance
                dist = abs(curr_x - next_x) + abs(curr_y - next_y)
                heapq.heappush(min_heap, (dist, next_node))

    return total_cost
