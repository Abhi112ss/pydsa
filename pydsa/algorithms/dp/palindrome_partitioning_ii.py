METADATA = {
    "id": 132,
    "name": "Palindrome Partitioning II",
    "slug": "palindrome_partitioning_ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "string"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum number of cuts needed for a palindrome partitioning of a given string.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of cuts needed such that every resulting 
    substring is a palindrome.

    Args:
        s: The input string to partition.

    Returns:
        The minimum number of cuts required.

    Examples:
        >>> solve("aab")
        1
        >>> solve("a")
        0
    """
    n = len(s)
    if n <= 1:
        return 0

    # is_palindrome[i][j] will be True if s[i:j+1] is a palindrome
    is_palindrome = [[False] * n for _ in range(n)]

    # Precompute all palindrome substrings using DP
    # A substring s[i:j] is a palindrome if s[i] == s[j] and 
    # (the inner substring s[i+1:j-1] is a palindrome or length <= 2)
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length <= 2:
                    is_palindrome[i][j] = True
                else:
                    is_palindrome[i][j] = is_palindrome[i + 1][j - 1]

    # min_cuts[i] stores the minimum cuts for the prefix s[0:i+1]
    min_cuts = [0] * n

    for i in range(n):
        # If the whole prefix s[0:i+1] is a palindrome, no cuts needed
        if is_palindrome[0][i]:
            min_cuts[i] = 0
        else:
            # Initialize with maximum possible cuts (cutting every character)
            min_cuts[i] = i
            # Try all possible cut positions j before i
            for j in range(i):
                # If s[j+1:i+1] is a palindrome, we can cut after index j
                if is_palindrome[j + 1][i]:
                    min_cuts[i] = min(min_cuts[i], min_cuts[j] + 1)

    return min_cuts[n - 1]
