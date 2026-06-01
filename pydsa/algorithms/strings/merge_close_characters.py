METADATA = {
    "id": 3853,
    "name": "Merge Close Characters",
    "slug": "merge_close_characters",
    "category": "Union Find",
    "aliases": [],
    "tags": ["union_find", "string", "disjoint_set_union"],
    "difficulty": "medium",
    "time_complexity": "O(n * alpha(n))",
    "space_complexity": "O(1)",
    "description": "Merge characters in a string based on proximity constraints using Disjoint Set Union.",
}

class DisjointSetUnion:
    """A standard implementation of the Disjoint Set Union (DSU) data structure."""
    
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

def solve(s: str, constraints: list[tuple[int, int]]) -> str:
    """
    Merges characters in the string based on given index constraints.
    
    Args:
        s: The input string.
        constraints: A list of tuples where each tuple (i, j) represents 
                     that characters at index i and j should be merged.

    Returns:
        A string where merged characters are represented by the character 
        at the smallest index of their respective cluster.

    Examples:
        >>> solve("abcde", [(0, 1), (1, 2)])
        'aaade'
        >>> solve("leetcode", [(0, 4), (4, 7)])
        'lleetlee'
    """
    n = len(s)
    if n == 0:
        return ""

    dsu = DisjointSetUnion(n)

    # Group indices together based on the provided constraints
    for idx1, idx2 in constraints:
        dsu.union(idx1, idx2)

    # Map each index to the smallest index in its disjoint set
    # We first find the representative for each index
    representative_map = {}
    for i in range(n):
        root = dsu.find(i)
        # We want the smallest index in the cluster to be the representative
        # However, DSU find returns the root of the tree. 
        # To ensure we use the smallest index, we can pre-process or 
        # simply find the minimum index in each set.
        if root not in representative_map:
            representative_map[root] = root
        else:
            representative_map[root] = min(representative_map[root], root)

    # To strictly follow the "smallest index" rule, we need to ensure 
    # that for every index in a set, the representative is the minimum index.
    # Let's refine the mapping.
    min_index_in_set = {}
    for i in range(n):
        root = dsu.find(i)
        if root not in min_index_in_set:
            min_index_in_set[root] = i
        else:
            min_index_in_set[root] = min(min_index_in_set[root], i)

    # Construct the result string
    result_chars = []
    for i in range(n):
        root = dsu.find(i)
        # The character used is the one at the smallest index of the cluster
        target_index = min_index_in_set[root]
        result_chars.append(s[target_index])

    return "".join(result_chars)
