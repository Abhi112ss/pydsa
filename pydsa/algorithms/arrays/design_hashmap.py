METADATA = {
    "id": 706,
    "name": "Design HashMap",
    "slug": "design_hashmap",
    "category": "design",
    "aliases": [],
    "tags": ["hash_table", "design"],
    "difficulty": "medium",
    "time_complexity": "O(1) average",
    "space_complexity": "O(n)",
    "description": "Implements a simple hash map with O(1) average operations using separate chaining.",
}


class MyHashMap:
    """A hash map supporting put, get, and remove in O(1) average time.

    The implementation uses separate chaining with a fixed number of buckets.
    """

    def __init__(self, bucket_count: int = 1000) -> None:
        """Initialize the hash map with a given number of buckets."""
        self.bucket_count = bucket_count
        # Each bucket stores a list of (key, value) tuples.
        self.buckets: list[list[tuple[int, int]]] = [[] for _ in range(bucket_count)]

    def _hash(self, key: int) -> int:
        """Compute the bucket index for a given key."""
        return key % self.bucket_count

    def put(self, key: int, value: int) -> None:
        """Insert a (key, value) pair or update the value if the key exists."""
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for idx, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                # Update existing entry.
                bucket[idx] = (key, value)
                return
        # Append new entry if key not found.
        bucket.append((key, value))

    def get(self, key: int) -> int:
        """Return the value associated with the key, or -1 if the key does not exist."""
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for existing_key, existing_value in bucket:
            if existing_key == key:
                return existing_value
        return -1

    def remove(self, key: int) -> None:
        """Remove the key and its associated value if present."""
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for idx, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket.pop(idx)
                return


def solve() -> MyHashMap:
    """Create a MyHashMap, perform sample operations, and return the map.

    Args:
        None

    Returns:
        MyHashMap: The hash map after performing sample operations.

    Examples:
        >>> hashmap = solve()
        >>> hashmap.get(1)
        -1
        >>> hashmap.put(1, 10)
        >>> hashmap.get(1)
        10
        >>> hashmap.remove(1)
        >>> hashmap.get(1)
        -1
    """
    hashmap = MyHashMap()
    hashmap.put(1, 10)
    hashmap.put(2, 20)
    hashmap.remove(1)
    return hashmap