METADATA = {
    "id": 3502,
    "name": "Minimum Cost to Reach Every Position",
    "slug": "minimum_cost_to_reach_every_position",
    "category": "Graph",
    "aliases": [],
    "tags": ["prim_algorithm", "kruskal_algorithm", "mst"],
    "difficulty": "medium",
    "time_complexity": "O(E log E)",
    "space_complexity": "O(E)",
    "description": "Find the minimum cost to connect all positions in a graph using a Minimum Spanning Tree approach.",
}

import heapq

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the minimum cost to connect all n positions using Kruskal's algorithm.

    Args:
        n: The number of positions (nodes), labeled 1 to n.
        edges: A list of edges where each edge is [u, v, cost].

    Returns:
        The minimum cost to connect all positions. Returns -1 if it's impossible 
        to connect all positions.

    Examples:
        >>> solve(3, [[1, 2, 5], [2, 3, 10], [1, 3, 15]])
        15
        >>> solve(4, [[1, 2, 1], [2, 3, 1]])
        -1
    """
    # Disjoint Set Union (DSU) to manage connected components
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    def find(i: int) -> int:
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])  # Path compression
        return parent[i]

    def union(i: int, j: int) -> bool:
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            # Union by rank
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_i] = root_j
                rank[root_j] += 1
            return True
        return False

    # Sort edges by cost to apply Kruskal's greedy approach
    edges.sort(key=lambda x: x[2])

    total_cost = 0
    edges_count = 0

    for u, v, cost in edges:
        # If u and v are not in the same component, add the edge to MST
        if union(u, v):
            total_cost += cost
            edges_count += 1
            # If we have connected all n nodes, we need n-1 edges
            if edges_count == n - 1:
                break

    # If we couldn't connect all nodes, return -1
    return total_cost if edges_count == n - 1 else -1
