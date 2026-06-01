METADATA = {
    "id": 677,
    "name": "Map Sum Pairs",
    "slug": "map-sum-pairs",
    "category": "Design",
    "aliases": [],
    "tags": ["trie", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(L) per operation, where L is the length of the key",
    "space_complexity": "O(N * L), where N is the number of keys and L is the average length",
    "description": "Design a data structure that maps a string key to an integer value and allows retrieving the sum of values of all keys with a given prefix.",
}

class TrieNode:
    """A node in the Trie structure."""
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.prefix_sum: int = 0

class MapSum:
    """
    A data structure that maps a string key to an integer value.
    It supports updating values and querying the sum of values for a prefix.
    """

    def __init__(self) -> None:
        """Initializes the MapSum object."""
        self.root = TrieNode()
        self.key_map: dict[str, int] = {}

    def insert(self, key: str, val: int) -> None:
        """
        Inserts a key-value pair into the data structure. 
        If the key already exists, the value is updated.

        Args:
            key: The string key to insert.
            val: The integer value associated with the key.
        """
        # Calculate the difference if the key already exists to update prefix sums correctly
        delta = val - self.key_map.get(key, 0)
        self.key_map[key] = val
        
        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            # Update the running sum for every node along the path of the key
            current.prefix_sum += delta

    def sum(self, prefix: str) -> int:
        """
        Returns the sum of all values of keys that have the given prefix.

        Args:
            prefix: The prefix string to query.

        Returns:
            The sum of values of all keys starting with the given prefix.
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]
        
        # The prefix_sum stored at the end of the prefix path contains the total sum
        return current.prefix_sum

def solve() -> None:
    """
    Example usage of the MapSum class.
    """
    map_sum = MapSum()
    map_sum.insert("apple", 3)
    print(map_sum.sum("ap"))    # Expected: 3
    map_sum.insert("app", 2)
    print(map_sum.sum("ap"))    # Expected: 5
    print(map_sum.sum("app"))   # Expected: 5
    print(map_sum.sum("apple")) # Expected: 3
    print(map_sum.sum("a"))     # Expected: 5
    print(map_sum.sum("b"))     # Expected: 0
