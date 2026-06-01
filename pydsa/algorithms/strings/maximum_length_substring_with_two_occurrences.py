METADATA = {
    "id": 3090,
    "name": "Maximum Length Substring With Two Occurrences",
    "slug": "maximum-length-substring-with-two-occurrences",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "strings", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum length of a substring where each character appears at most twice.",
}

def solve(s: str) -> int:
    """
    Finds the maximum length of a substring where no character appears more than twice.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The length of the longest substring satisfying the condition.

    Examples:
        >>> solve("aaabbb")
        4
        >>> solve("abcde")
        5
        >>> solve("aaaaa")
        2
    """
    char_frequency: dict[str, int] = {}
    max_length: int = 0
    left_pointer: int = 0

    # Iterate through the string using a right pointer to expand the window
    for right_pointer in range(len(s)):
        current_char = s[right_pointer]
        char_frequency[current_char] = char_frequency.get(current_char, 0) + 1

        # If the current character's count exceeds 2, shrink the window from the left
        # until the frequency of the current character is back to 2 or less.
        while char_frequency[current_char] > 2:
            left_char = s[left_pointer]
            char_frequency[left_char] -= 1
            left_pointer += 1

        # Calculate the current valid window size and update the global maximum
        current_window_size = right_pointer - left_pointer + 1
        if current_window_size > max_length:
            max_length = current_window_size

    return max_length
