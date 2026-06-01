METADATA = {
    "id": 480,
    "name": "Sliding Window Median",
    "slug": "sliding-window-median",
    "category": "Hard",
    "aliases": [],
    "tags": ["sliding_window", "heap", "ordered_set"],
    "difficulty": "hard",
    "time_complexity": "O(n log k)",
    "space_complexity": "O(k)",
    "description": "Find the median of every sliding window of size k in an array.",
}

import heapq

class SlidingWindowMedianSolver:
    """
    A solver for the Sliding Window Median problem using two heaps and lazy removal.
    """

    def __init__(self):
        # Max-heap for the lower half (using negative values to simulate max-heap)
        self.small_heap: list[float] = []
        # Min-heap for the upper half
        self.large_heap: list[float] = []
        # Hash map to track elements that need to be removed (lazy removal)
        self.to_remove: dict[float, int] = {}
        # Track the number of valid elements in each heap
        self.small_size: int = 0
        self.large_size: int = 0

    def _clean_heap(self, heap: list[float], is_small_heap: bool) -> None:
        """
        Removes elements from the top of the heap if they are marked for deletion.
        """
        while heap:
            val = -heap[0] if is_small_heap else heap[0]
            if self.to_remove.get(val, 0) > 0:
                heapq.heappop(heap)
                self.to_remove[val] -= 1
            else:
                break

    def _rebalance(self) -> None:
        """
        Ensures the size difference between heaps is at most 1.
        """
        if self.small_size > self.large_size + 1:
            # Move from small to large
            val = -heapq.heappop(self.small_heap)
            self._clean_heap(self.small_heap, True)
            heapq.heappush(self.large_heap, val)
            self.small_size -= 1
            self.large_size += 1
        elif self.large_size > self.small_size:
            # Move from large to small
            val = heapq.heappop(self.large_heap)
            self._clean_heap(self.large_heap, False)
            heapq.heappush(self.small_heap, -val)
            self.large_size -= 1
            self.small_size += 1

    def add(self, num: float) -> None:
        """Adds a number to the heaps."""
        if not self.small_heap or num <= -self.small_heap[0]:
            heapq.heappush(self.small_heap, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large_heap, num)
            self.large_size += 1
        self._rebalance()

    def remove(self, num: float) -> None:
        """Marks a number for removal and updates sizes."""
        self.to_remove[num] = self.to_remove.get(num, 0) + 1
        if num <= -self.small_heap[0]:
            self.small_size -= 1
            if num == -self.small_heap[0]:
                self._clean_heap(self.small_heap, True)
        else:
            self.large_size -= 1
            if num == self.large_heap[0]:
                self._clean_heap(self.large_heap, False)
        self._rebalance()

    def get_median(self, k: int) -> float:
        """Returns the current median."""
        if k % 2 == 1:
            return float(-self.small_heap[0])
        else:
            return (-self.small_heap[0] + self.large_heap[0]) / 2.0

def solve(nums: list[int], k: int) -> list[float]:
    """
    Calculates the median for every sliding window of size k.

    Args:
        nums: A list of integers.
        k: The size of the sliding window.

    Returns:
        A list of floats representing the median of each window.

    Examples:
        >>> solve([1,3,-1,-3,5,3,6,7], 3)
        [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
        >>> solve([1], 1)
        [1.0]
    """
    if not nums or k == 0:
        return []

    solver = SlidingWindowMedianSolver()
    result = []

    # Initialize the first window
    for i in range(k):
        solver.add(nums[i])
    
    result.append(solver.get_median(k))

    # Slide the window across the array
    for i in range(k, len(nums)):
        # Remove the element that is sliding out of the window
        solver.remove(nums[i - k])
        # Add the new element sliding into the window
        solver.add(nums[i])
        # Append the current median
        result.append(solver.get_median(k))

    return result
