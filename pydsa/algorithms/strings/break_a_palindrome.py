METADATA = {
    "id": 1328,
    "name": "Break a Palindrome",
    "slug": "break-a-palindrome",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Replace exactly one character in a palindrome to make it the lexicographically smallest non-palindrome.",
}

def solve(palindrome: str) -> str:
    """
    Finds the lexicographically smallest non-palindrome by replacing exactly one character.

    Args:
        palindrome: A palindromic string of lowercase English letters.

    Returns:
        The lexicographically smallest non-palindrome string. 
        Returns an empty string if no such non-palindrome exists.

    Examples:
        >>> solve("abccba")
        'aaccba'
        >>> solve("a")
        ''
        >>> solve("aa")
        ''
    """
    n = len(palindrome)
    
    # If the string length is 1, any replacement results in a single character,
    # which is always a palindrome. Thus, no non-palindrome can be formed.
    if n <= 1:
        return ""

    # Convert to list because strings are immutable in Python
    chars = list(palindrome)

    # To get the lexicographically smallest string, we want to change the 
    # first character that is not 'a' to 'a'.
    # We only check the first half of the string because changing a character 
    # in the second half to 'a' would be less optimal or might maintain the palindrome.
    # Note: For odd lengths, the middle character cannot be changed to 'a' 
    # to break the palindrome if it's the only non-'a' because it's its own mirror.
    for i in range(n // 2):
        if chars[i] != 'a':
            chars[i] = 'a'
            return "".join(chars)

    # If we reach here, it means all characters in the first half (and thus the 
    # second half due to palindrome property) are 'a'.
    # To make it the smallest non-palindrome, we change the very last character to 'b'.
    # Example: "aaaa" -> "aaab"
    chars[n - 1] = 'b'
    return "".join(chars)
