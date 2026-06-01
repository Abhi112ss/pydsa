METADATA = {
    "id": 1643,
    "name": "Kth Smallest Instructions",
    "slug": "kth-smallest-instructions",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "combinatorics"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the kth lexicographically smallest permutation of a sequence based on specific combinatorial constraints.",
}

import math

def solve(n: int, k: int) -> list[int]:
    """
    Finds the kth lexicographically smallest permutation of numbers from 1 to n.
    
    Note: The problem description provided in the prompt implies a combinatorial 
    search for the kth permutation. Standard LeetCode #1643 is actually 
    'Kth Smallest Instructions' which is a different problem, but following 
    the provided 'Key insight' regarding combinatorics and factorials.

    Args:
        n: The number of elements in the sequence.
        k: The rank of the permutation to find (1-indexed).

    Returns:
        A list of integers representing the kth lexicographically smallest permutation.

    Examples:
        >>> solve(3, 1)
        [1, 2, 3]
        >>> solve(3, 3)
        [2, 1, 3]
    """
    # The problem asks for the kth lexicographical permutation of [1, 2, ..., n]
    # We use the factoradic number system approach.
    
    numbers = list(range(1, n + 1))
    permutation = []
    
    # Convert k to 0-indexed for easier calculation
    k -= 1
    
    # Precompute factorials to avoid repeated O(n) calculations
    # This ensures the overall complexity remains O(n)
    factorials = [1] * n
    for i in range(1, n):
        factorials[i] = factorials[i - 1] * i
        
    for i in range(n - 1, -1, -1):
        # Determine how many permutations exist for the remaining (i) elements
        # The index of the current element is k // (i!)
        idx = k // factorials[i]
        k %= factorials[i]
        
        # Append the selected number and remove it from the available pool
        permutation.append(numbers.pop(idx))
        
    return permutation
