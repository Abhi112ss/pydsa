METADATA = {
    "id": 1745,
    "name": "Palindrome Partitioning IV",
    "slug": "palindrome-partitioning-iv",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "string", "palindrome"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Determine if a string can be partitioned into exactly three non-empty palindromic substrings.",
}

def solve(s: str) -> bool:
    """
    Determines if the string s can be partitioned into exactly three non-empty 
    palindromic substrings.

    Args:
        s: The input string to be partitioned.

    Returns:
        True if the string can be partitioned into three palindromes, False otherwise.

    Examples:
        >>> solve("aab")
        False
        >>> solve("abc")
        False
        >>> solve("aaa")
        True
    """
    n = len(s)
    if n < 3:
        return False

    # is_palindrome[i][j] will be True if s[i:j+1] is a palindrome
    is_palindrome = [[False] * n for _ in range(n)]

    # Precompute all palindromic substrings using DP in O(n^2)
    # Base cases: single characters and pairs
    for i in range(n):
        is_palindrome[i][i] = True
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    is_palindrome[i][j] = True
                else:
                    is_palindrome[i][j] = is_palindrome[i + 1][j - 1]

    # Try all possible split points for three non-empty substrings.
    # The first split point 'i' marks the end of the first substring (s[0...i]).
    # The second split point 'j' marks the end of the second substring (s[i+1...j]).
    # The third substring is s[j+1...n-1].
    # Constraints: 0 <= i < j < n-1
    for i in range(n - 2):
        if is_palindrome[0][i]:
            for j in range(i + 1, n - 1):
                # Check if the middle and the last parts are also palindromes
                if is_palindrome[i + 1][j] and is_palindrome[j + 1][n - 1]:
                    return True

    return False
