METADATA = {
    "id": 3109,
    "name": "Find the Index of Permutation",
    "slug": "find-the-index-of-permutation",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the smallest index k such that the condition 'nums[i] % nums[k] == 0' holds for all i in [0, n-1].",
}

def solve(nums: list[int]) -> int:
    """
    Finds the smallest index k such that every element in the array is divisible by nums[k].

    Args:
        nums: A list of integers representing a permutation of numbers from 1 to n.

    Returns:
        The smallest index k such that nums[i] % nums[k] == 0 for all 0 <= i < len(nums).
        Since the array is a permutation of 1 to n, the answer is always the index 
        of the number 1.

    Examples:
        >>> solve([5, 2, 1, 3, 4])
        2
        >>> solve([1, 2, 3, 4, 5])
        0
    """
    # The problem asks for the smallest index k such that all elements are divisible by nums[k].
    # In a permutation of 1 to n, the only number that can divide all other numbers 
    # is the number 1. Any other number x > 1 will not divide numbers smaller than it.
    
    # Therefore, we simply need to find the index of the value 1.
    for index, value in enumerate(nums):
        if value == 1:
            return index
            
    # Based on problem constraints, 1 is always present in a permutation of 1 to n.
    return -1
