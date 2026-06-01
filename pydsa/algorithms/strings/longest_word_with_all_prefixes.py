METADATA = {
    "id": 1858,
    "name": "Longest Word With All Prefixes",
    "slug": "longest-word-with-all-prefixes",
    "category": "String",
    "aliases": [],
    "tags": ["trie", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(N * L)",
    "space_complexity": "O(N * L)",
    "description": "Find the longest string in an array such that every prefix of the string is also present in the array.",
}

class TrieNode:
    """A node in the Trie structure."""
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False

class Solution:
    def longestWord(self, words: list[str]) -> str:
        """
        Finds the longest word in the list such that all its prefixes are also in the list.
        If multiple words have the same maximum length, the lexicographically smallest is returned.

        Args:
            words: A list of strings.

        Returns:
            The longest word satisfying the prefix condition, or an empty string if none exist.

        Examples:
            >>> Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
            'apple'
            >>> Solution().longestWord(["w", "wo", "wor", "worl", "world"])
            'world'
        """
        root = TrieNode()

        # Step 1: Build the Trie
        for word in words:
            current_node = root
            for char in word:
                if char not in current_node.children:
                    current_node.children[char] = TrieNode()
                current_node = current_node.children[char]
            current_node.is_end_of_word = True

        longest_word = ""

        # Step 2: Traverse the Trie to find the valid longest word
        # We use DFS to explore paths where every node is marked as is_end_of_word
        def dfs(node: TrieNode, current_path: str) -> None:
            nonlocal longest_word
            
            # Check if the current path is a better candidate
            # Criteria: longer length, or same length but lexicographically smaller
            if len(current_path) > len(longest_word):
                longest_word = current_path
            elif len(current_path) == len(longest_word):
                if current_path < longest_word:
                    longest_word = current_path

            # Sort children keys to ensure deterministic traversal, 
            # though the length/lexicographical check handles the logic.
            for char in sorted(node.children.keys()):
                child_node = node.children[char]
                # Only proceed if the child node represents a complete word from the input
                if child_node.is_end_of_word:
                    dfs(child_node, current_path + char)

        # Start DFS from root. Note: root itself is not a word, 
        # but its children might be.
        for char in sorted(root.children.keys()):
            child_node = root.children[char]
            if child_node.is_end_of_word:
                dfs(child_node, char)

        return longest_word

def solve(words: list[str]) -> str:
    """Helper function to call the Solution class."""
    return Solution().longestWord(words)
