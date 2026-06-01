METADATA = {
    "id": 1615,
    "name": "Maximal Network Rank",
    "slug": "maximal-network-rank",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "hash_map", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the maximum network rank of a city given a list of direct connections between cities.",
}

def solve(n: int, connections: list[list[int]]) -> int:
    """
    Calculates the maximal network rank of a graph.

    The network rank of two different cities is the total number of 
    direct connections from both cities. If the two cities are connected, 
    the connection is counted only once.

    Args:
        n: The number of cities.
        connections: A list of pairs [u, v] representing a direct connection.

    Returns:
        The maximum network rank possible for any pair of cities.

    Examples:
        >>> solve(4, [[0, 1], [0, 3], [1, 2], [1, 3]])
        3
        >>> solve(2, [[0, 1]])
        1
    """
    # adjacency_matrix[i][j] is True if there is a connection between i and j
    adjacency_matrix = [[False for _ in range(n)] for _ in range(n)]
    # degree[i] stores the number of connections for city i
    degree = [0] * n

    # Build the adjacency matrix and calculate degrees in O(E)
    for u, v in connections:
        adjacency_matrix[u][v] = True
        adjacency_matrix[v][u] = True
        degree[u] += 1
        degree[v] += 1

    max_rank = 0

    # Iterate through all possible pairs of cities (i, j)
    for i in range(n):
        for j in range(i + 1, n):
            # Rank is the sum of degrees of both cities
            current_rank = degree[i] + degree[j]
            
            # If there is a direct connection between i and j, 
            # we must subtract 1 because the edge is counted twice
            if adjacency_matrix[i][j]:
                current_rank -= 1
            
            if current_rank > max_rank:
                max_rank = current_rank

    return max_rank
