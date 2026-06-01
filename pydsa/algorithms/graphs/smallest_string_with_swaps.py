METADATA = {
    "id": 1202,
    "name": "Smallest String With Swaps",
    "slug": "smallest-string-with-swaps",
    "category": "Graph",
    "aliases": [],
    "tags": ["union_find", "sorting", "graphs"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Given a string and a list of pairs of indices that can be swapped, find the lexicographically smallest string possible.",
}

class UnionFind:
    """Standard Disjoint Set Union (DSU) implementation with path compression and union by rank."""
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
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

def solve(s: str, pairs: list[list[int]]) -> str:
    """
    Finds the lexicographically smallest string by swapping characters at given index pairs.
    
    Args:
        s: The input string.
        pairs: A list of integer pairs representing indices that can be swapped.
        
    Returns:
        The lexicographically smallest string possible.
        
    Examples:
        >>> solve("dcab", [[0,3],[1,2]])
        'abcd'
        >>> solve("dcab", [[0,3],[1,2],[0,2]])
        'abcd'
    """
    n = len(s)
    dsu = UnionFind(n)

    # Step 1: Group all indices that belong to the same connected component
    for u, v in pairs:
        dsu.union(u, v)

    # Step 2: Organize indices and characters by their component root
    # components maps root_index -> list of indices in that component
    components: dict[int, list[int]] = {}
    for i in range(n):
        root = dsu.find(i)
        if root not in components:
            components[root] = []
        components[root].append(i)

    # Step 3: Sort characters within each component and place them back into the string
    # We convert s to a list because strings are immutable in Python
    result_chars = list(s)
    for root in components:
        indices = components[root]
        # Extract characters at these indices
        component_chars = [s[idx] for idx in indices]
        # Sort characters to get the smallest lexicographical order
        component_chars.sort()
        # Sort indices to ensure we place characters in the correct positions
        indices.sort()
        
        # Map the sorted characters back to the sorted indices
        for i in range(len(indices)):
            result_chars[indices[i]] = component_chars[i]

    return "".join(result_chars)
