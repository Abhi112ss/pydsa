METADATA = {
    "id": 398,
    "name": "Random Pick Index",
    "slug": "random-pick-index",
    "category": "Random",
    "aliases": [],
    "tags": ["reservoir_sampling", "randomized"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given an array of integers and a target, return a random index of the target using a single pass.",
}

import random

class Solution:
    def pickIndex(self, nums: list[int], target: int) -> int:
        """
        Selects a random index of the target value using Reservoir Sampling.

        This algorithm ensures that each occurrence of the target has an equal 
        probability of being selected while only requiring a single pass 
        through the array and constant extra space.

        Args:
            nums: A list of integers.
            target: The integer value to search for and pick an index from.

        Returns:
            An integer representing a random index where nums[index] == target.
            Returns -1 if the target is not found (though problem constraints 
            usually guarantee existence).

        Examples:
            >>> sol = Solution()
            >>> sol.pickIndex([1, 2, 3, 3, 3], 3)
            # Returns 2, 3, or 4 with equal probability
        """
        result_index = -1
        count = 0

        for current_index, value in enumerate(nums):
            if value == target:
                count += 1
                # Reservoir Sampling:
                # For the k-th occurrence of the target, we pick it with 
                # probability 1/k. This ensures that after processing 
                # the whole array, every occurrence has a 1/N probability.
                if random.randint(1, count) == 1:
                    result_index = current_index

        return result_index

def solve():
    """
    Example driver function to demonstrate the solution.
    """
    solution = Solution()
    nums = [1, 2, 3, 3, 3]
    target = 3
    
    # Run multiple times to observe distribution
    results = []
    for _ in range(1000):
        results.append(solution.pickIndex(nums, target))
    
    print(f"Target: {target}")
    print(f"Indices found: {results}")
    print(f"Counts: { {i: results.count(i) for i in [2, 3, 4]} }")
