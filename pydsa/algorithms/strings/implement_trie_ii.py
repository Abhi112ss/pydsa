METADATA = {
    "id": 1804,
    "name": "Implement Trie II",
    "slug": "implement-trie-ii",
    "category": "Design",
    "aliases": [],
    "tags": ["trie", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(m) per operation, where m is the length of the word",
    "space_complexity": "O(total_characters * alphabet_size)",
    "description": "Design a data structure that supports inserting words, searching for exact words, and checking if any word starts with a given prefix, while tracking the count of words passing through each node.",
}

class TrieNode:
    """A node in the Trie structure."""
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False
        # count tracks how many words pass through or end at this node
        self.count: int = 0

class Trie:
    """
    A Trie (Prefix Tree) implementation that supports word insertion,
    exact word search, and prefix existence checks.
    """

    def __init__(self) -> None:
        """Initializes the Trie with a root node."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.

        Args:
            word: The string to be inserted.

        Examples:
            >>> trie = Trie()
            >>> trie.insert("apple")
        """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
            # Increment count for every node in the path of the word
            current_node.count += 1
        current_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns true if the word is in the trie.

        Args:
            word: The string to search for.

        Returns:
            True if the word exists, False otherwise.

        Examples:
            >>> trie = Trie()
            >>> trie.insert("apple")
            >>> trie.search("apple")
            True
            >>> trie.search("app")
            False
        """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns true if there is any word in the trie that starts with the given prefix.

        Args:
            prefix: The prefix to check.

        Returns:
            True if the prefix exists, False otherwise.

        Examples:
            >>> trie = Trie()
            >>> trie.insert("apple")
            >>> trie.startsWith("app")
            True
        """
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        # If we successfully traversed the prefix, it exists in the trie
        return True

def solve():
    """
    Entry point for testing the Trie implementation.
    """
    trie = Trie()
    trie.insert("apple")
    print(f"Search 'apple': {trie.search('apple')}")    # Expected: True
    print(f"Search 'app': {trie.search('app')}")        # Expected: False
    print(f"StartsWith 'app': {trie.startsWith('app')}") # Expected: True
    trie.insert("app")
    print(f"Search 'app' after insert: {trie.search('app')}") # Expected: True
