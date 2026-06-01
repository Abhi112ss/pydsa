METADATA = {
    "id": 1101,
    "name": "The Earliest Moment When Everyone Become Friends",
    "slug": "the-earliest-moment-when-everyone-become-friends",
    "category": "Union Find",
    "aliases": [],
    "tags": ["union_find", "sorting", "graphs"],
    "difficulty": "medium",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Find the earliest time when all people in a group become connected using Union-Find and sorting.",
}

class UnionFind:
    """A standard Disjoint Set Union (DSU) implementation with path compression and union by rank."""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_components = n

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
            
            self.num_components -= 1
            return True
        return False


def solve(n: int, logs: list[list[int]]) -> int:
    """
    Finds the earliest time when all n people become connected.

    Args:
        n: The number of people.
        logs: A list of logs where logs[i] = [timestamp, person_a, person_b].

    Returns:
        The earliest timestamp when everyone is connected, or -1 if they never are.

    Examples:
        >>> solve(3, [[1, 0, 1], [2, 1, 2]])
        2
        >>> solve(4, [[1, 0, 1], [2, 2, 3]])
        -1
    """
    # Sort logs by timestamp to process friendships in chronological order
    logs.sort(key=lambda x: x[0])

    dsu = UnionFind(n)

    for timestamp, person_a, person_b in logs:
        # Attempt to union the two people
        dsu.union(person_a, person_b)

        # If the number of connected components reaches 1, everyone is friends
        if dsu.num_components == 1:
            return timestamp

    return -1
