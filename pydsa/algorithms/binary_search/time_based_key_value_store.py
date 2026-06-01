METADATA = {
    "id": 981,
    "name": "Time Based Key-Value Store",
    "slug": "time_based_key_value_store",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "binary_search", "design"],
    "difficulty": "medium",
    "time_complexity": "O(1) for set, O(log N) for get",
    "space_complexity": "O(N)",
    "description": "Design a data structure that can store multiple values for the same key with different timestamps and retrieve the value associated with the largest timestamp less than or equal to a given timestamp.",
}

class TimeMap:
    def __init__(self) -> None:
        """
        Initializes the data structure.
        Uses a dictionary where keys map to a list of (timestamp, value) tuples.
        Since timestamps are strictly increasing in set(), the lists remain sorted.
        """
        self.store: dict[str, list[tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores the key-value pair with the given timestamp.

        Args:
            key: The key to store the value under.
            value: The value to be stored.
            timestamp: The timestamp associated with the value.
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        Retrieves the value such that its timestamp is the largest less than or equal to the input timestamp.

        Args:
            key: The key to look up.
            timestamp: The target timestamp.

        Returns:
            The value associated with the largest timestamp <= target timestamp, 
            or an empty string if no such value exists.

        Examples:
            >>> tm = TimeMap()
            >>> tm.set("foo", "bar", 1)
            >>> tm.get("foo", 1)
            'bar'
            >>> tm.get("foo", 3)
            'bar'
            >>> tm.get("foo", 0)
            ''
        """
        if key not in self.store:
            return ""

        history = self.store[key]
        
        # Binary search to find the rightmost timestamp <= target timestamp
        # We search for the insertion point of the target timestamp
        low = 0
        high = len(history) - 1
        result_index = -1

        while low <= high:
            mid = (low + high) // 2
            # If current timestamp is less than or equal to target, it's a candidate
            if history[mid][0] <= timestamp:
                result_index = mid
                low = mid + 1
            else:
                # If current timestamp is too large, look in the left half
                high = mid - 1

        return history[result_index][1] if result_index != -1 else ""

def solve():
    """
    Example usage of the TimeMap class.
    """
    time_map = TimeMap()
    time_map.set("love", "leetcode", 10)
    print(time_map.get("love", 5))   # Expected: ""
    print(time_map.get("love", 10))  # Expected: "leetcode"
    print(time_map.get("love", 15))  # Expected: "leetcode"
    time_map.set("love", "rain", 20)
    print(time_map.get("love", 15))  # Expected: "leetcode"
    print(time_map.get("love", 20))  # Expected: "rain"
    print(time_map.get("love", 25))  # Expected: "rain"
