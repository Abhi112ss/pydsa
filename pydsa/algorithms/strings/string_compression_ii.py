METADATA = {
    "id": 1531,
    "name": "String Compression II",
    "slug": "string-compression-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "strings", "substring"],
    "difficulty": "hard",
    "time_complexity": "O(n^3 * k)",
    "space_complexity": "O(n^2 * k)",
    "description": "Find the minimum length of a compressed string after performing at most k character changes.",
}

def solve(s: str, k: int) -> int:
    """
    Finds the minimum length of the compressed string after at most k changes.

    Args:
        s: The input string consisting of lowercase English letters.
        k: The maximum number of character changes allowed.

    Returns:
        The minimum length of the compressed string.

    Examples:
        >>> solve("aaabaaa", 0)
        4
        >>> solve("aaabaaa", 2)
        3
    """
    n = len(s)
    # dp[i][j][rem_k] represents the minimum length of the compressed 
    # representation of substring s[i:j+1] with rem_k changes allowed.
    # Using a 3D array for memoization.
    memo: dict[tuple[int, int, int], int] = {}

    def get_compressed_len(char: str, count: int) -> int:
        """Calculates the length of a compressed segment of a specific character."""
        if count == 0:
            return 0
        if count == 1:
            return 1
        if count < 10:
            return 2  # e.g., 'a2'
        if count < 100:
            return 3  # e.g., 'a12'
        return 4      # e.g., 'a123' (max n is 100)

    def dp(i: int, j: int, rem_k: int) -> int:
        """Recursive DP with memoization to find min length for substring s[i:j+1]."""
        if i > j:
            return 0
        if i == j:
            return 1
        
        state = (i, j, rem_k)
        if state in memo:
            return memo[state]

        # Option 1: The current substring is treated as a single block of the same character.
        # We pick a character 'c' and try to change all other characters in s[i:j+1] to 'c'.
        # We must check if we have enough k to do this.
        res = float('inf')
        
        # To optimize, we only consider characters that actually exist in the substring
        # or we can just iterate through all 'a'-'z'. However, the optimal character 
        # to turn everything into must be one of the characters already present.
        unique_chars = set(s[i : j + 1])
        
        for char_to_use in unique_chars:
            changes_needed = 0
            for idx in range(i, j + 1):
                if s[idx] != char_to_use:
                    changes_needed += 1
            
            if changes_needed <= rem_k:
                res = min(res, get_compressed_len(char_to_use, j - i + 1))

        # Option 2: Split the substring into two parts at every possible index 'p'.
        # This covers cases where the compressed string has multiple different character blocks.
        for p in range(i, j):
            # We distribute the remaining k between the left and right partitions.
            # Since k is small (up to 100), we can iterate through all possible k_left.
            for k_left in range(rem_k + 1):
                res = min(res, dp(i, p, k_left) + dp(p + 1, j, rem_k - k_left))

        memo[state] = int(res)
        return int(res)

    # The problem asks for the minimum length of the whole string.
    # However, the standard DP approach for this problem is to define dp[i][j][k] 
    # as the min length of s[i...j] with k changes.
    # To avoid O(n^4) or higher, we use the split-point approach.
    
    # Re-implementing with a more efficient iterative or structured approach 
    # because the recursive split with k-distribution can be slow.
    # Let's use the standard DP: dp[i][j][k]
    
    dp_table = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(n)]

    for length in range(1, n + 1):  # length of substring
        for i in range(n - length + 1):
            j = i + length - 1
            
            for current_k in range(k + 1):
                # Base Case: Single character
                if i == j:
                    dp_table[i][j][current_k] = 1
                    continue

                # Case 1: Try making the entire substring s[i:j+1] the same character
                # We check every character 'a'-'z' that could be the target
                for char_code in range(ord('a'), ord('z') + 1):
                    target_char = chr(char_code)
                    needed = 0
                    for idx in range(i, j + 1):
                        if s[idx] != target_char:
                            needed += 1
                    
                    if needed <= current_k:
                        dp_table[i][j][current_k] = min(
                            dp_table[i][j][current_k], 
                            get_compressed_len(target_char, length)
                        )

                # Case 2: Split the substring into two parts
                for p in range(i, j):
                    for k_left in range(current_k + 1):
                        # The total length is the sum of lengths of two parts
                        val = dp_table[i][p][k_left] + dp_table[p + 1][j][current_k - k_left]
                        if val < dp_table[i][j][current_k]:
                            dp_table[i][j][current_k] = val

    return int(dp_table[0][n - 1][k])
