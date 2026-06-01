METADATA = {
    "id": 305,
    "name": "Number of Islands II",
    "slug": "number-of-islands-ii",
    "category": "Union Find",
    "aliases": [],
    "tags": ["union-find", "grid", "dynamic-connectivity"],
    "difficulty": "hard",
    "time_complexity": "O(k * alpha(m * n))",
    "space_complexity": "O(m * n)",
    "description": "Given an m x n grid and a list of positions to add land, return the number of islands after each addition.",
}

class UnionFind:
    """A standard Disjoint Set Union (DSU) implementation with path compression and union by rank."""

    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.count = 0

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Union by rank to keep the tree flat
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            return True
        return False

def solve(m: int, n: int, positions: list[list[int]]) -> list[int]:
    """
    Calculates the number of islands after each land addition using Union-Find.

    Args:
        m: Number of rows in the grid.
        n: Number of columns in the grid.
        positions: A list of [row, col] coordinates representing land being added.

    Returns:
        A list of integers representing the number of islands after each addition.

    Examples:
        >>> solve(3, 3, [[0,0], [0,1], [1,2], [2,1]])
        [1, 1, 2, 3]
    """
    uf = UnionFind(m * n)
    is_land = [False] * (m * n)
    results = []
    current_islands = 0

    # Directions for 4-connectivity (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for r, c in positions:
        index = r * n + c
        
        # If the position is already land, the island count doesn't change
        if is_land[index]:
            results.append(current_islands)
            continue

        is_land[index] = True
        current_islands += 1

        # Check all 4 neighbors to see if we can merge existing islands
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            neighbor_index = nr * n + nc

            if 0 <= nr < m and 0 <= nc < n and is_land[neighbor_index]:
                # If neighbor is land and in a different component, merge them
                if uf.union(index, neighbor_index):
                    current_islands -= 1
        
        results.append(current_islands)

    return results
