METADATA = {
    "id": 425,
    "name": "Word Squares",
    "slug": "word-squares",
    "category": "Hard",
    "aliases": [],
    "tags": ["trie", "backtracking", "recursion"],
    "difficulty": "hard",
    "time_complexity": "O(N * L^L)",
    "space_complexity": "O(N * L)",
    "description": "Given a list of words, find all possible N x N matrices such that the i-th row and i-th column are the same word.",
}

class TrieNode:
    """A node in the Trie structure used for prefix searching."""
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.words: list[str] = []


class WordSquaresSolver:
    """Solver class for the Word Squares problem using Trie and Backtracking."""

    def __init__(self, words: list[str]) -> None:
        self.words = words
        self.n = len(words[0]) if words else 0
        self.root = TrieNode()
        self._build_trie()

    def _build_trie(self) -> None:
        """Builds a Trie where each node stores a list of words passing through it."""
        for word in self.words:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                # Store the word at each node to allow O(1) retrieval of words with this prefix
                node.words.append(word)

    def _get_words_with_prefix(self, prefix: str) -> list[str]:
        """Returns all words in the Trie that start with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.words

    def solve(self) -> list[list[str]]:
        """
        Finds all valid word squares using backtracking.

        Returns:
            list[list[str]]: A list of all valid N x N word squares.
        """
        if not self.words:
            return []

        results: list[list[str]] = []
        current_square: list[str] = []

        def backtrack() -> None:
            # Base case: if the square is full, we found a valid solution
            if len(current_square) == self.n:
                results.append(list(current_square))
                return

            # The prefix for the next word is formed by the characters at the 
            # current index of all previously placed words.
            # For row 'i', the prefix is [word[0][i], word[1][i], ..., word[i-1][i]]
            prefix_list = []
            for row_idx in range(len(current_square)):
                prefix_list.append(current_square[row_idx][len(current_square)])
            prefix = "".join(prefix_list)

            # Retrieve all words that satisfy the prefix requirement
            candidates = self._get_words_with_prefix(prefix)

            for candidate in candidates:
                current_square.append(candidate)
                backtrack()
                current_square.pop()

        backtrack()
        return results


def solve(words: list[str]) -> list[list[str]]:
    """
    Main entry point to solve the Word Squares problem.

    Args:
        words: A list of strings representing the dictionary.

    Returns:
        A list of lists of strings, where each inner list is a valid word square.

    Examples:
        >>> solve(["area", "lead", "wall", "lady", "ball"])
        [['area', 'read', 'e...']] # (Simplified example output)
    """
    solver = WordSquaresSolver(words)
    return solver.solve()
