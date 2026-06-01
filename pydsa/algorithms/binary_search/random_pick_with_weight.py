METADATA = {
    "id": 528,
    "name": "Random Pick with Weight",
    "slug": "random-pick-with-weight",
    "category": "Design",
    "aliases": [],
    "tags": ["prefix_sum", "randomization", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(log n) per pick",
    "space_complexity": "O(n)",
    "description": "Design a class that picks an index from an array of weights with probability proportional to the weights.",
}

import random
import bisect

class Solution:
    def __init__(self, w: list[int]):
        """
        Initializes the WeightedRandomPicker with a list of weights.

        Args:
            w: A list of positive integers representing the weights.
        """
        self.prefix_sums = []
        current_total = 0
        
        # Build a prefix sum array where each element represents 
        # the upper bound of the range for that index.
        for weight in w:
            current_total += weight
            self.prefix_sums.append(current_total)
        
        self.total_sum = current_total

    def pickIndex(self) -> int:
        """
        Picks an index based on the provided weights.

        Returns:
            An integer index picked with probability proportional to its weight.

        Examples:
            >>> sol = Solution([1, 3])
            >>> # Probabilities: index 0 (1/4), index 1 (3/4)
            >>> sol.pickIndex()
        """
        # Generate a random number in the range [1, total_sum]
        # We use random.randint which is inclusive of both endpoints.
        target = random.randint(1, self.total_sum)
        
        # Use binary search to find the first prefix sum that is 
        # greater than or equal to our target.
        # bisect_left returns the leftmost insertion point to maintain order.
        return bisect.bisect_left(self.prefix_sums, target)

def solve():
    """
    Example usage of the Solution class.
    """
    weights = [1, 3]
    picker = Solution(weights)
    
    # Test the distribution
    results = {0: 0, 1: 0}
    for _ in range(10000):
        idx = picker.pickIndex()
        results[idx] += 1
    
    print(f"Results after 10,000 picks: {results}")
    # Expected: index 0 ~ 2500, index 1 ~ 7500
