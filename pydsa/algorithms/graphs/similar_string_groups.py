METADATA = {
    "id": 839,
    "name": "Similar String Groups",
    "slug": "similar-string-groups",
    "category": "Graph",
    "aliases": [],
    "tags": ["union_find", "dfs", "graph", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n^2 * m)",
    "space_complexity": "O(n)",
    "description": "Find the number of connected components in a graph where strings are nodes and edges exist between strings that differ by exactly two positions.",
}

class UnionFind:
    """A standard Disjoint Set Union (DSU) implementation with path compression and union by rank."""
    
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
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
            self.count -= 1

def solve(strs: list[str]) -> int:
    """
    Calculates the number of similar string groups using Union-Find.
    
    Two strings are similar if they are equal or if we can swap two letters 
    in one string to make it equal to the other. Since all strings are 
    anagrams of each other (implied by the problem context of similarity), 
    this is equivalent to checking if they differ in exactly 0 or 2 positions.

    Args:
        strs: A list of strings where all strings are anagrams of each other.

    Returns:
        The number of connected components (groups) of similar strings.

    Examples:
        >>> solve(["tars","rats","arts","star"])
        2
        >>> solve(["stand","tands","dants","tands"])
        1
    """
    n = len(strs)
    if n == 0:
        return 0
    
    def are_similar(s1: str, s2: str) -> bool:
        """Checks if two strings are similar by counting mismatches."""
        mismatches = 0
        for char1, char2 in zip(s1, s2):
            if char1 != char2:
                mismatches += 1
                # Optimization: if more than 2 mismatches, they can't be similar
                if mismatches > 2:
                    return False
        # Since they are anagrams, mismatches will be 0 or 2 if they are similar
        return mismatches == 0 or mismatches == 2

    dsu = UnionFind(n)
    m = len(strs[0])

    # Compare every pair of strings to build the graph components
    for i in range(n):
        for j in range(i + 1, n):
            # If strings are similar, union their sets in the DSU
            if are_similar(strs[i], strs[j]):
                dsu.union(i, j)

    return dsu.count
