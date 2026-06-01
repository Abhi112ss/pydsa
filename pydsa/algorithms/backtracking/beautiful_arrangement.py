METADATA = {
    "id": 526,
    "name": "Beautiful Arrangement",
    "slug": "beautiful-arrangement",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["recursion", "backtracking", "bitmask"],
    "difficulty": "medium",
    "time_complexity": "O(k) where k is the number of valid permutations",
    "space_complexity": "O(n) for the recursion stack",
    "description": "Count the number of beautiful arrangements that can be formed with numbers from 1 to n.",
}

def solve(n: int) -> int:
    """
    Calculates the number of beautiful arrangements for a given n.
    
    A beautiful arrangement is an arrangement of numbers 1 to n such that 
    for every position i (1-indexed), either:
    - The number at position i is divisible by i.
    - i is divisible by the number at position i.

    Args:
        n: The upper bound of the range of numbers [1, n].

    Returns:
        The total count of beautiful arrangements.

    Examples:
        >>> solve(2)
        2
        >>> solve(3)
        3
    """
    # used_mask tracks which numbers from 1 to n have been placed in the arrangement
    # We use a bitmask for efficient state tracking and potential memoization
    count = 0
    used_mask = 0

    def backtrack(index: int, mask: int) -> None:
        nonlocal count
        
        # Base case: If we have successfully placed all n numbers
        if index > n:
            count += 1
            return

        # Try placing every number from 1 to n in the current 'index' position
        for num in range(1, n + 1):
            # Check if the number 'num' has already been used using bitwise AND
            if not (mask & (1 << (num - 1))):
                # Check the 'beautiful' condition: 
                # num is divisible by index OR index is divisible by num
                if num % index == 0 or index % num == 0:
                    # Recurse to the next position, marking 'num' as used in the mask
                    backtrack(index + 1, mask | (1 << (num - 1)))

    # Start backtracking from the first position (index 1) with an empty mask
    backtrack(1, 0)
    return count
