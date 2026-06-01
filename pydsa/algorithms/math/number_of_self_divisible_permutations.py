METADATA = {
    "id": 2992,
    "name": "Number of Self-Divisible Permutations",
    "slug": "number-of-self-divisible-permutations",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "math", "permutations"],
    "difficulty": "medium",
    "time_complexity": "O(n!)",
    "space_complexity": "O(n)",
    "description": "Count the number of permutations of numbers from 1 to n such that each number at index i is divisible by i + 1.",
}

def solve(n: int) -> int:
    """
    Calculates the number of permutations of [1, ..., n] where each element 
    at index i is divisible by (i + 1).

    Args:
        n: The upper bound of the range [1, n].

    Returns:
        The total count of valid self-divisible permutations.

    Examples:
        >>> solve(3)
        2
        >>> solve(1)
        1
    """
    # used[i] tracks if the number i has been placed in the current permutation
    used = [False] * (n + 1)
    count = 0

    def backtrack(index: int) -> None:
        nonlocal count
        
        # Base case: if we have successfully placed n numbers, we found a valid permutation
        if index > n:
            count += 1
            return

        # Try placing every available number from 1 to n at the current position
        for num in range(1, n + 1):
            # Check if number is available and satisfies the divisibility rule:
            # The number at position 'index' must be divisible by 'index'
            if not used[num] and num % index == 0:
                used[num] = True
                backtrack(index + 1)
                # Backtrack: reset the state for the next iteration
                used[num] = False

    # Start backtracking from the first position (index 1)
    backtrack(1)
    return count
