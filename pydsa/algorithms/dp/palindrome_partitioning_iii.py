METADATA = {
    "id": 1278,
    "name": "Palindrome Partitioning III",
    "slug": "palindrome-partitioning-iii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "string_manipulation"],
    "difficulty": "hard",
    "time_complexity": "O(k * n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum number of characters to change to partition a string into k palindromic substrings.",
}

def solve(s: str, k: int) -> int:
    """
    Finds the minimum number of characters to change to partition the string into k palindromes.

    Args:
        s: The input string.
        k: The number of partitions required.

    Returns:
        The minimum number of character changes needed.

    Examples:
        >>> solve("aab", 2)
        0
        >>> solve("aab", 3)
        0
        >>> solve("abacaba", 3)
        0
        >>> solve("abcd", 2)
        1
    """
    n = len(s)

    # cost[i][j] will store the minimum changes to make s[i:j+1] a palindrome
    cost = [[0] * n for _ in range(n)]

    # Precompute costs for all possible substrings using a gap-based approach
    # A substring is a palindrome if s[i] == s[j] and s[i+1:j] is a palindrome
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                # If characters match, cost is same as the inner substring
                cost[i][j] = cost[i + 1][j - 1] if i + 1 <= j - 1 else 0
            else:
                # If characters don't match, we must change one, plus inner cost
                cost[i][j] = (cost[i + 1][j - 1] if i + 1 <= j - 1 else 0) + 1

    # dp[i][p] is the min cost to partition s[0:i] into p palindromes
    # Initialize with a large value (infinity)
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    
    # Base case: 0 characters partitioned into 0 groups costs 0
    dp[0][0] = 0

    # Fill DP table
    for p in range(1, k + 1):
        # We need at least p characters to make p partitions (assuming non-empty)
        # However, the problem allows empty partitions if we consider the logic, 
        # but standard partitioning implies non-empty substrings.
        for i in range(1, n + 1):
            # Try all possible split points 'j' for the last partition
            # The last partition will be s[j:i] (0-indexed in string, 1-indexed in dp)
            # j must be at least p-1 to allow previous p-1 partitions to have at least 1 char
            for j in range(p - 1, i):
                # dp[j][p-1] is cost of previous p-1 partitions
                # cost[j][i-1] is cost to make the current substring s[j:i] a palindrome
                current_cost = dp[j][p - 1] + cost[j][i - 1]
                if current_cost < dp[i][p]:
                    dp[i][p] = current_cost

    return int(dp[n][k])
