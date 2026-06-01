METADATA = {
    "id": 3167,
    "name": "Better Compression of String",
    "slug": "better-compression-of-string",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "strings", "interval dp"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum length of a compressed string representation where repeated characters can be represented as char + count.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum length of the compressed string.
    
    The compression rule allows representing a sequence of identical characters 
    as the character followed by its count (e.g., 'aaaaa' -> 'a5'). 
    Note: The problem context implies we want to find the minimum length 
    of the string after applying optimal compression rules.

    Args:
        s: The input string to compress.

    Returns:
        The minimum length of the compressed string.

    Examples:
        >>> solve("aaaaa")
        2
        >>> solve("abcde")
        5
        >>> solve("aaabbb")
        4
    """
    n = len(s)
    if n == 0:
        return 0

    # dp[i][j] will store the minimum length of the compressed string for substring s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters have length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate over substring lengths from 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Option 1: Treat the substring as a split of two parts
            # Initialize with the worst case (splitting at i)
            min_len = float('inf')
            for k in range(i, j):
                min_len = min(min_len, dp[i][k] + dp[k + 1][j])
            
            # Option 2: If the entire substring consists of the same character,
            # we can compress it as 'char' + 'count_string'.
            # However, the standard LeetCode version of this problem (like 467) 
            # usually involves a specific compression rule. 
            # For "Better Compression", we check if s[i...j] is all the same char.
            is_uniform = True
            for idx in range(i + 1, j + 1):
                if s[idx] != s[i]:
                    is_uniform = False
                    break
            
            if is_uniform:
                # Length is 1 (for char) + length of the string representation of the count
                # e.g., 'aaaaa' (5) -> 'a' + '5' -> length 2
                count_len = len(str(length))
                min_len = min(min_len, 1 + count_len)
            
            # Special case for compression: if the substring can be formed by 
            # repeating a smaller pattern. This is the core of interval DP.
            # But for the specific "char + count" rule, we check if s[i...j] 
            # can be compressed by looking at the character counts.
            
            # Check if the substring is a repetition of a smaller block
            # This handles cases like "ababab" -> "ab3" (if the rule allows pattern compression)
            # Given the prompt "char + count", we focus on character runs.
            
            # Refined logic for "char + count" compression:
            # If s[i...j] is all same char, length is 1 + len(str(j-i+1))
            # Otherwise, we must split.
            
            dp[i][j] = int(min_len)

    # Note: The logic above follows the standard Interval DP pattern.
    # For the specific problem 3167 (if it follows the 'a5' pattern):
    # We need to ensure we handle the case where a character run is split.
    
    # Re-calculating with a more robust approach for character runs:
    # dp[i][j] = min length of s[i...j]
    dp = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
        
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Standard split
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
            
            # Check if s[i...j] is a single character run
            all_same = True
            for k in range(i + 1, j + 1):
                if s[k] != s[i]:
                    all_same = False
                    break
            if all_same:
                dp[i][j] = min(dp[i][j], 1 + len(str(length)))
                
    return int(dp[0][n-1])
