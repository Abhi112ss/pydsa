METADATA = {
    "id": 3491,
    "name": "Phone Number Prefix",
    "slug": "phone-number-prefix",
    "category": "String",
    "aliases": [],
    "tags": ["trie", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(N * L)",
    "space_complexity": "O(N * L)",
    "description": "Determine if a given phone number starts with any of the provided prefixes using a Trie structure.",
}

class TrieNode:
    """A node in the Trie structure."""
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_prefix: bool = False

class Trie:
    """A Trie implementation for efficient prefix searching."""
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, prefix: str) -> None:
        """Inserts a prefix into the Trie."""
        current = self.root
        for char in prefix:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_prefix = True

    def has_prefix(self, number: str) -> bool:
        """Checks if the given number starts with any prefix stored in the Trie."""
        current = self.root
        for char in number:
            if char not in current.children:
                return False
            current = current.children[char]
            # If we encounter a node marked as end of prefix, the number matches
            if current.is_end_of_prefix:
                return True
        return False

def solve(prefixes: list[str], phone_numbers: list[str]) -> list[bool]:
    """
    Determines for each phone number if it starts with any of the given prefixes.

    Args:
        prefixes: A list of strings representing the prefixes to check against.
        phone_numbers: A list of strings representing the phone numbers.

    Returns:
        A list of booleans where the i-th element is True if phone_numbers[i] 
        starts with one of the prefixes, and False otherwise.

    Examples:
        >>> solve(["123", "456"], ["12345", "789", "4567"])
        [True, False, True]
        >>> solve(["9", "12"], ["987", "123", "456"])
        [True, True, False]
    """
    trie = Trie()
    
    # Build the Trie with all provided prefixes
    for prefix in prefixes:
        trie.insert(prefix)
    
    # For each phone number, check if it matches any prefix in the Trie
    results = []
    for number in phone_numbers:
        results.append(trie.has_prefix(number))
        
    return results
