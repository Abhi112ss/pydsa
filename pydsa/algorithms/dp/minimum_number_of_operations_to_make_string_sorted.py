METADATA = {
    "id": 1830,
    "name": "Minimum Number of Operations to Make String Sorted",
    "slug": "minimum-number-of-operations-to-make-string-sorted",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of character changes to make a string non-decreasing.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of character changes required to make the string sorted.
    
    The problem is equivalent to finding the Longest Non-Decreasing Subsequence (LNDS).
    The minimum operations needed is the total length of the string minus the length 
    of the LNDS.

    Args:
        s: The input string to be sorted.

    Returns:
        The minimum number of operations (character replacements) to make the string sorted.

    Examples:
        >>> solve("abcd")
        0
        >>> solve("ba")
        1
        >>> solve("cba")
        2
    """
    n = len(s)
    if n <= 1:
        return 0

    # dp[i] will store the length of the Longest Non-Decreasing Subsequence 
    # ending at index i.
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            # If the character at j is less than or equal to character at i,
            # it can form a non-decreasing subsequence.
            if s[j] <= s[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in dp is the length of the longest non-decreasing subsequence.
    longest_non_decreasing_subsequence_length = max(dp)

    # Minimum operations = Total length - length of the characters we keep.
    return n - longest_non_decreasing_subsequence_length
