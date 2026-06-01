METADATA = {
    "id": 208,
    "name": "Implement Trie (Prefix Tree)",
    "slug": "implement_trie_prefix_tree",
    "category": "Design",
    "aliases": ["trie", "prefix tree"],
    "tags": ["trie", "design", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(L)",
    "space_complexity": "O(N * L)",
    "description": "Implement a trie with insert, search, and startsWith methods.",
}

class TrieNode:
    """A node in the Trie data structure."""
    def __init__(self):
        self.children: dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie.
        
        Args:
            word: The word to insert.
        """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Search for a word in the trie.
        
        Args:
            word: The word to search for.
            
        Returns:
            True if the word exists in the trie, False otherwise.
        """
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """Check if any word in the trie starts with the given prefix.
        
        Args:
            prefix: The prefix to check.
            
        Returns:
            True if any word starts with the prefix, False otherwise.
        """
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> TrieNode | None:
        """Traverse the trie to find the node corresponding to the last character of the prefix.
        
        Args:
            prefix: The prefix to traverse.
            
        Returns:
            The TrieNode at the end of the prefix, or None if the prefix is not found.
        """
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node


def solve():
    """Example usage of the Trie class.
    
    Returns:
        None
    """
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))   # True
    print(trie.search("app"))     # False
    print(trie.startsWith("app")) # True
    trie.insert("app")
    print(trie.search("app"))     # True
