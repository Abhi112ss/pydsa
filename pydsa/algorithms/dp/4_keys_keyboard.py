METADATA = {
    "id": 651,
    "name": "4 Keys Keyboard",
    "slug": "4-keys-keyboard",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of characters you can print on the screen using four keys: Ctrl-A, Ctrl-C, Ctrl-V, and a character key.",
}

def solve(n: int) -> int:
    """
    Calculates the maximum number of characters that can be printed on the screen
    using the four keys: 'A', 'Ctrl-A', 'Ctrl-C', and 'Ctrl-V'.

    Args:
        n: The total number of keystrokes allowed.

    Returns:
        The maximum number of 'A' characters that can be printed.

    Examples:
        >>> solve(1)
        1
        >>> solve(3)
        3
        >>> solve(7)
        10
    """
    if n <= 6:
        return n

    # dp[i] stores the maximum number of characters possible with i keystrokes.
    dp = [0] * (n + 1)

    # Base cases for small n where Ctrl-A, Ctrl-C, Ctrl-V sequence isn't optimal yet.
    for i in range(1, min(n + 1, 7)):
        dp[i] = i

    for i in range(7, n + 1):
        # The default option is to just press 'A' (incrementing from dp[i-1]).
        # However, for n > 6, the optimal strategy always involves a copy-paste sequence.
        # We look back at all possible points 'j' where we could have performed 
        # Ctrl-A, Ctrl-C, and then multiple Ctrl-V operations.
        
        # To perform a copy-paste:
        # 1. Ctrl-A (1 stroke)
        # 2. Ctrl-C (1 stroke)
        # 3. Ctrl-V (1 stroke)
        # Total 3 strokes to get the first paste.
        # Any subsequent Ctrl-V adds 1 stroke and adds the amount copied.
        
        # Let j be the number of keystrokes used before starting the Ctrl-A, Ctrl-C sequence.
        # The sequence is: Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V, ...
        # Total strokes used for the sequence: (i - j)
        # We need at least 3 strokes for the sequence (A, C, V) to be useful.
        # So, i - j >= 3 => j <= i - 3.
        
        # If we use (i - j) strokes for the sequence, we have:
        # 1 stroke for Ctrl-A
        # 1 stroke for Ctrl-C
        # (i - j - 2) strokes for Ctrl-V
        # The number of times we paste is (i - j - 2).
        # The total characters = dp[j] + (number of pastes) * dp[j]
        # Total characters = dp[j] * (1 + (i - j - 2)) = dp[j] * (i - j - 1)
        
        for j in range(i - 3, 0, -1):
            # We check if this specific j provides a better result.
            # Note: As j decreases, (i - j - 1) increases, but dp[j] decreases.
            # There is an optimal j that balances these.
            current_val = dp[j] * (i - j - 1)
            if current_val > dp[i]:
                dp[i] = current_val
            
            # Optimization: If dp[j] is too small, it won't beat our current dp[i].
            # However, for a standard O(n^2) DP, we iterate through all.
            
    return dp[n]
