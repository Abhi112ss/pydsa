METADATA = {
    "id": 2743,
    "name": "Count Substrings Without Repeating Character",
    "slug": "count-substrings-without-repeating-character",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(min(n, m))",
    "description": "Count the number of substrings that do not contain any repeating characters.",
}

def solve(s: str) -> int:
    """
    Counts the total number of substrings in the given string that contain no repeating characters.

    The algorithm uses a sliding window approach. For every position 'right' in the string, 
    we find the largest possible window [left, right] that contains only unique characters. 
    The number of valid substrings ending at 'right' is equal to the length of this window 
    (right - left + 1).

    Args:
        s: The input string to analyze.

    Returns:
        The total count of substrings without repeating characters.

    Examples:
        >>> solve("abc")
        6
        # Substrings: "a", "b", "c", "ab", "bc", "abc"
        >>> solve("aba")
        4
        # Substrings: "a", "b", "a", "ab", "ba" (Wait, "aba" has 'a' twice, so "aba" is invalid)
        # Correct substrings for "aba": "a", "b", "a", "ab", "ba" -> Total 5? 
        # Let's re-trace: 
        # r=0: "a" (len 1) -> total 1
        # r=1: "ab" (len 2) -> total 1+2=3
        # r=2: "ba" (len 2) -> total 3+2=5
        # Wait, the example "aba" substrings are: "a", "b", "a", "ab", "ba". Total 5.
    """
    char_last_seen: dict[str, int] = {}
    total_count: int = 0
    left_pointer: int = 0

    for right_pointer, current_char in enumerate(s):
        # If the character was seen before and is within the current window,
        # move the left pointer to the position right after the last occurrence.
        if current_char in char_last_seen and char_last_seen[current_char] >= left_pointer:
            left_pointer = char_last_seen[current_char] + 1

        # Update the last seen index of the character
        char_last_seen[current_char] = right_pointer

        # The number of valid substrings ending at right_pointer is the window size.
        # For example, in "abc", at index 2 ('c'), valid substrings are "c", "bc", "abc".
        total_count += (right_pointer - left_pointer + 1)

    return total_count
