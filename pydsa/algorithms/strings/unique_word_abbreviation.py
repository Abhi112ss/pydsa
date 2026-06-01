METADATA = {
    "id": 288,
    "name": "Unique Word Abbreviation",
    "slug": "unique-word-abbreviation",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "design", "string"],
    "difficulty": "medium",
    "time_complexity": "O(1) per operation after O(N * L) initialization",
    "space_complexity": "O(N * L)",
    "description": "Design a data structure that stores a list of words and allows checking if an abbreviation uniquely identifies a word.",
}

class WordAbbreviation:
    def __init__(self, words: list[str]):
        """
        Args:
            words: A list of strings to be stored.
        """
        self.abbreviation_counts = {}
        for word in words:
            self._register_word(word)

    def _register_word(self, word: str) -> None:
        """
        Args:
            word: The word to process.
        """
        n = len(word)
        for i in range(n):
            abbr = word[i:]
            self.abbreviation_counts[abbr] = self.abbreviation_counts.get(abbr, 0) + 1

    def isUnique(self, abbr: str) -> bool:
        """
        Args:
            abbr: The abbreviation to check.

        Returns:
            True if the abbreviation uniquely identifies a word, False otherwise.
        """
        return self.abbreviation_counts.get(abbr, 0) == 1

def solve(words: list[str]) -> WordAbbreviation:
    """
    Args:
        words: A list of strings.

    Returns:
        An instance of WordAbbreviation.
    """
    return WordAbbreviation(words)