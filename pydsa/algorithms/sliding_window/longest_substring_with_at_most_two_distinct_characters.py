METADATA = {
    "id": 159,
    "name": "Longest Substring with At Most Two Distinct Characters",
    "slug": "longest-substring-with-at-most-two-distinct-characters",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest substring that contains at most two distinct characters.",
}

def solve(s: str) -> int:
    """
    Finds the length of the longest substring that contains at most two distinct characters.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring with at most two distinct characters.

    Examples:
        >>> solve("eceba")
        3
        >>> solve("ccaabbb")
        5
    """
    if not s:
        return 0

    # Dictionary to store the frequency of characters in the current window
    char_frequency: dict[str, int] = {}
    left_pointer: int = 0
    max_length: int = 0

    for right_pointer in range(len(s)):
        current_char = s[right_pointer]
        char_frequency[current_char] = char_frequency.get(current_char, 0) + 1

        # If we have more than 2 distinct characters, shrink the window from the left
        while len(char_frequency) > 2:
            left_char = s[left_pointer]
            char_frequency[left_char] -= 1
            
            # If frequency drops to zero, remove the character from the map to reduce distinct count
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            
            left_pointer += 1

        # Calculate the current window size and update the maximum length found
        current_window_size = right_pointer - left_pointer + 1
        if current_window_size > max_length:
            max_length = current_window_size

    return max_length
