METADATA = {
    "id": 3144,
    "name": "Minimum Substring Partition of Equal Character Frequency",
    "slug": "minimum-substring-partition-of-equal-character-frequency",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["strings", "dynamic_programming", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Partition a string into the minimum number of substrings such that each substring has the same frequency for all characters present in that substring.",
}

def solve(s: str) -> int:
    """
    Finds the minimum number of substrings needed to partition the string such that 
    in each substring, all characters present in that substring appear with the same frequency.

    Args:
        s: The input string to partition.

    Returns:
        The minimum number of substrings required.

    Examples:
        >>> solve("aabb")
        1
        >>> solve("abc")
        1
        >>> solve("aabbcc")
        1
        >>> solve("aabbc")
        2
    """
    n = len(s)
    # dp[i] represents the minimum partitions for the prefix s[0:i]
    # Initialize with infinity, dp[0] = 0 (base case for empty string)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        # char_counts stores the frequency of each character in the current substring s[j:i]
        char_counts = {}
        
        # Iterate backwards to check all possible substrings ending at index i-1
        for j in range(i - 1, -1, -1):
            char = s[j]
            char_counts[char] = char_counts.get(char, 0) + 1
            
            # Check if all characters in the current substring have the same frequency
            # We extract the values (frequencies) and check if they are all equal
            frequencies = list(char_counts.values())
            
            # A substring is valid if all its character frequencies are identical
            # We use a set to check for uniqueness of frequency values
            is_valid = len(set(frequencies)) == 1
            
            if is_valid:
                # If valid, update dp[i] using the optimal solution for the prefix before this substring
                if dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
                    
    return int(dp[n])
