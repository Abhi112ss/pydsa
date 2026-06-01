METADATA = {
    "id": 2080,
    "name": "Range Frequency Queries",
    "slug": "range-frequency-queries",
    "category": "Data Structures",
    "aliases": [],
    "tags": ["binary_search", "hash_map", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(Q log N)",
    "space_complexity": "O(N)",
    "description": "Find the frequency of a value within a given range [left, right] using an efficient lookup mechanism.",
}

import collections
import bisect

class RangeFreqQuery:
    """
    A class to handle range frequency queries efficiently.
    """

    def __init__(self, arr: list[int]):
        """
        Initializes the RangeFreqQuery object with an array.

        Args:
            arr (list[int]): The input array of integers.
        """
        # Map each value to a sorted list of indices where it appears
        self.value_to_indices = collections.defaultdict(list)
        for index, value in enumerate(arr):
            self.value_to_indices[value].append(index)

    def query(self, left: int, right: int, value: int) -> int:
        """
        Returns the frequency of 'value' in the range [left, right].

        Args:
            left (int): The starting index of the range (inclusive).
            right (int): The ending index of the range (inclusive).
            value (int): The value to count.

        Returns:
            int: The number of times 'value' appears in arr[left...right].

        Examples:
            >>> rfq = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
            >>> rfq.query(1, 2, 4)
            1
            >>> rfq.query(0, 20, 33)
            2
        """
        if value not in self.value_to_indices:
            return 0

        indices = self.value_to_indices[value]

        # Use binary search to find the range of indices that fall within [left, right]
        # bisect_left finds the first index >= left
        start_pos = bisect.bisect_left(indices, left)
        # bisect_right finds the first index > right
        end_pos = bisect.bisect_right(indices, right)

        # The number of elements in the range is the difference between the two positions
        return end_pos - start_pos

def solve():
    """
    Example usage of the RangeFreqQuery class.
    """
    arr = [12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]
    rfq = RangeFreqQuery(arr)
    
    # Test cases
    assert rfq.query(1, 2, 4) == 1
    assert rfq.query(0, 20, 33) == 2
    assert rfq.query(0, 11, 12) == 2
    print("All tests passed!")
