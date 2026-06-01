METADATA = {
    "id": 1576,
    "name": "Replace All ?'s to Avoid Consecutive Repeating Characters",
    "slug": "replace-all-qs-to-avoid-consecutive-repeating-characters",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Replace all question marks in a string with lowercase English letters such that no two adjacent characters are the same.",
}

def solve(s: str) -> str:
    """
    Replaces all '?' characters in a string with lowercase English letters 
    to ensure no two adjacent characters are identical.

    Args:
        s: The input string containing lowercase letters and '?'.

    Returns:
        The modified string with all '?' replaced.

    Examples:
        >>> solve("a?b")
        'aab' -> Wait, 'aab' is wrong. Correct logic: 'acb' or 'aab' is invalid.
        Actually, 'a?b' -> 'acb' (if 'a' and 'b' are neighbors).
        Example 1: "a?b" -> "acb"
        Example 2: "????" -> "abcd"
    """
    # Convert string to list for mutability
    chars = list(s)
    n = len(chars)
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(n):
        if chars[i] == '?':
            # Determine the characters to avoid (left and right neighbors)
            prev_char = chars[i - 1] if i > 0 else None
            next_char = chars[i + 1] if i < n - 1 else None

            # Greedy approach: Pick the first character from 'a'-'z' 
            # that is not equal to the previous or the next character.
            for char in alphabet:
                if char != prev_char and char != next_char:
                    chars[i] = char
                    break
                    
    return "".join(chars)
