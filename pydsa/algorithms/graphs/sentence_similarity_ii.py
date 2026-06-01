METADATA = {
    "id": 737,
    "name": "Sentence Similarity II",
    "slug": "sentence-similarity-ii",
    "category": "Union Find",
    "aliases": [],
    "tags": ["union_find", "dfs", "hash_table"],
    "difficulty": "medium",
    "time_complexity": "O(N + P * alpha(P))",
    "space_complexity": "O(P)",
    "description": "Determine if two sentences are similar given a list of similar word pairs, where similarity is transitive.",
}

class UnionFind:
    """A standard Disjoint Set Union (DSU) implementation with path compression and union by rank."""

    def __init__(self) -> None:
        self.parent: dict[str, str] = {}
        self.rank: dict[str, int] = {}

    def find(self, x: str) -> str:
        """Finds the representative of the set containing x with path compression."""
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x
        
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: str, y: str) -> None:
        """Unites the sets containing x and y using union by rank."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def solve(sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool:
    """
    Determines if two sentences are similar based on transitive word similarity.

    Args:
        sentence1: A list of words representing the first sentence.
        sentence2: A list of words representing the second sentence.
        similarPairs: A list of pairs where each pair [w1, w2] indicates similarity.

    Returns:
        True if the sentences are similar, False otherwise.

    Examples:
        >>> solve(["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "fine"], ["acting", "drama"], ["drama", "talent"]])
        True
        >>> solve(["a"], ["b"], [["a", "b"]])
        True
    """
    # If lengths differ, sentences cannot be similar
    if len(sentence1) != len(sentence2):
        return False

    dsu = UnionFind()

    # Build the disjoint set components from the similarity pairs
    # This handles the transitivity: if (a, b) and (b, c) are pairs, a and c will share a root
    for word1, word2 in similarPairs:
        dsu.union(word1, word2)

    # Check each word pair in the sentences
    for w1, w2 in zip(sentence1, sentence2):
        # Words are similar if they are identical or belong to the same DSU component
        if w1 == w2:
            continue
        
        # If one word is not in the DSU and they aren't equal, they can't be similar
        if w1 not in dsu.parent or w2 not in dsu.parent:
            return False
            
        if dsu.find(w1) != dsu.find(w2):
            return False

    return True