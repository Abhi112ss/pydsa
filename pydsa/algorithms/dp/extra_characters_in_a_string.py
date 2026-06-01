METADATA = {
    "id": 2707,
    "name": "Extra Characters in a String",
    "slug": "extra-characters-in-a-string",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "string_matching", "trie"],
    "difficulty": "medium",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n + m * sigma)",
    "description": "Find the minimum number of extra characters in a string after removing all occurrences of words from a dictionary.",
}

class TrieNode:
    """A node in a Trie structure to store dictionary words."""
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False

class Solution:
    def solve(self, s: str, words: list[str]) -> int:
        """
        Calculates the minimum number of extra characters in string s after 
        removing all occurrences of words from the dictionary.

        Args:
            s: The input string.
            words: A list of strings representing the dictionary.

        Returns:
            The minimum number of extra characters remaining.

        Examples:
            >>> sol = Solution()
            >>> sol.solve("leetscode", ["leet", "code"])
            1
            >>> sol.solve("abcde", ["ab", "bc"])
            1
        """
        n = len(s)
        root = TrieNode()

        # Build the Trie for efficient prefix matching
        for word in words:
            current_node = root
            for char in word:
                if char not in current_node.children:
                    current_node.children[char] = TrieNode()
                current_node = current_node.children[char]
            current_node.is_end = True

        # dp[i] represents the minimum extra characters in the prefix s[0:i]
        # Initialize with the worst case: every character is an extra character
        dp = list(range(n + 1))

        for i in range(n):
            # Option 1: The character at s[i] is treated as an extra character
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)

            # Option 2: Try to match words starting from index i using the Trie
            current_node = root
            for j in range(i, n):
                char = s[j]
                if char not in current_node.children:
                    break
                
                current_node = current_node.children[char]
                
                # If we found a word in the Trie, update the DP state for the end of this word
                if current_node.is_end:
                    # dp[j + 1] is the min extra chars for prefix ending at j
                    # We transition from dp[i] (the state before this word started)
                    dp[j + 1] = min(dp[j + 1], dp[i])

        return dp[n]

def solve(s: str, words: list[str]) -> int:
    """Helper function to match the required interface."""
    return Solution().solve(s, words)
