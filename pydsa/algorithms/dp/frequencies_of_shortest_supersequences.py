METADATA = {
    "id": 3435,
    "name": "Frequencies of Shortest Supersequences",
    "slug": "frequencies_of_shortest_supersequences",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "string", "shortest common supersequence"],
    "difficulty": "hard",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n * m)",
    "description": "Find the number of shortest supersequences of two strings modulo 10^9 + 7.",
}

def solve(word1: str, word2: str) -> int:
    """
    Calculates the number of shortest supersequences of two strings modulo 10^9 + 7.

    Args:
        word1: The first input string.
        word2: The second input string.

    Returns:
        The number of shortest supersequences modulo 10^9 + 7.

    Examples:
        >>> solve("ab", "ba")
        2
        >>> solve("abc", "def")
        6
    """
    MOD = 1_000_000_007
    n = len(word1)
    m = len(word2)

    # dp_len[i][j] stores the length of the shortest supersequence of word1[:i] and word2[:j]
    # dp_cnt[i][j] stores the number of ways to form that shortest supersequence
    dp_len = [[0] * (m + 1) for _ in range(n + 1)]
    dp_cnt = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: empty strings
    dp_cnt[0][0] = 1

    # Initialize boundaries (supersequence of string and empty string is the string itself)
    for i in range(1, n + 1):
        dp_len[i][0] = i
        dp_cnt[i][0] = 1
    for j in range(1, m + 1):
        dp_len[0][j] = j
        dp_cnt[0][j] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                # If characters match, they must be part of the supersequence together
                dp_len[i][j] = dp_len[i - 1][j - 1] + 1
                dp_cnt[i][j] = dp_cnt[i - 1][j - 1]
            else:
                # If characters don't match, we take the minimum length from either 
                # including word1[i-1] or word2[j-1]
                len_from_top = dp_len[i - 1][j] + 1
                len_from_left = dp_len[i][j - 1] + 1
                
                min_len = min(len_from_top, len_from_left)
                dp_len[i][j] = min_len
                
                ways = 0
                # If taking from top yields the minimum length, add those ways
                if len_from_top == min_len:
                    ways = (ways + dp_cnt[i - 1][j]) % MOD
                # If taking from left yields the minimum length, add those ways
                if len_from_left == min_len:
                    ways = (ways + dp_cnt[i][j - 1]) % MOD
                
                dp_cnt[i][j] = ways

    return dp_cnt[n][m]
