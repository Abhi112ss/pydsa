METADATA = {
    "id": 642,
    "name": "Design Search Autocomplete System",
    "slug": "design-search-autocomplete-system",
    "category": "Design",
    "aliases": [],
    "tags": ["trie", "design", "hash_map", "heap"],
    "difficulty": "hard",
    "time_complexity": "O(L * N) for search where L is sentence length and N is total nodes, though practically optimized by Trie structure",
    "space_complexity": "O(N) where N is the total number of characters in all sentences stored",
    "description": "Design a system that provides top 3 autocomplete suggestions based on user input history and frequency.",
}

import heapq

class TrieNode:
    """A node in the Trie structure."""
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False
        # Stores mapping of {sentence: frequency} that pass through this node
        # This allows faster retrieval of all sentences under a prefix
        self.sentences_at_node: dict[str, int] = {}

class AutocompleteSystem:
    def __init__(self, sentences: list[str], times: list[int]):
        """
        Initializes the system with historical sentences and their frequencies.

        Args:
            sentences: A list of historical sentences.
            times: A list of frequencies corresponding to each sentence.
        """
        self.root = TrieNode()
        self.current_input = ""
        
        for sentence, time in zip(sentences, times):
            self._insert(sentence, time)

    def _insert(self, sentence: str, count: int) -> None:
        """Inserts or updates a sentence in the Trie."""
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            # Update the frequency map at every node in the path for the sentence
            node.sentences_at_node[sentence] = node.sentences_at_node.get(sentence, 0) + count
        node.is_end = True

    def input(self, c: str) -> list[str]:
        """
        Processes a character input and returns top 3 suggestions.

        Args:
            c: The character typed. '#' indicates end of input.

        Returns:
            A list of top 3 sentences (sorted by frequency descending, then lexicographically).
        """
        if c == '#':
            # End of sentence: save the current sentence to the Trie
            self._insert(self.current_input, 1)
            self.current_input = ""
            return []
        
        self.current_input += c
        
        # 1. Traverse the Trie to find the node representing the current prefix
        node = self.root
        for char in self.current_input:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # 2. Use a Min-Heap to find the top 3 sentences
        # We store (-frequency, sentence) to handle the sorting requirements:
        # Higher frequency first, then lexicographical order for ties.
        # Since Python's heapq is a min-heap, we use (-freq, sentence) 
        # so that the "smallest" element is the one with the highest freq 
        # and the "smallest" string (lexicographically).
        # Wait, to get top 3 with min-heap: 
        # We want to keep the 3 largest. A min-heap of size 3 keeps the largest.
        # But we have a tie-breaker rule: higher frequency, then lexicographical.
        # Let's use a custom comparison logic via a heap of (frequency, -sentence).
        
        candidates = []
        for sentence, freq in node.sentences_at_node.items():
            # We use (freq, negative_sentence) to use a min-heap of size 3.
            # However, Python strings don't have a "negative". 
            # Let's use a simpler approach: collect all and sort, 
            # or use a heap with a custom wrapper.
            # Given the constraints, collecting and sorting is efficient enough.
            candidates.append((freq, sentence))
            
        # Sort by frequency descending, then sentence ascending
        candidates.sort(key=lambda x: (-x[0], x[1]))
        
        return [item[1] for item in candidates[:3]]

def solve():
    """
    Example usage of the AutocompleteSystem.
    """
    sentences = ["i love you", "leetcode", "i love leetcode"]
    times = [5, 10, 3]
    obj = AutocompleteSystem(sentences, times)
    
    # Test cases
    print(obj.input("i"))      # Expected: ["i love you", "i love leetcode"]
    print(obj.input(" "))      # Expected: ["i love you", "i love leetcode"]
    print(obj.input("l"))      # Expected: ["i love you", "i love leetcode"]
    print(obj.input("e"))      # Expected: ["i love leetcode"]
    print(obj.input("#"))      # End of input
    print(obj.input("a"))      # Expected: []
