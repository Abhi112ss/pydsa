METADATA = {
    "id": 1625,
    "name": "Lexicographically Smallest String After Applying Operations",
    "slug": "lexicographically-smallest-string-after-applying-operations",
    "category": "String",
    "aliases": [],
    "tags": ["union_find", "strings", "sorting", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the lexicographically smallest string possible by swapping characters based on specific modular arithmetic constraints.",
}

class UnionFind:
    """Standard Disjoint Set Union (DSU) implementation with path compression."""
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j


def solve(s: str, a: int, b: int, k: int) -> str:
    """
    Finds the lexicographically smallest string by grouping indices that can be swapped.

    Args:
        s: The input string.
        a: The first modular constraint (swap if i % a == j % a).
        b: The second modular constraint (swap if i % b == j % b).
        k: The third modular constraint (swap if i % k == j % k).

    Returns:
        The lexicographically smallest string possible.

    Examples:
        >>> solve("abcde", 2, 3, 4, 1)
        'abcde'
        >>> solve("dcba", 1, 1, 1, 1)
        'abcd'
    """
    n = len(s)
    dsu = UnionFind(n)

    # Group indices that can be swapped based on the three modular rules.
    # If two indices share the same remainder for any of a, b, or k, 
    # they belong to the same connected component.
    for mod in [a, b, k]:
        # For each remainder, all indices with that remainder can be swapped.
        # We only need to union each index with the first index found for that remainder.
        first_occurrence = {}
        for i in range(n):
            remainder = i % mod
            if remainder in first_occurrence:
                dsu.union(i, first_occurrence[remainder])
            else:
                first_occurrence[remainder] = i

    # Group characters and their original indices by their DSU root.
    groups: dict[int, list[str]] = {}
    indices_by_group: dict[int, list[int]] = {}
    
    for i in range(n):
        root = dsu.find(i)
        if root not in groups:
            groups[root] = []
            indices_by_group[root] = []
        groups[root].append(s[i])
        indices_by_group[root].append(i)

    # For each group, sort the characters and place them back into the sorted indices.
    # This ensures the smallest characters occupy the smallest available indices in the group.
    result = [""] * n
    for root in groups:
        chars = sorted(groups[root])
        sorted_indices = sorted(indices_by_group[root])
        for char, idx in zip(chars, sorted_indices):
            result[idx] = char

    return "".join(result)
