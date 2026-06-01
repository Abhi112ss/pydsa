METADATA = {
    "id": 2307,
    "name": "Check for Contradictions in Equations",
    "slug": "check-for-contradictions-in-equations",
    "category": "Union Find",
    "aliases": [],
    "tags": ["union_find", "graphs", "disjoint_set_union"],
    "difficulty": "medium",
    "time_complexity": "O(N * alpha(N))",
    "space_complexity": "O(N)",
    "description": "Determine if a list of equality and inequality equations is consistent using Disjoint Set Union.",
}

class DisjointSetUnion:
    """A standard implementation of the Disjoint Set Union (DSU) data structure."""

    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, i: int) -> int:
        """Finds the representative of the set containing i with path compression."""
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        """Unites the sets containing i and j using union by rank."""
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1


def solve(equations: list[list[str]]) -> bool:
    """
    Checks if the given equations are consistent.

    Args:
        equations: A list of equations where each equation is a list of 
                   [variable1, operator, variable2]. 
                   Example: [["a", "==", "b"], ["b", "!=", "a"]]

    Returns:
        True if the equations are consistent, False otherwise.

    Examples:
        >>> solve([["a", "==", "b"], ["b", "==", "c"], ["a", "!=", "c"]])
        False
        >>> solve([["a", "==", "b"], ["b", "!=", "c"], ["c", "==", "a"]])
        False
        >>> solve([["a", "==", "b"], ["b", "!=", "c"], ["a", "==", "c"]])
        False
        >>> solve([["a", "==", "b"], ["b", "!=", "c"], ["a", "!=", "c"]])
        True
    """
    # Map variable names (characters) to integer indices 0-25
    def var_to_idx(char: str) -> int:
        return ord(char) - ord('a')

    dsu = DisjointSetUnion(26)

    # First pass: Process all equality constraints to group variables
    for var1, operator, var2 in equations:
        if operator == "==":
            dsu.union(var_to_idx(var1), var_to_idx(var2))

    # Second pass: Check all inequality constraints for contradictions
    for var1, operator, var2 in equations:
        if operator == "!=":
            # If two variables are in the same set but are supposed to be unequal,
            # we have found a contradiction.
            if dsu.find(var_to_idx(var1)) == dsu.find(var_to_idx(var2)):
                return False

    return True
