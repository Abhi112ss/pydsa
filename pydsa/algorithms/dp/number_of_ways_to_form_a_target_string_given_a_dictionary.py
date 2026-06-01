METADATA = {
    "id": 1639,
    "name": "Number of Ways to Form a Target String Given a Dictionary",
    "slug": "number-of-ways-to-form-a-target-string-given-a-dictionary",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "hash_map", "combinatorics"],
    "difficulty": "hard",
    "time_complexity": "O(words_len + target_len * 26)",
    "space_complexity": "O(target_len + 26)",
    "description": "Calculate the number of ways to form a target string using characters from a dictionary of words, maintaining relative order.",
}

def solve(words: list[str], target: str) -> int:
    """
    Calculates the number of ways to form the target string using characters 
    from the given dictionary of words while maintaining the relative order 
    of characters in the words.

    Args:
        words: A list of strings representing the dictionary.
        target: The target string to form.

    Returns:
        The number of ways to form the target string modulo 10^9 + 7.

    Examples:
        >>> solve(["a", "b", "c"], "ab")
        1
        >>> solve(["abc", "def"], "abc")
        1
    """
    MOD = 10**9 + 7
    target_len = len(target)
    
    # Step 1: Precompute the frequency of each character at each column index.
    # Since we can only pick one character from each column, we count how many
    # times each character 'a'-'z' appears in each column across all words.
    num_columns = len(words[0])
    char_counts = [[0] * 26 for _ in range(num_columns)]
    
    for word in words:
        for col_idx, char in enumerate(word):
            char_counts[col_idx][ord(char) - ord('a')] += 1

    # Step 2: Dynamic Programming.
    # dp[i] represents the number of ways to form the prefix of target of length i.
    # We use a 1D DP array to optimize space from O(target_len * num_columns) to O(target_len).
    dp = [0] * (target_len + 1)
    dp[0] = 1  # Base case: 1 way to form an empty target prefix.

    # Iterate through each column of the dictionary words.
    for col in range(num_columns):
        # We iterate backwards through the DP array to ensure we use the 
        # results from the 'previous' column state, preventing using the 
        # same column multiple times for different characters of the target.
        for i in range(target_len - 1, -1, -1):
            target_char = target[i]
            char_idx = ord(target_char) - ord('a')
            count_in_col = char_counts[col][char_idx]
            
            if count_in_col > 0:
                # If the current column has the character we need for target[i],
                # the number of ways to form target[:i+1] increases by:
                # (ways to form target[:i]) * (occurrences of target[i] in this column)
                dp[i + 1] = (dp[i + 1] + dp[i] * count_in_col) % MOD

    return dp[target_len]
