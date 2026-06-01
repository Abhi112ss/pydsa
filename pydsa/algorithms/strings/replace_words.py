METADATA = {
    "id": 648,
    "name": "Replace Words",
    "slug": "replace-words",
    "category": "String",
    "aliases": [],
    "tags": ["trie", "hash_set", "string"],
    "difficulty": "medium",
    "time_complexity": "O(S), where S is the total number of characters in the sentence",
    "space_complexity": "O(R), where R is the total number of characters in the dictionary",
    "description": "Replace every word in a sentence with the shortest root from a given dictionary that is a prefix of that word.",
}

class TrieNode:
    """A node in the Trie structure."""
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False

class Trie:
    """A Trie implementation for efficient prefix searching."""
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the Trie."""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def find_shortest_prefix(self, word: str) -> str:
        """Finds the shortest prefix of the word that exists in the Trie."""
        current = self.root
        prefix = []
        for char in word:
            if char not in current.children:
                break
            current = current.children[char]
            prefix.append(char)
            # As soon as we find a valid root, return it to ensure it's the shortest
            if current.is_end_of_word:
                return "".join(prefix)
        return word

def solve(dictionary: list[str], sentence: str) -> str:
    """
    Replaces every word in a sentence with the shortest root from a given dictionary.

    Args:
        dictionary: A list of strings representing the available roots.
        sentence: A string containing words separated by spaces.

    Returns:
        A string where each word is replaced by its shortest root if one exists.

    Examples:
        >>> solve(["cat", "bat", "rat"], "the cattle was rattled by the battery")
        'the cat was rat by the bat'
        >>> solve(["a"], "a zoo a girl a man a planet a star")
        'a zoo a girl a man a planet a star'
    """
    # Build the Trie from the dictionary roots
    trie = Trie()
    for root in dictionary:
        trie.insert(root)

    words = sentence.split()
    result = []

    for word in words:
        # For each word, attempt to find the shortest matching root in the Trie
        shortest_root = trie.find_shortest_prefix(word)
        result.append(shortest_root)

    return " ".join(result)
