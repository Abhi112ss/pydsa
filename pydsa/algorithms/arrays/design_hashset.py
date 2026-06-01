METADATA = {
    "id": 705,
    "name": "Design HashSet",
    "slug": "design_hashset",
    "category": "Design",
    "aliases": ["design_hash_set", "hashset"],
    "tags": ["hash_table", "design"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design a HashSet without using any built-in hash table libraries.",
}

class MyHashSet:
    def __init__(self) -> None:
        """Initialize the hash set with a fixed-size boolean array."""
        self.size = 1000001  # Covers all possible values (0 to 10^6)
        self.data = [False] * self.size

    def add(self, key: int) -> None:
        """Add the key to the hash set."""
        self.data[key] = True

    def remove(self, key: int) -> None:
        """Remove the key from the hash set."""
        self.data[key] = False

    def contains(self, key: int) -> bool:
        """Check if the key is present in the hash set."""
        return self.data[key]


def solve(operations: list[str], values: list[int]) -> list[bool | None]:
    """
    Simulate a HashSet with add, remove, and contains operations.

    Args:
        operations: List of operation names: "add", "remove", "contains".
        values: List of integer values corresponding to each operation.

    Returns:
        List of results: None for add/remove, bool for contains.

    Examples:
        >>> solve(["add", "add", "contains", "contains", "remove", "contains"], [1, 2, 1, 3, 2, 2])
        [None, None, True, False, None, False]
    """
    hash_set = MyHashSet()
    results: list[bool | None] = []

    for op, val in zip(operations, values):
        if op == "add":
            hash_set.add(val)
            results.append(None)
        elif op == "remove":
            hash_set.remove(val)
            results.append(None)
        elif op == "contains":
            results.append(hash_set.contains(val))

    return results