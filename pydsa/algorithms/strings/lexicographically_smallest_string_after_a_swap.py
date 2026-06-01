METADATA = {
    "id": 3216,
    "name": "Lexicographically Smallest String After a Swap",
    "slug": "lexicographically-smallest-string-after-a-swap",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "strings", "union-find", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n alpha(n))",
    "space_complexity": "O(n)",
    "description": "Find the lexicographically smallest string possible by swapping adjacent characters that are equal.",
}

class UnionFind:
    """Standard Disjoint Set Union (DSU) implementation."""
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

def solve(s: str) -> str:
    """
    Finds the lexicographically smallest string by swapping adjacent identical characters.
    
    The core idea is that if s[i] == s[i+1], they belong to the same connected component.
    Any characters within the same connected component can be rearranged in any order.
    To get the lexicographically smallest string, we sort the characters within each component.

    Args:
        s: The input string.

    Returns:
        The lexicographically smallest string possible.

    Examples:
        >>> solve("aacab")
        'aabca'
        >>> solve("baaba")
        'aaabb'
    """
    n = len(s)
    if n <= 1:
        return s

    dsu = UnionFind(n)

    # Step 1: Group indices into connected components.
    # Two indices are connected if they are adjacent and have the same character.
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dsu.union(i, i + 1)

    # Step 2: Collect characters belonging to each component.
    # We use a dictionary where key is the root of the component and value is a list of chars.
    components: dict[int, list[str]] = {}
    for i in range(n):
        root = dsu.find(i)
        if root not in components:
            components[root] = []
        components[root].append(s[i])

    # Step 3: Sort characters within each component in descending order.
    # We sort descending so we can use pop() which is O(1) to get the smallest char.
    for root in components:
        components[root].sort(reverse=True)

    # Step 4: Reconstruct the string.
    # For each index, pick the smallest available character from its component.
    result_chars: list[str] = []
    for i in range(n):
        root = dsu.find(i)
        result_chars.append(components[root].pop())

    return "".join(result_chars)
