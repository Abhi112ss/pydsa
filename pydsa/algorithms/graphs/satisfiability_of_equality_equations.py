METADATA = {
    "id": 990,
    "name": "Satisfiability of Equality Equations",
    "slug": "satisfiability_of_equality_equations",
    "category": "Union Find",
    "aliases": [],
    "tags": ["union_find", "graph", "disjoint set union"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a set of equality and inequality equations is consistent using Union-Find.",
}

class UnionFind:
    """A standard Disjoint Set Union (DSU) implementation with path compression and union by rank."""

    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        # Path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
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

def solve(equations: list[str]) -> bool:
    """
    Determines if the given equations are satisfiable.

    Args:
        equations: A list of strings where each string is in the format "a==b" or "a!=b".

    Returns:
        True if the equations are satisfiable, False otherwise.

    Examples:
        >>> solve(["a==b", "b!=a"])
        False
        >>> solve(["b==a", "a==b"])
        True
        >>> solve(["a==b", "b==c", "a!=c"])
        False
    """
    # There are 26 lowercase English letters
    dsu = UnionFind(26)

    def char_to_idx(char: str) -> int:
        return ord(char) - ord('a')

    # First pass: Process all equality constraints to group variables
    for eq in equations:
        if eq[1] == '=':
            var_1 = char_to_idx(eq[0])
            var_2 = char_to_idx(eq[3])
            dsu.union(var_1, var_2)

    # Second pass: Check all inequality constraints for contradictions
    for eq in equations:
        if eq[1] == '!':
            var_1 = char_to_idx(eq[0])
            var_2 = char_to_idx(eq[3])
            # If two variables are in the same set but are supposed to be unequal, return False
            if dsu.find(var_1) == dsu.find(var_2):
                return False

    return True