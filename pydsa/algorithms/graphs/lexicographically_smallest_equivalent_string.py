METADATA = {
    "id": 1061,
    "name": "Lexicographically Smallest Equivalent String",
    "slug": "lexicographically-smallest-equivalent-string",
    "category": "Union Find",
    "aliases": [],
    "tags": ["union_find", "disjoint_set", "strings"],
    "difficulty": "medium",
    "time_complexity": "O((n + m) * alpha(26))",
    "space_complexity": "O(1)",
    "description": "Find the lexicographically smallest equivalent string by grouping equivalent characters using a Disjoint Set Union structure.",
}

class UnionFind:
    """A Disjoint Set Union (DSU) implementation optimized for character sets."""

    def __init__(self):
        # parent[i] stores the parent of character i (0-25)
        self.parent = list(range(26))

    def find(self, i: int) -> int:
        """Finds the root of the set containing i with path compression."""
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        """Unites two sets, ensuring the root is always the smaller character index."""
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # To keep the lexicographically smallest character as the root,
            # we always point the larger root to the smaller root.
            if root_i < root_j:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j


def solve(s1: str, s2: str, base_str: str) -> str:
    """
    Constructs the lexicographically smallest equivalent string.

    Args:
        s1: The first string containing equivalence relations.
        s2: The second string containing equivalence relations.
        base_str: The string to be transformed.

    Returns:
        The transformed string where each character is replaced by its 
        lexicographically smallest equivalent.

    Examples:
        >>> solve("park", "tesc", "parser")
        'ascesr'
        >>> solve("hello", "world", "hold")
        'hold'
    """
    dsu = UnionFind()

    # Step 1: Process all equivalence relations from s1 and s2
    for char1, char2 in zip(s1, s2):
        idx1 = ord(char1) - ord('a')
        idx2 = ord(char2) - ord('a')
        dsu.union(idx1, idx2)

    # Step 2: Build the result string by finding the smallest root for each character
    result_chars = []
    for char in base_str:
        char_idx = ord(char) - ord('a')
        # The find operation returns the smallest character in the equivalence class
        smallest_root_idx = dsu.find(char_idx)
        result_chars.append(chr(smallest_root_idx + ord('a')))

    return "".join(result_chars)
