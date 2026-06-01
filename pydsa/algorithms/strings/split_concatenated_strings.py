METADATA = {
    "id": 555,
    "name": "Split Concatenated Strings",
    "slug": "split_concatenated_strings",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Determine if a concatenated string can be split into two parts such that each part is a palindrome.",
}

def solve(s: str, words: list[str]) -> bool:
    """
    Determines if the string 's' can be split into two non-empty parts 
    where each part is a palindrome and both parts are formed by 
    concatenating elements from the 'words' list.

    Args:
        s: The concatenated string to check.
        words: A list of strings that were used to form 's'.

    Returns:
        True if 's' can be split into two palindromic substrings that are 
        both valid concatenations of words, False otherwise.

    Examples:
        >>> solve("racecarlevel", ["racecar", "level"])
        True
        >>> solve("abcba", ["abcba"])
        False
    """
    n = len(s)
    if n < 2:
        return False

    # Pre-calculate which prefixes and suffixes are valid concatenations of words
    # using dynamic programming.
    is_valid_prefix = [False] * (n + 1)
    is_valid_suffix = [False] * (n + 1)
    
    is_valid_prefix[0] = True
    for i in range(1, n + 1):
        for word in words:
            word_len = len(word)
            if i >= word_len and is_valid_prefix[i - word_len]:
                if s[i - word_len : i] == word:
                    is_valid_prefix[i] = True
                    break
                    
    is_valid_suffix[n] = True
    for i in range(n - 1, -1, -1):
        for word in words:
            word_len = len(word)
            if i + word_len <= n and is_valid_suffix[i + word_len]:
                if s[i : i + word_len] == word:
                    is_valid_suffix[i] = True
                    break

    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]

    # Iterate through every possible split point from index 1 to n-1
    # A split point 'i' means the first part is s[0:i] and the second is s[i:n]
    for i in range(1, n):
        # Check if the first part is a valid concatenation AND a palindrome
        # AND the second part is a valid concatenation AND a palindrome
        if is_valid_prefix[i] and is_valid_suffix[i]:
            if is_palindrome(s[0:i]) and is_palindrome(s[i:n]):
                return True

    return False
