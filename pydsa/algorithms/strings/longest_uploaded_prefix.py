METADATA = {
    "id": 2424,
    "name": "Longest Uploaded Prefix",
    "slug": "longest-uploaded-prefix",
    "category": "String",
    "aliases": [],
    "tags": ["trie", "string_matching", "prefix"],
    "difficulty": "medium",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n * m)",
    "description": "Find the length of the longest prefix of any string in the array that is also a prefix of at least one other string in the array.",
}

class TrieNode:
    """A node in the Trie structure."""
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.count: int = 0

class Solution:
    def longestUploadedPrefix(self, words: list[str]) -> int:
        """
        Finds the length of the longest prefix shared by at least two strings.

        Args:
            words: A list of strings to analyze.

        Returns:
            The length of the longest prefix that appears in at least two different words.

        Examples:
            >>> Solution().longestUploadedPrefix(["abcd", "bcde", "abce", "cdef"])
            3
            >>> Solution().longestUploadedPrefix(["a", "b", "c"])
            0
        """
        root = TrieNode()
        max_prefix_len = 0

        for word in words:
            current_node = root
            # Traverse the Trie for the current word
            for i, char in enumerate(word):
                if char not in current_node.children:
                    current_node.children[char] = TrieNode()
                
                current_node = current_node.children[char]
                # Increment the count of how many words pass through this node
                current_node.count += 1
                
                # If count > 1, it means this prefix is shared by multiple words
                if current_node.count > 1:
                    # The length of the prefix is the current index + 1
                    max_prefix_len = max(max_prefix_len, i + 1)

        return max_prefix_len

def solve(words: list[str]) -> int:
    """
    Wrapper function to call the Solution class.

    Args:
        words: A list of strings.

    Returns:
        The length of the longest uploaded prefix.
    """
    return Solution().longestUploadedPrefix(words)
