METADATA = {
    "id": 3088,
    "name": "Make String Anti-palindrome",
    "slug": "make-string-anti-palindrome",
    "category": "Greedy",
    "aliases": [],
    "tags": ["strings", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine the minimum number of character changes needed to make a string an anti-palindrome.",
}

def solve(s: str) -> int:
    """
    Args:
        s: The input string to be transformed into an anti-palindrome.

    Returns:
        The minimum number of character changes required.
    """
    n = len(s)
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    max_freq = 0
    for count in char_counts.values():
        if count > max_freq:
            max_freq = count

    if max_freq > n // 2:
        return -1

    anti_palindrome_violations = 0
    for i in range(n // 2):
        if s[i] == s[n - 1 - i]:
            anti_palindrome_violations += 1

    return anti_palindrome_violations