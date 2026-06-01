METADATA = {
    "id": 758,
    "name": "Bold Words in String",
    "slug": "bold-words-in-string",
    "category": "String",
    "aliases": [],
    "tags": ["string", "trie", "interval_merging"],
    "difficulty": "hard",
    "time_complexity": "O(N * L)",
    "space_complexity": "O(N)",
    "description": "Given a string and a list of words, return the string with bolded words formatted using markdown asterisks, merging overlapping or adjacent bolded intervals.",
}

class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False

class Solution:
    def boldWords(self, s: str, words: list[str]) -> str:
        """
        Identifies all occurrences of words in the string and applies bold formatting.

        Args:
            s: The input string to process.
            words: A list of words that should be bolded.

        Returns:
            The string with bolded words wrapped in asterisks, with merged intervals.

        Examples:
            >>> sol = Solution()
            >>> sol.boldWords("abcde", ["abc", "cde"])
            '**abcde**'
            >>> sol.boldWords("aaaaa", ["aaa", "aaa"])
            '**aaaaa**'
            >>> sol.boldWords("abcde", ["ab", "de"])
            '**ab**c**de**'
        """
        n = len(s)
        # Build a Trie for efficient multi-pattern matching
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True

        # boolean array to mark characters that should be bolded
        is_bold = [False] * n

        # Step 1: Find all occurrences of words using the Trie
        for i in range(n):
            node = root
            for j in range(i, n):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.is_end:
                    # Mark all characters in this match as bold
                    for k in range(i, j + 1):
                        is_bold[k] = True

        # Step 2: Construct the result string by checking the boolean array
        # We iterate through the string and wrap contiguous blocks of True in asterisks
        result = []
        i = 0
        while i < n:
            if is_bold[i]:
                # Find the end of the current contiguous bold block
                start = i
                while i < n and is_bold[i]:
                    i += 1
                result.append("**")
                result.append(s[start:i])
                result.append("**")
            else:
                result.append(s[i])
                i += 1

        return "".join(result)

def solve(s: str, words: list[str]) -> str:
    """Helper function to call the Solution class."""
    return Solution().boldWords(s, words)
