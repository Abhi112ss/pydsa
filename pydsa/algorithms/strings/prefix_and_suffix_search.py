METADATA = {
    "id": 745,
    "name": "Prefix and Suffix Search",
    "slug": "prefix-and-suffix-search",
    "category": "Design",
    "aliases": [],
    "tags": ["trie", "string_matching", "design"],
    "difficulty": "hard",
    "time_complexity": "O(N * L^2)",
    "space_complexity": "O(N * L^2)",
    "description": "Design a data structure that supports adding words and searching for words that match a given prefix and suffix.",
}

class TrieNode:
    """A node in the Trie structure."""
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}


class WordFilter:
    """
    A data structure that stores words and allows searching by prefix and suffix.
    
    The core idea is to store every word in a Trie in a transformed format:
    'suffix + '#' + prefix'. For a word 'apple', we insert:
    'e#apple', 'le#apple', 'ple#apple', 'pple#apple', 'apple#apple'.
    This allows a single Trie traversal to satisfy both prefix and suffix constraints.
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word to the filter by inserting all possible suffix-prefix combinations.

        Args:
            word: The string to be added to the dictionary.
        """
        # For each possible suffix of the word, create a combined string
        # 'suffix#word' ensures that when we search for 'suffix#prefix',
        # we are effectively checking both conditions.
        for i in range(len(word) + 1):
            suffix = word[i:]
            combined_string = f"{suffix}#{word}"
            
            # Standard Trie insertion
            current_node = self.root
            for char in combined_string:
                if char not in current_node.children:
                    current_node.children[char] = TrieNode()
                current_node = current_node.children[char]

    def search(self, suffix: str, prefix: str) -> bool:
        """
        Searches for a word that matches the given suffix and prefix.

        Args:
            suffix: The required suffix.
            prefix: The required prefix.

        Returns:
            True if a matching word exists, False otherwise.

        Examples:
            >>> filter = WordFilter()
            >>> filter.addWord("apple")
            >>> filter.search("e", "app")
            True
            >>> filter.search("e", "b")
            False
        """
        # The search pattern follows the same format used during insertion
        search_pattern = f"{suffix}#{prefix}"
        
        current_node = self.root
        for char in search_pattern:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
            
        return True


def solve() -> None:
    """
    Example usage of the WordFilter class.
    """
    word_filter = WordFilter()
    word_filter.addWord("apple")
    print(word_filter.search("e", "app"))  # Expected: True
    print(word_filter.search("e", "b"))   # Expected: False
    print(word_filter.search("le", "ap")) # Expected: True
    print(word_filter.search("le", "p"))  # Expected: False
