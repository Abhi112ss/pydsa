METADATA = {
    "id": 703,
    "name": "Kth Largest Element in a Stream",
    "slug": "kth_largest_element_in_a_stream",
    "category": "Design",
    "aliases": ["Kth Largest Element in a Stream"],
    "tags": ["heap", "min_heap", "design"],
    "difficulty": "easy",
    "time_complexity": "O(log k)",
    "space_complexity": "O(k)",
    "description": "Design a class to find the kth largest element in a stream of numbers.",
}

import heapq


class KthLargest:
    """A class to efficiently find the kth largest element in a stream of numbers.

    Uses a min-heap of size k to store the k largest elements encountered so far.
    The root of the min-heap is always the kth largest element.

    Args:
        k: The position of the largest element to find (1-indexed).
        nums: Initial list of numbers to populate the stream.

    Examples:
        >>> kth = KthLargest(3, [4, 5, 8, 2])
        >>> kth.add(3)
        4
        >>> kth.add(5)
        5
        >>> kth.add(10)
        5
        >>> kth.add(9)
        8
        >>> kth.add(4)
        8
    """

    def __init__(self, k: int, nums: list[int]) -> None:
        self.k = k
        self.min_heap = []
        # Initialize the min-heap with at most k elements from nums
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """Add a new value to the stream and return the kth largest element.

        Args:
            val: The new value to add to the stream.

        Returns:
            The kth largest element after adding the new value.

        Examples:
            >>> kth = KthLargest(3, [4, 5, 8, 2])
            >>> kth.add(3)
            4
            >>> kth.add(5)
            5
        """
        if len(self.min_heap) < self.k:
            # Heap not full yet, just push the new value
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            # New value is larger than current kth largest, replace the root
            heapq.heapreplace(self.min_heap, val)
        # The root of the min-heap is always the kth largest element
        return self.min_heap[0]


def solve(k: int, nums: list[int], additions: list[int]) -> list[int]:
    """Solve the Kth Largest Element in a Stream problem.

    Args:
        k: The position of the largest element to find (1-indexed).
        nums: Initial list of numbers to populate the stream.
        additions: List of values to add to the stream one by one.

    Returns:
        List of kth largest elements after each addition.

    Examples:
        >>> solve(3, [4, 5, 8, 2], [3, 5, 10, 9, 4])
        [4, 5, 5, 8, 8]
        >>> solve(1, [], [3, 5, 10])
        [3, 5, 10]
        >>> solve(2, [0], [-1])
        [-1, 0]
    """
    kth_largest = KthLargest(k, nums)
    results = []
    for val in additions:
        results.append(kth_largest.add(val))
    return results