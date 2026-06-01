METADATA = {
    "id": 295,
    "name": "Find Median from Data Stream",
    "slug": "find-median-from-data-stream",
    "category": "Design",
    "aliases": [],
    "tags": ["heap", "priority_queue", "design"],
    "difficulty": "hard",
    "time_complexity": "O(log n) per addNum, O(1) per findMedian",
    "space_complexity": "O(n)",
    "description": "Design a data structure that supports adding integers from a stream and finding the median of the elements seen so far.",
}

import heapq

class MedianFinder:
    def __init__(self) -> None:
        """
        Initializes the data structure with two heaps.
        
        We use a max-heap to store the smaller half of the numbers and 
        a min-heap to store the larger half. In Python, heapq is a min-heap,
        so we store negative values to simulate a max-heap.
        """
        # max_heap stores the smaller half of elements (using negative values)
        self.small_half_max_heap: list[int] = []
        # min_heap stores the larger half of elements
        self.large_half_min_heap: list[int] = []

    def addNum(self, num: int) -> None:
        """
        Adds a number into the data structure.

        Args:
            num (int): The integer to be added to the stream.
        """
        # Step 1: Add to max-heap (small half) first. 
        # We push to small_half, then pop the largest of small_half to large_half.
        # This ensures the new number is correctly categorized.
        heapq.heappush(self.small_half_max_heap, -num)
        
        # Move the largest element from small_half to large_half
        largest_of_small = -heapq.heappop(self.small_half_max_heap)
        heapq.heappush(self.large_half_min_heap, largest_of_small)

        # Step 2: Rebalance. 
        # We maintain the property that small_half can have at most 1 more element than large_half.
        # If large_half becomes larger, move one back to small_half.
        if len(self.large_half_min_heap) > len(self.small_half_max_heap):
            smallest_of_large = heapq.heappop(self.large_half_min_heap)
            heapq.heappush(self.small_half_max_heap, -smallest_of_large)

    def findMedian(self) -> float:
        """
        Returns the median of all elements seen so far.

        Returns:
            float: The median value.
        """
        # If small_half has more elements, the median is its top element.
        if len(self.small_half_max_heap) > len(self.large_half_min_heap):
            return float(-self.small_half_max_heap[0])
        
        # If sizes are equal, the median is the average of the tops of both heaps.
        return (-self.small_half_max_heap[0] + self.large_half_min_heap[0]) / 2.0

def solve() -> None:
    """
    Example usage of the MedianFinder class.
    """
    median_finder = MedianFinder()
    median_finder.addNum(1)
    median_finder.addNum(2)
    print(f"Median after [1, 2]: {median_finder.findMedian()}")  # Expected: 1.5
    median_finder.addNum(3)
    print(f"Median after [1, 2, 3]: {median_finder.findMedian()}")  # Expected: 2.0
