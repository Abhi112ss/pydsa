METADATA = {
    "id": 3291,
    "name": "Minimum Number of Valid Strings to Form Target I",
    "slug": "minimum-number-of-valid-strings-to-form-target-i",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "string", "trie", "aho-corasick"],
    "difficulty": "hard",
    "time_complexity": "O(N * M)",
    "space_complexity": "O(N * M)",
    "description": "Find the minimum number of valid strings from a dictionary required to concatenate into a target string.",
}

def solve(target: str, words: list[str]) -> int:
    """
    Calculates the minimum number of valid strings needed to form the target string.

    Args:
        target: The target string to be formed.
        words: A list of valid strings that can be used.

    Returns:
        The minimum number of strings required, or -1 if it is impossible.

    Examples:
        >>> solve("leetcode", ["leet", "code"])
        2
        >>> solve("apple", ["app", "le"])
        2
        >>> solve("abc", ["a", "b"])
        -1
    """
    n = len(target)
    
    # Build a Trie to store all valid words for efficient prefix matching
    trie = {}
    for word in words:
        current_node = trie
        for char in word:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node["#"] = True  # Mark end of a valid word

    # dp[i] represents the minimum number of words to form target[i:]
    # Initialize with infinity. dp[n] is the base case (empty string).
    inf = float('inf')
    dp = [inf] * (n + 1)
    dp[n] = 0

    # Iterate backwards from the end of the target string
    for i in range(n - 1, -1, -1):
        current_node = trie
        # Traverse the Trie using the target string starting from index i
        for j in range(i, n):
            char = target[j]
            if char not in current_node:
                # No more words in the Trie match this prefix
                break
            
            current_node = current_node[char]
            
            # If we reached the end of a valid word in the Trie
            if "#" in current_node:
                # The cost to form target[i:] is 1 + cost to form target[j+1:]
                if dp[j + 1] != inf:
                    dp[i] = min(dp[i], 1 + dp[j + 1])
                    
    return dp[0] if dp[0] != inf else -1
