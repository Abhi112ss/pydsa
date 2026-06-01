METADATA = {
    "id": 2336,
    "name": "Smallest Number in Infinite Set",
    "slug": "smallest-number-in-infinite-set",
    "category": "Design",
    "aliases": [],
    "tags": ["heap", "set"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(n)",
    "description": "Design a data structure that manages an infinite set of positive integers and supports adding and removing elements.",
}

import heapq

class SmallestInfiniteSet:
    def __init__(self) -> None:
        """
        Initializes the object.
        """
        self.current_smallest_available = 1
        self.removed_elements_heap = []
        self.removed_elements_set = set()

    def add(self, num: int) -> None:
        """
        Adds the integer num to the infinite set.

        Args:
            num (int): The integer to add.
        """
        if num < self.current_smallest_available:
            if num in self.removed_elements_set:
                self.removed_elements_set.remove(num)
                heapq.heappop(self.removed_elements_heap)
                while self.removed_elements_heap and self.removed_elements_heap[0] in self.removed_elements_set:
                    heapq.heappop(self.removed_elements_heap)

    def remove(self, num: int) -> None:
        """
        Removes the integer num from the infinite set.

        Args:
            num (int): The integer to remove.
        """
        if num >= self.current_smallest_available:
            heapq.heappush(self.removed_elements_heap, num)
            self.removed_elements_set.add(num)
        else:
            if num in self.removed_elements_set:
                self.removed_elements_set.remove(num)
                # Note: We don't strictly need to pop from heap here because 
                # the heap logic in add() and getSmallest() handles it, 
                # but for consistency we manage the set.
                # However, to keep complexity optimal, we only pop when the top is invalid.

    def popSmallest(self) -> int:
        """
        Returns the smallest integer in the infinite set and removes it.

        Returns:
            int: The smallest integer in the set.
        """
        while self.removed_elements_heap and self.removed_elements_heap[0] not in self.removed_elements_set:
            heapq.heappop(self.removed_elements_heap)

        if self.removed_elements_heap:
            smallest = heapq.heappop(self.removed_elements_heap)
            self.removed_elements_set.remove(smallest)
            return smallest
        
        smallest = self.current_smallest_available
        self.current_smallest_available += 1
        return smallest

def solve():
    """
    This function is a placeholder to satisfy the requirement of a solve() function.
    In the context of LeetCode design problems, the class itself is the solution.

    Args:
        None

    Returns:
        None
    """
    pass