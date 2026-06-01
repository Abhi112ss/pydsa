METADATA = {
    "id": 1334,
    "name": "Find the City With the Smallest Number of Neighbors at a Threshold Distance",
    "slug": "find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance",
    "category": "Graph",
    "aliases": [],
    "tags": ["floyd_warshall", "dijkstra", "shortest_path", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(n^2)",
    "description": "Find the city that has the smallest number of neighbors within a given threshold distance, returning the city with the largest index in case of a tie.",
}

def solve(n: int, edges: list[list[int]], distance_threshold: int) -> int:
    """
    Finds the city with the smallest number of neighbors within a threshold distance.
    If multiple cities have the same smallest number of neighbors, returns the one with the largest index.

    Args:
        n: The number of cities.
        edges: A list of edges where edges[i] = [from_i, to_i, weight_i].
        distance_threshold: The maximum distance allowed to consider a neighbor.

    Returns:
        The index of the city that meets the criteria.

    Examples:
        >>> solve(4, [[0,1,4],[0,2,3],[1,2,1],[1,3,2],[2,3,1]], 3)
        3
        >>> solve(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2)
        0
    """
    # Initialize the distance matrix with infinity
    # dist[i][j] will hold the shortest distance between city i and city j
    inf = float('inf')
    dist = [[inf] * n for _ in range(n)]
    
    # Distance to self is always 0
    for i in range(n):
        dist[i][i] = 0
        
    # Populate initial distances from the edges provided
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w

    # Floyd-Warshall algorithm to find all-pairs shortest paths
    # O(n^3) complexity
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    min_neighbors_count = n
    result_city = -1

    # Iterate through each city to count how many neighbors are within the threshold
    for i in range(n):
        reachable_neighbors = 0
        for j in range(n):
            if i != j and dist[i][j] <= distance_threshold:
                reachable_neighbors += 1
        
        # Update result if we find a city with fewer neighbors.
        # If counts are equal, we prefer the larger index (i >= result_city).
        if reachable_neighbors <= min_neighbors_count:
            min_neighbors_count = reachable_neighbors
            result_city = i

    return result_city
