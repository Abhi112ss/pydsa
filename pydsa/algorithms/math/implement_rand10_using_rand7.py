METADATA = {
    "id": 470,
    "name": "Implement Rand10() Using Rand7()",
    "slug": "implement-rand10-using-rand7",
    "category": "Math",
    "aliases": [],
    "tags": ["random", "math", "rejection_sampling"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Implement a function that returns a random integer from 1 to 10 using only a function that returns a random integer from 1 to 7.",
}

class Rand7:
    """
    A mock class representing the provided Rand7() interface.
    In a real LeetCode environment, this is provided by the system.
    """
    def rand7(self) -> int:
        import random
        return random.randint(1, 7)

class Solution:
    def rand10(self, rand7: Rand7) -> int:
        """
        Implements rand10() using rejection sampling on a 2D grid.

        The algorithm maps the outcomes of two rand7() calls to a 7x7 grid (49 outcomes).
        We use the first 40 outcomes (4 rows of 10) to ensure each number 1-10 
        has an equal probability of 4/49. If the outcome falls in the remaining 
        9 outcomes (41-49), we reject and try again.

        Args:
            rand7: An instance of a class providing a rand7() method.

        Returns:
            A random integer between 1 and 10 inclusive.

        Examples:
            >>> sol = Solution()
            >>> sol.rand10(Rand7())
            7
        """
        while True:
            # Generate a unique number from 1 to 49 using two calls to rand7.
            # Formula: (row - 1) * 7 + col
            row = rand7.rand7()
            col = rand7.rand7()
            
            # Map the 2D coordinate to a 1D range [1, 49]
            index = (row - 1) * 7 + col
            
            # Rejection Sampling:
            # We want to pick a number from 1 to 10. 
            # Since 49 is not divisible by 10, we take the largest multiple of 10 
            # less than or equal to 49, which is 40.
            # This ensures each number 1-10 has exactly 4 chances out of 49.
            if index <= 40:
                return (index - 1) % 10 + 1
