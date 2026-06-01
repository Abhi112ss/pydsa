METADATA = {
    "id": 2416,
    "name": "Sum of Prefix Scores of Strings",
    "slug": "sum-of-prefix-scores-of-strings",
    "category": "String",
    "aliases": [],
    "tags": ["trie", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Calculate the sum of scores for each string where a score is the number of strings in the array that share the same prefix.",
}

class TrieNode:
    """A node in the Trie structure."""
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.count: int = 0

class Solution:
    def solve(self, words: list[str]) -> int:
        """
        Calculates the sum of prefix scores for all strings in the input list.
        
        The score of a string is defined as the number of strings in the input 
        that share the same prefix as the current string's characters.

        Args:
            words: A list of strings to process.

        Returns:
            The total sum of prefix scores for all strings.

        Examples:
            >>> sol = Solution()
            >>> sol.solve(["abcd", "bce", "bcde", "cde"])
            16
            >>> sol.solve(["a"])
            1
        """
        root = TrieNode()

        # Step 1: Build the Trie and increment counts at each node
        # Each node's count represents how many strings pass through that prefix
        for word in words:
            current_node = root
            for char in word:
                if char not in current_node.children:
                    current_node.children[char] = TrieNode()
                current_node = current_node.children[char]
                current_node.count += 1

        total_score_sum = 0

        # Step 2: Traverse the Trie for each word to sum up the counts
        # The score of a word is the sum of 'count' values of all nodes in its path
        for word in words:
            current_node = root
            word_score = 0
            for char in word:
                # Since all words were inserted, the path is guaranteed to exist
                current_node = current_node.children[char]
                word_score += current_node.count
            total_score_sum += word_score

        return total_score_sum

def solve(words: list[str]) -> int:
    """Helper function to match the requested interface."""
    return Solution().solve(words)
