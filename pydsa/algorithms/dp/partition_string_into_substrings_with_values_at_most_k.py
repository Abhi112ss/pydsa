METADATA = {
    "id": 2522,
    "name": "Partition String Into Substrings With Values at Most K",
    "slug": "partition-string-into-substrings-with-values-at-most-k",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "string", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Partition a string into the minimum number of substrings such that the value of each substring does not exceed k.",
}

def solve(s: str, k: int) -> int:
    """
    Partitions the string into the minimum number of substrings where each 
    substring's value (sum of products of character positions) is at most k.

    The value of a substring is calculated as:
    sum_{i=0}^{len-1} (i + 1) * (ord(char) - ord('a') + 1)

    Args:
        s: The input string consisting of lowercase English letters.
        k: The maximum allowed value for any single substring.

    Returns:
        The minimum number of substrings required to partition the string.

    Examples:
        >>> solve("abc", 10)
        1
        >>> solve("abc", 5)
        2
    """
    n = len(s)
    # dp[i] represents the minimum number of substrings needed for the prefix s[0:i]
    # Initialize with infinity, except dp[0] = 0 (empty string needs 0 partitions)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        current_substring_value = 0
        # Try all possible starting positions 'j' for the last substring ending at 'i-1'
        # The substring is s[j:i]
        for j in range(i - 1, -1, -1):
            # Calculate the value of the substring s[j:i]
            # Note: The problem defines value based on the position WITHIN the substring.
            # However, it is easier to calculate the value of s[j:i] by iterating 
            # from the start of the substring to the end.
            
            # To maintain O(n^2), we recalculate the value of s[j:i] 
            # by treating j as the start and iterating forward, or 
            # more efficiently, we can iterate j backwards and build the value.
            # But the formula is: sum_{p=0}^{len-1} (p+1) * val(s[j+p])
            # This is tricky to update backwards. Let's use a forward approach for clarity.
            pass

    # Re-implementing the inner loop logic correctly for O(n^2)
    # We use dp[i] as the min partitions for s[0:i]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(n):
        # If the current prefix is unreachable, skip
        if dp[i] == float('inf'):
            continue
            
        current_substring_value = 0
        # Try to form a substring starting at index i and ending at index j
        for j in range(i, n):
            # char_val is the 1-indexed value of the character (a=1, b=2...)
            char_val = ord(s[j]) - ord('a') + 1
            # The position in the current substring is (j - i + 1)
            current_substring_value += (j - i + 1) * char_val
            
            # If the current substring exceeds k, any longer substring starting at i will also exceed k
            if current_substring_value > k:
                break
            
            # Update the DP state for the prefix ending at j + 1
            if dp[i] + 1 < dp[j + 1]:
                dp[j + 1] = dp[i] + 1
                
    return int(dp[n])
