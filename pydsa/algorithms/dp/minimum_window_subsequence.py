METADATA = {
    "id": 727,
    "name": "Minimum Window Subsequence",
    "slug": "minimum-window-subsequence",
    "category": "Hard",
    "aliases": [],
    "tags": ["dynamic_programming", "sliding_window", "two_pointers"],
    "difficulty": "hard",
    "time_complexity": "O(S * T)",
    "space_complexity": "O(T)",
    "description": "Find the minimum window in string S that contains T as a subsequence.",
}

def solve(s: str, t: str) -> str:
    """
    Finds the minimum window in string s that contains string t as a subsequence.

    The algorithm uses dynamic programming to track the latest possible starting 
    index in s for each prefix of t.

    Args:
        s: The source string.
        t: The target subsequence string.

    Returns:
        The shortest substring of s that contains t as a subsequence. 
        If no such window exists, returns an empty string.

    Examples:
        >>> solve("abcdebdde", "bde")
        'bcde'
        >>> solve("a", "b")
        ''
    """
    if not s or not t:
        return ""

    s_len = len(s)
    t_len = len(t)

    # dp[j] stores the maximum starting index in s such that 
    # t[0...j] is a subsequence of s[dp[j]...current_i]
    # We use -1 to represent that the prefix is not yet found.
    dp = [-1] * t_len

    min_len = float('inf')
    result_range = (-1, -1)

    for i in range(s_len):
        # If current character matches the first character of t, 
        # it's a potential start of a new window.
        if s[i] == t[0]:
            dp[0] = i

        # Iterate backwards through dp to update matches for t[1...t_len-1]
        # We go backwards to ensure we use the dp values from the previous i-1 state.
        for j in range(t_len - 1, 0, -1):
            if s[i] == t[j]:
                dp[j] = dp[j - 1]

        # If the last character of t is matched, we found a valid window.
        # dp[t_len - 1] gives the starting index of this window.
        if dp[t_len - 1] != -1:
            start_index = dp[t_len - 1]
            current_window_len = i - start_index + 1
            
            # Update the global minimum window found so far.
            if current_window_len < min_len:
                min_len = current_window_len
                result_range = (start_index, i)
            
            # Optimization: To find the *minimum* window ending at i, 
            # we could potentially shrink the window, but the DP approach 
            # with the 'latest start' logic naturally handles the subsequence constraint.

    if result_range == (-1, -1):
        return ""
    
    start, end = result_range
    return s[start : end + 1]
