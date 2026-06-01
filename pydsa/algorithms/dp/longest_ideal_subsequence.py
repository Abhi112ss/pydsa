METADATA = {
    "id": 2370,
    "name": "Longest Ideal Subsequence",
    "slug": "longest-ideal-subsequence",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest subsequence where the absolute difference between the alphabet positions of adjacent characters is at most k.",
}

def solve(s: str, k: int) -> int:
    """
    Calculates the length of the longest ideal subsequence in a given string.

    An ideal subsequence is one where the absolute difference between the 
    alphabetical positions of every two adjacent characters in the subsequence 
    is at most k.

    Args:
        s: The input string consisting of lowercase English letters.
        k: The maximum allowed absolute difference between adjacent characters.

    Returns:
        The length of the longest ideal subsequence.

    Examples:
        >>> solve("acfgbd", 2)
        4
        >>> solve("a", 0)
        1
    """
    # dp[i] stores the length of the longest ideal subsequence ending with 
    # the character corresponding to index i (0 for 'a', 25 for 'z').
    # Since the alphabet size is fixed at 26, space complexity is O(1).
    dp = [0] * 26

    for char in s:
        current_idx = ord(char) - ord('a')
        
        # Determine the range of valid preceding characters [current - k, current + k]
        # We must stay within the bounds [0, 25].
        start_range = max(0, current_idx - k)
        end_range = min(25, current_idx + k)
        
        # Find the maximum length among all valid preceding characters
        max_prev_length = 0
        for prev_idx in range(start_range, end_range + 1):
            if dp[prev_idx] > max_prev_length:
                max_prev_length = dp[prev_idx]
        
        # Update the DP table for the current character
        # The new length is the best previous length + 1 (the current character)
        dp[current_idx] = max_prev_length + 1

    # The answer is the maximum value found in our DP table
    return max(dp)
