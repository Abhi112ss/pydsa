METADATA = {
    "id": 211,
    "name": "Design Add and Search Words Data Structure",
    "slug": "design_add_and_search_words_data_structure",
    "category": "Design",
    "aliases": ["WordDictionary", "Add and Search Word"],
    "tags": ["trie", "dfs", "design"],
    "difficulty": "medium",
    "time_complexity": "O(M)",
    "space_complexity": "O(N * M)",
    "description": "Design a data structure that supports adding new words and searching for words that match a pattern containing wildcard '.' characters.",
}


class TrieNode:
    """A node in the Trie data structure."""
    __slots__ = ['children', 'is_end']
    
    def __init__(self):
        self.children: dict[str, 'TrieNode'] = {}
        self.is_end: bool = False


class WordDictionary:
    """
    A word dictionary that supports adding words and searching with wildcards.
    
    Uses a Trie data structure for efficient storage and retrieval.
    The '.' wildcard in search matches any single character.
    """
    
    def __init__(self):
        """Initialize the WordDictionary with an empty Trie."""
        self.root = TrieNode()
    
    def add_word(self, word: str) -> None:
        """
        Add a word to the data structure.
        
        Args:
            word: The word to add to the dictionary.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        """
        Search for a word in the data structure.
        
        The word may contain '.' to represent any single character.
        
        Args:
            word: The word to search for, may contain '.' wildcards.
            
        Returns:
            True if the word exists in the dictionary, False otherwise.
        """
        return self._dfs_search(self.root, word, 0)
    
    def _dfs_search(self, node: TrieNode, word: str, index: int) -> bool:
        """
        Perform DFS search from the current node for the remaining word.
        
        Args:
            node: Current Trie node.
            word: The full word being searched.
            index: Current position in the word.
            
        Returns:
            True if the remaining word matches from this node.
        """
        # Base case: we've matched all characters
        if index == len(word):
            return node.is_end
        
        char = word[index]
        
        if char == '.':
            # Wildcard: try all possible children
            for child in node.children.values():
                if self._dfs_search(child, word, index + 1):
                    return True
            return False
        else:
            # Exact character match required
            if char not in node.children:
                return False
            return self._dfs_search(node.children[char], word, index + 1)


def solve() -> None:
    """
    Demonstrate the WordDictionary functionality.
    
    Examples:
        >>> wd = WordDictionary()
        >>> wd.add_word("bad")
        >>> wd.add_word("dad")
        >>> wd.add_word("mad")
        >>> wd.search("pad")  # Returns False
        False
        >>> wd.search("bad")  # Returns True
        True
        >>> wd.search(".ad")  # Returns True
        True
        >>> wd.search("b..")  # Returns True
        True
    """
    wd = WordDictionary()
    wd.add_word("bad")
    wd.add_word("dad")
    wd.add_word("mad")
    
    assert wd.search("pad") == False
    assert wd.search("bad") == True
    assert wd.search(".ad") == True
    assert wd.search("b..") == True
    print("All tests passed!")
