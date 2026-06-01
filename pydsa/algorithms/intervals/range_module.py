METADATA = {
    "id": 715,
    "name": "Range Module",
    "slug": "range-module",
    "category": "Design",
    "aliases": [],
    "tags": ["segment_tree", "ordered_set", "design"],
    "difficulty": "hard",
    "time_complexity": "O(log n)",
    "space_complexity": "O(n)",
    "description": "Design a data structure that tracks ranges of numbers and provides methods to add, remove, and query ranges.",
}

import bisect

class RangeModule:
    def __init__(self) -> None:
        self.starts = []
        self.ends = []

    def add_range(self, left: int, right: int) -> None:
        """
        Args:
            left (int): The start of the range.
            right (int): The end of the range.
        Returns:
            None
        """
        idx_start = bisect.bisect_left(self.ends, left)
        idx_end = bisect.bisect_right(self.starts, right)

        if idx_start < idx_end:
            new_left = min(left, self.starts[idx_start])
            new_right = max(right, self.ends[idx_end - 1])
            self.starts[idx_start:idx_end] = [new_left]
            self.ends[idx_start:idx_end] = [new_right]
        else:
            self.starts.insert(idx_start, left)
            self.ends.insert(idx_start, right)

    def remove_range(self, left: int, right: int) -> None:
        """
        Args:
            left (int): The start of the range.
            right (int): The end of the range.
        Returns:
            None
        """
        idx_start = bisect.bisect_left(self.ends, left)
        idx_end = bisect.bisect_right(self.starts, right)

        if idx_start >= idx_end:
            return

        first_start = self.starts[idx_start]
        last_end = self.ends[idx_end - 1]

        new_starts = []
        new_ends = []

        if first_start < left:
            new_starts.append(first_start)
            new_ends.append(left)

        if last_end > right:
            new_starts.append(right)
            new_ends.append(last_end)

        self.starts[idx_start:idx_end] = new_starts
        self.ends[idx_start:idx_end] = new_ends

    def query_range(self, left: int, right: int) -> bool:
        """
        Args:
            left (int): The start of the range.
            right (int): The end of the range.
        Returns:
            bool: True if the range is fully covered, False otherwise.
        """
        idx = bisect.bisect_left(self.ends, left)
        if idx < len(self.starts) and self.starts[idx] <= left and self.ends[idx] >= right:
            return True
        if idx < len(self.starts) and self.starts[idx] < left and self.ends[idx] >= right:
            return True
        
        idx_check = bisect.bisect_right(self.starts, left) - 1
        if idx_check >= 0 and self.starts[idx_check] <= left and self.ends[idx_check] >= right:
            return True
            
        return False

def solve():
    pass