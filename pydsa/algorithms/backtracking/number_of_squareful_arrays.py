METADATA = {
    "id": 996,
    "name": "Number of Squareful Arrays",
    "slug": "number-of-squareful-arrays",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "math", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(n!)",
    "space_complexity": "O(n)",
    "description": "Find the number of permutations of an array such that every pair of adjacent elements sums to a perfect square.",
}

import math
from collections import Counter

def solve(nums: list[int]) -> int:
    """
    Calculates the number of permutations where every adjacent pair sums to a perfect square.

    Args:
        nums: A list of integers.

    Returns:
        The total count of unique squareful permutations.

    Examples:
        >>> solve([1, 17, 8])
        2
        >>> solve([2, 2, 2])
        1
    """
    n = len(nums)
    if n == 0:
        return 0

    # Count frequencies to handle duplicate numbers and avoid duplicate permutations
    counts = Counter(nums)
    # Sort unique numbers to ensure consistent traversal
    unique_nums = sorted(counts.keys())
    
    def is_perfect_square(val: int) -> bool:
        if val < 0:
            return False
        root = int(math.isqrt(val))
        return root * root == val

    def backtrack(current_permutation: list[int]) -> int:
        # Base case: if the permutation is complete, we found one valid array
        if len(current_permutation) == n:
            return 1
        
        total_count = 0
        last_val = current_permutation[-1] if current_permutation else None

        for num in unique_nums:
            # If we have remaining instances of this number
            if counts[num] > 0:
                # Check if it's the first element or if the sum with the previous is a square
                if last_val is None or is_perfect_square(last_val + num):
                    # Choose
                    counts[num] -= 1
                    current_permutation.append(num)
                    
                    # Explore
                    total_count += backtrack(current_permutation)
                    
                    # Un-choose (backtrack)
                    current_permutation.pop()
                    counts[num] += 1
                    
        return total_count

    return backtrack([])
