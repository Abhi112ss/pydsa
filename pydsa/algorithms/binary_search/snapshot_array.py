METADATA = {
    "id": 1146,
    "name": "Snapshot Array",
    "slug": "snapshot_array",
    "category": "Design",
    "aliases": [],
    "tags": ["binary_search", "hash_map", "design"],
    "difficulty": "medium",
    "time_complexity": "O(log S) for get, O(1) for set and snap",
    "space_complexity": "O(N + S)",
    "description": "Design a data structure that supports setting values, taking snapshots, and retrieving values at specific snapshot IDs.",
}

import bisect

class SnapshotArray:
    def __init__(self, length: int):
        """
        Initializes the SnapshotArray with a given length.
        
        Args:
            length (int): The size of the array.
        """
        # Each index in the array stores a list of [snap_id, value] pairs.
        # We initialize each index with snap_id 0 and value 0.
        self.history: list[list[list[int]]] = [[[0, 0]] for _ in range(length)]
        self.current_snap_id: int = 0

    def set(self, index: int, val: int) -> None:
        """
        Sets the value of the array at a specific index.
        
        Args:
            index (int): The index to set.
            val (int): The value to set.
        """
        # If the last recorded snap_id for this index is the current snap_id,
        # we simply update the value to avoid duplicate snap_id entries.
        if self.history[index][-1][0] == self.current_snap_id:
            self.history[index][-1][1] = val
        else:
            self.history[index].append([self.current_snap_id, val])

    def snap(self) -> int:
        """
        Takes a snapshot of the array.
        
        Returns:
            int: The ID of the snapshot just taken.
        """
        self.current_snap_id += 1
        return self.current_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        """
        Returns the value at a specific index at a specific snapshot ID.
        
        Args:
            index (int): The index to retrieve.
            snap_id (int): The snapshot ID to retrieve from.
            
        Returns:
            int: The value at the given index and snapshot ID.
            
        Examples:
            >>> obj = SnapshotArray(3)
            >>> obj.set(0, 5)
            >>> obj.snap()
            0
            >>> obj.get(0, 0)
            5
        """
        # We need to find the largest snap_id in history[index] such that snap_id <= target snap_id.
        # We use binary search (bisect_right) on the snap_ids stored in the history.
        # Since history[index] is a list of [snap_id, value], we search for the position
        # where [snap_id, float('inf')] would be inserted to find the rightmost valid entry.
        
        history_at_index = self.history[index]
        
        # bisect_right returns the insertion point which is one index higher than the target.
        # We search for [snap_id, float('inf')] to ensure we find the entry for the exact snap_id
        # or the entry immediately preceding it.
        idx = bisect.bisect_right(history_at_index, [snap_id, float('inf')])
        
        # The element at idx-1 is the one with the largest snap_id <= target snap_id.
        return history_at_index[idx - 1][1]

def solve():
    """
    Example usage of the SnapshotArray class.
    """
    # Example 1
    snap_array = SnapshotArray(3)
    snap_array.set(0, 5)
    snap_array.snap()
    snap_array.set(0, 6)
    print(f"Get index 0 at snap 0: {snap_array.get(0, 0)}")  # Expected: 5
    print(f"Get index 0 at snap 1: {snap_array.get(0, 1)}")  # Expected: 6
