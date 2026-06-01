METADATA = {
    "id": 547,
    "name": "Number of Provinces",
    "slug": "number-of-provinces",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "union_find", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the total number of connected components in an undirected graph represented by an adjacency matrix.",
}

def solve(isConnected: list[list[int]]) -> int:
    """
    Calculates the number of provinces (connected components) in a graph.

    Args:
        isConnected: A 2D integer matrix where isConnected[i][j] = 1 if 
                     city i and city j are directly connected, and 0 otherwise.

    Returns:
        The total number of disjoint sets (provinces) in the graph.

    Examples:
        >>> solve([[1,1,0],[1,1,0],[0,0,1]])
        2
        >>> solve([[1,0,0],[0,1,0],[0,0,1]])
        3
    """
    n = len(isConnected)
    visited = [False] * n
    province_count = 0

    def dfs(city_index: int) -> None:
        """Performs a depth-first search to mark all reachable cities."""
        visited[city_index] = True
        # Check all potential neighbors for the current city
        for neighbor_index in range(n):
            # If there is a connection and the neighbor hasn't been visited
            if isConnected[city_index][neighbor_index] == 1 and not visited[neighbor_index]:
                dfs(neighbor_index)

    # Iterate through each city to ensure all components are discovered
    for i in range(n):
        if not visited[i]:
            # A new unvisited city signifies the start of a new province
            province_count += 1
            dfs(i)

    return province_count
