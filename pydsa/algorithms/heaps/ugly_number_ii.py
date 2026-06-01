METADATA = {
    "id": 264,
    "name": "Ugly Number II",
    "slug": "ugly-number-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "heap", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the n-th number whose prime factors are limited to 2, 3, and 5.",
}

def solve(n: int) -> int:
    """
    Finds the n-th ugly number using a dynamic programming approach with three pointers.

    An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
    The sequence starts: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ...

    Args:
        n: The index of the ugly number to retrieve (1-indexed).

    Returns:
        The n-th ugly number.

    Examples:
        >>> solve(10)
        12
        >>> solve(1)
        1
    """
    if n <= 0:
        return 0

    # dp array stores the sequence of ugly numbers in increasing order
    dp = [0] * n
    dp[0] = 1

    # Pointers for the next multiple of 2, 3, and 5
    # These indices track which previously found ugly number will be multiplied
    # by the respective prime factor to produce the next candidate.
    idx2 = 0
    idx3 = 0
    idx5 = 0

    for i in range(1, n):
        # Calculate the next potential candidates for the sequence
        next_multiple_of_2 = dp[idx2] * 2
        next_multiple_of_3 = dp[idx3] * 3
        next_multiple_of_5 = dp[idx5] * 5

        # The next ugly number is the minimum of the three candidates
        next_ugly = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        dp[i] = next_ugly

        # Increment the pointer(s) that produced the minimum value.
        # We use 'if' instead of 'elif' to handle duplicates (e.g., 2*3 and 3*2 both equal 6).
        if next_ugly == next_multiple_of_2:
            idx2 += 1
        if next_ugly == next_multiple_of_3:
            idx3 += 1
        if next_ugly == next_multiple_of_5:
            idx5 += 1

    return dp[n - 1]
