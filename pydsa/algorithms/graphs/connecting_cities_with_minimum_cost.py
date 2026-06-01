METADATA = {
    "id": 1135,
    "name": "Connecting Cities With Minimum Cost",
    "slug": "connecting_cities_with_minimum_cost",
    "category": "Graph",
    "aliases": [],
    "tags": ["union_find", "kruskal", "prim", "minimum_spanning_tree"],
    "difficulty": "medium",
    "time_complexity": "O(E log E)",
    "space_complexity": "O(V + E)",
    "description": "Find the minimum cost to connect all cities such that every city is reachable, or return -1 if it is impossible.",
}

class UnionFind:
    """A Disjoint Set Union (DSU) data structure with path compression and union by rank."""

    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.num_sets = n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        # Path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Union by rank
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            self.num_sets -= 1
            return True
        return False


def solve(n: int, connections: list[list[int]]) -> int:
    """
    Finds the minimum cost to connect all n cities using Kruskal's algorithm.

    Args:
        n: The number of cities.
        connections: A list of connections where connections[i] = [city1, city2, cost].

    Returns:
        The minimum cost to connect all cities, or -1 if not all cities can be connected.

    Examples:
        >>> solve(3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]])
        6
        >>> solve(4, [[1, 2, 1], [2, 3, 2], [3, 4, 3]])
        6
        >>> solve(4, [[1, 2, 1], [2, 3, 2]])
        -1
    """
    # Sort connections by cost to satisfy the greedy property of Kruskal's
    connections.sort(key=lambda x: x[2])

    dsu = UnionFind(n)
    total_min_cost = 0
    edges_used = 0

    for city_a, city_b, cost in connections:
        # If the two cities are not already in the same component, connect them
        if dsu.union(city_a, city_b):
            total_min_cost += cost
            edges_used += 1
            
            # Optimization: If we have used n-1 edges, all cities are connected
            if edges_used == n - 1:
                break

    # A connected graph with n nodes must have at least n-1 edges in its MST
    return total_min_cost if edges_used == n - 1 else -1
