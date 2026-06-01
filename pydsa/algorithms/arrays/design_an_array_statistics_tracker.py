METADATA = {
    "id": 3369,
    "name": "Design an Array Statistics Tracker",
    "slug": "design-an-array-statistics-tracker",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "hash_map", "heap"],
    "difficulty": "hard",
    "time_complexity": "O(log n)",
    "space_complexity": "O(n)",
    "description": "Design a data structure that tracks the median and mode of a stream of integers.",
}

import heapq
from collections import Counter, defaultdict

class ArrayStatisticsTracker:
    """
    A data structure to track the median and mode of a stream of integers.
    
    The tracker maintains:
    - Median: Using two heaps (max-heap for the lower half, min-heap for the upper half).
    - Mode: Using a frequency map and a frequency-to-elements map to find the most frequent element.
    """

    def __init__(self) -> None:
        """Initializes the tracker with empty data structures."""
        # Median tracking: max_heap stores the smaller half, min_heap stores the larger half
        self.max_heap_lower: list[int] = []  # Stores negative values to simulate max-heap
        self.min_heap_upper: list[int] = []
        
        # Mode tracking
        self.counts: dict[int, int] = Counter()
        # freq_map maps frequency -> set of elements having that frequency
        self.freq_map: dict[int, set[int]] = defaultdict(set)
        self.max_freq: int = 0

    def add(self, num: int) -> None:
        """
        Adds a new integer to the tracker.

        Args:
            num: The integer to add.
        """
        # 1. Update Median Heaps
        # Push to max_heap first, then move largest of lower half to upper half
        heapq.heappush(self.max_heap_lower, -num)
        heapq.heappush(self.min_heap_upper, -heapq.heappop(self.max_heap_lower))
        
        # Rebalance: max_heap_lower can have at most 1 more element than min_heap_upper
        if len(self.min_heap_upper) > len(self.max_heap_lower):
            heapq.heappush(self.max_heap_lower, -heapq.heappop(self.min_heap_upper))
            
        # 2. Update Mode Tracking
        old_freq = self.counts[num]
        new_freq = old_freq + 1
        self.counts[num] = new_freq
        
        # Remove from old frequency set
        if old_freq > 0:
            self.freq_map[old_freq].remove(num)
            # If the old frequency set is empty and it was the max_freq, we don't strictly 
            # need to decrement max_freq here because the new_freq will always be >= old_freq
            
        # Add to new frequency set
        self.freq_map[new_freq].add(num)
        
        # Update global max frequency
        if new_freq > self.max_freq:
            self.max_freq = new_freq

    def get_median(self) -> float:
        """
        Returns the median of the elements added so far.

        Returns:
            The median as a float.
        """
        if len(self.max_heap_lower) > len(self.min_heap_upper):
            return float(-self.max_heap_lower[0])
        else:
            # Even number of elements: average of the two middle elements
            return (-self.max_heap_lower[0] + self.min_heap_upper[0]) / 2.0

    def get_mode(self) -> int:
        """
        Returns the most frequent element. If multiple exist, returns the smallest one.

        Returns:
            The mode as an integer.
        """
        # The problem requirement for ties (smallest element) is handled by 
        # picking min from the set of elements with max_freq.
        # Note: In a real production environment, we might want to optimize 
        # the tie-breaking if get_mode is called much more frequently than add.
        return min(self.freq_map[self.max_freq])

def solve() -> None:
    """
    Example usage of the ArrayStatisticsTracker.
    """
    tracker = ArrayStatisticsTracker()
    tracker.add(1)
    tracker.add(2)
    print(f"Median: {tracker.get_median()}") # Expected: 1.5
    print(f"Mode: {tracker.get_mode()}")     # Expected: 1 (or 2, depending on tie-break)
    tracker.add(2)
    print(f"Median: {tracker.get_median()}") # Expected: 2.0
    print(f"Mode: {tracker.get_mode()}")     # Expected: 2
