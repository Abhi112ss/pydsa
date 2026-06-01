METADATA = {
    "id": 2730,
    "name": "Find the Longest Semi-Repetitive Substring",
    "slug": "find-the-longest-semi-repetitive-substring",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest substring that contains at most one pair of adjacent equal characters.",
}

def solve(s: str) -> int:
    """
    Finds the length of the longest semi-repetitive substring.
    A semi-repetitive substring is a substring that contains at most one 
    pair of adjacent equal characters.

    Args:
        s: The input string.

    Returns:
        The length of the longest semi-repetitive substring.

    Examples:
        >>> solve("522333")
        4
        >>> solve("11111")
        2
        >>> solve("12345")
        5
    """
    n = len(s)
    if n <= 2:
        return n

    max_length = 0
    left = 0
    # last_duplicate_index stores the index of the most recent pair of adjacent identical characters.
    # We initialize it to -1 to indicate no duplicate pair has been found yet.
    last_duplicate_index = -1

    for right in range(1, n):
        # Check if the current character forms an adjacent duplicate with the previous one
        if s[right] == s[right - 1]:
            # If we already encountered a duplicate pair, we must shrink the window.
            # The new left boundary must start after the first character of the previous duplicate pair.
            if last_duplicate_index != -1:
                left = last_duplicate_index + 1
            
            # Update the index of the most recent duplicate pair found.
            # We store the index of the first character of the pair (right - 1).
            last_duplicate_index = right - 1

        # Calculate the current valid window size
        current_window_size = right - left + 1
        if current_window_size > max_length:
            max_length = current_window_size

    return max_length
