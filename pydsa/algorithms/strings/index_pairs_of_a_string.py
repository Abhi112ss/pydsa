METADATA = {
    "id": 1065,
    "name": "Index Pairs of a String",
    "slug": "index-pairs-of-a-string",
    "category": "String",
    "aliases": [],
    "tags": ["trie", "strings", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n^2 + m)",
    "space_complexity": "O(m)",
    "description": "Find all pairs of indices (i, j) such that the substring starting at i with length words[j] matches words[j].",
}

class TrieNode:
    """A node in the Trie structure."""
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        # Stores indices of words that end at this node
        self.word_indices: list[int] = []

class Trie:
    """A Trie implementation to store words and their original indices."""
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str, index: int) -> None:
        """Inserts a word into the Trie along with its index."""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.word_indices.append(index)

def solve(text: str, words: list[str]) -> list[list[int]]:
    """
    Finds all pairs of (i, j) where text[i : i + len(words[j])] == words[j].

    Args:
        text: The source string to search within.
        words: A list of strings to search for.

    Returns:
        A list of lists, where each inner list is [i, j] representing the 
        starting index in text and the index in the words list.

    Examples:
        >>> solve("abcde", ["abc", "de"])
        [[0, 0], [3, 1]]
        >>> solve("aaaaa", ["a", "aa"])
        [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1], [3, 0], [3, 1], [4, 0]]
    """
    trie = Trie()
    for index, word in enumerate(words):
        trie.insert(word, index)

    results: list[list[int]] = []
    n = len(text)

    # Iterate through every possible starting position in the text
    for i in range(n):
        current = trie.root
        # Traverse the Trie using characters from the text starting at index i
        for j in range(i, n):
            char = text[j]
            if char not in current.children:
                # No more words in the Trie match this prefix
                break
            
            current = current.children[char]
            
            # If the current path forms one or more words, add their indices to results
            if current.word_indices:
                for word_idx in current.word_indices:
                    results.append([i, word_idx])
                    
    return results
