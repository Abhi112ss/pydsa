METADATA = {
    "id": 395,
    "name": "Longest Substring with At Least K Repeating Characters",
    "slug": "longest-substring-with-at-least-k-repeating-characters",
    "category": "String",
    "aliases": [],
    "tags": ["divide_and_conquer", "recursion", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest substring where every character appears at least k times.",
}

def solve(s: str, k: int) -> int:
    """
    Finds the length of the longest substring where every character appears at least k times.

    Args:
        s: The input string.
        k: The minimum frequency required for each character in the substring.

    Returns:
        The length of the longest valid substring.

    Examples:
        >>> solve("aaabb", 3)
        3
        >>> solve("ababbc", 2)
        5
    """
    if len(s) < k:
        return 0

    # Count frequencies of all characters in the current string segment
    char_frequencies = {}
    for char in s:
        char_frequencies[char] = char_frequencies.get(char, 0) + 1

    # Identify characters that violate the 'at least k' rule
    # These characters cannot be part of any valid substring
    for char, count in char_frequencies.items():
        if count < k:
            # Split the string by this invalid character and solve for each segment
            # The longest valid substring must exist entirely within one of these segments
            max_length = 0
            for segment in s.split(char):
                max_length = max(max_length, solve(segment, k))
            return max_length

    # If no character violates the rule, the entire current string is valid
    return len(s)
