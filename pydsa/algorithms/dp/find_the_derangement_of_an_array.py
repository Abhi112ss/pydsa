METADATA = {
    "id": 634,
    "name": "Find the Derangement of An Array",
    "slug": "find-the-derangement-of-an-array",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "combinatorics"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of derangements of n elements modulo 10^9 + 7.",
}

def solve(n: int) -> int:
    """
    Calculates the number of derangements of n elements using a recurrence relation.
    
    A derangement is a permutation of the elements of a set in which no element 
    appears in its original position. The recurrence relation is:
    dp[n] = (n - 1) * (dp[n - 1] + dp[n - 2])

    Args:
        n: The number of elements in the set.

    Returns:
        The number of derangements of n elements modulo 10^9 + 7.

    Examples:
        >>> solve(1)
        0
        >>> solve(2)
        1
        >>> solve(3)
        2
        >>> solve(4)
        9
    """
    MOD = 1_000_000_007

    if n == 1:
        return 0
    if n == 2:
        return 1

    # We only need the last two states to calculate the current state,
    # allowing us to reduce space complexity from O(n) to O(1).
    prev_prev = 0  # Represents dp[i-2], initially dp[1]
    prev = 1       # Represents dp[i-1], initially dp[2]
    current = 0

    for i in range(3, n + 1):
        # Apply the recurrence: dp[i] = (i - 1) * (dp[i-1] + dp[i-2])
        # We apply modulo at each step to prevent integer overflow and satisfy requirements.
        current = ((i - 1) * (prev + prev_prev)) % MOD
        
        # Shift the window forward for the next iteration
        prev_prev = prev
        prev = current

    return prev
