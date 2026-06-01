METADATA = {
    "id": 384,
    "name": "Shuffle an Array",
    "slug": "shuffle-an-array",
    "category": "Design",
    "aliases": [],
    "tags": ["randomized", "math"],
    "difficulty": "medium",
    "time_complexity": "O(1) per shuffle, O(n) initialization",
    "space_complexity": "O(n) to store the array",
    "description": "Implement a class that generates a random shuffle of an array using the Fisher-Yates algorithm.",
}

import random

class Solution:
    def __init__(self, nums: list[int]):
        """
        Initializes the object with the given array.

        Args:
            nums (list[int]): The initial array to be shuffled.
        """
        self.nums = nums

    def reset(self) -> list[int]:
        """
        Resets the array to its original configuration and returns it.

        Returns:
            list[int]: The original array.
        """
        # We need to store the original state to reset correctly.
        # Since the problem implies we modify the array in place during shuffle,
        # we should have kept a copy of the original.
        # However, for the sake of this implementation, we assume 'nums' 
        # passed in init is the source of truth.
        # To make this robust, we should have stored a copy in __init__.
        # Let's assume the user wants the original input back.
        # Note: In a real LeetCode environment, the test harness provides 
        # the original list, but we must maintain our own copy.
        pass

    # Re-implementing with proper state management for the class structure
    def __init__(self, nums: list[int]):
        self.original = list(nums)
        self.current = list(nums)

    def reset(self) -> list[int]:
        """
        Resets the array to its original configuration.

        Returns:
            list[int]: The original array.
        """
        self.current = list(self.original)
        return self.current

    def shuffle(self) -> list[int]:
        """
        Returns a random shuffling of the array.

        Returns:
            list[int]: The shuffled array.

        Examples:
            >>> sol = Solution([1, 2, 3])
            >>> sol.shuffle()
            [2, 1, 3] # (Example output, not deterministic)
            >>> sol.reset()
            [1, 2, 3]
        """
        n = len(self.current)
        # Fisher-Yates Shuffle Algorithm:
        # Iterate from the last element down to the first.
        for i in range(n - 1, 0, -1):
            # Pick a random index from 0 to i (inclusive)
            random_index = random.randint(0, i)
            
            # Swap the current element with the element at the random index
            self.current[i], self.current[random_index] = (
                self.current[random_index],
                self.current[i],
            )
            
        return self.current

def solve():
    """
    Example usage of the Solution class.
    """
    nums = [1, 2, 3]
    solution = Solution(nums)
    print(f"Original: {nums}")
    print(f"Shuffle 1: {solution.shuffle()}")
    print(f"Shuffle 2: {solution.shuffle()}")
    print(f"Reset: {solution.reset()}")
    print(f"Shuffle 3: {solution.shuffle()}")
