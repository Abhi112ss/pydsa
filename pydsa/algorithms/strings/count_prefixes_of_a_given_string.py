METADATA = {
    "id": 2255,
    "name": "Count Prefixes of a Given String",
    "slug": "count-prefixes-of-a-given-string",
    "category": "String",
    "aliases": [],
    "tags": ["trie", "hash_map", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n * l)",
    "space_complexity": "O(n * l)",
    "description": "Count how many strings in a given list have a specific string as a prefix.",
}

class TrieNode:
    """A node in the Trie structure."""
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.count: int = 0

class Trie:
    """A Trie (Prefix Tree) implementation to store and count prefixes."""
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie and increments prefix counts."""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            # Increment count at each node to track how many words pass through this prefix
            current.count += 1

    def count_prefix(self, prefix: str) -> int:
        """Returns the number of words that have the given prefix."""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]
        return current.count

def solve(words: list[str], queries: list[str]) -> list[int]:
    """
    Counts how many strings in 'words' have each string in 'queries' as a prefix.

    Args:
        words: A list of strings to be indexed.
        queries: A list of prefix strings to search for.

    Returns:
        A list of integers representing the count of words for each query.

    Examples:
        >>> solve(["a", "b", "c"], ["a", "b", "c"])
        [1, 1, 1]
        >>> solve(["app", "apple", "apricot"], ["ap", "app", "apple", "b"])
        [3, 2, 1, 0]
    """
    trie = Trie()
    
    # Step 1: Build the Trie by inserting all words
    for word in words:
        trie.insert(word)
        
    # Step 2: Query the Trie for each prefix
    results = []
    for query in queries:
        results.append(trie.count_prefix(query))
        
    return results
