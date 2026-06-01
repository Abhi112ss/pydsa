METADATA = {
    "id": 139,
    "name": "Word Break",
    "slug": "word-break",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "hash_set", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(n)",
    "description": "Determine if a string can be segmented into a space-separated sequence of one or more dictionary words.",
}

def solve(s: str, word_dict: list[str]) -> bool:
    """
    Determines if the input string 's' can be segmented into words found in 'word_dict'.

    Args:
        s: The input string to be segmented.
        word_dict: A list of valid words.

    Returns:
        True if the string can be segmented, False otherwise.

    Examples:
        >>> solve("leetcode", ["leet", "code"])
        True
        >>> solve("applepenapple", ["apple", "pen"])
        True
        >>> solve("catsandog", ["cats", "dog", "sand", "and", "cat"])
        False
    """
    # Convert list to set for O(1) average lookup time
    word_set = set(word_dict)
    n = len(s)
    
    # dp[i] is True if the prefix s[0:i] can be segmented into words from the dictionary
    # We use size n + 1 to represent the empty string at index 0
    dp = [False] * (n + 1)
    
    # Base case: An empty string can always be "segmented"
    dp[0] = True
    
    # Iterate through every possible end position of a prefix
    for end in range(1, n + 1):
        # Check every possible split point before the current end position
        for start in range(end):
            # If the prefix up to 'start' is valid AND the substring from 
            # 'start' to 'end' exists in the dictionary, then s[0:end] is valid
            if dp[start] and s[start:end] in word_set:
                dp[end] = True
                # Once we find one valid segmentation for this prefix, we can stop
                break
                
    return dp[n]
