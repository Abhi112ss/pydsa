METADATA = {
    "id": 3,
    "name": "Longest Substring Without Repeating Characters",
    "slug": "longest-substring-without-repeating-characters",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(min(m, n))",
    "description": "Find the length of the longest substring without repeating characters.",
}

def solve(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters 
    using a sliding window approach with a hash map.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring without repeating characters.

    Examples:
        >>> solve("abcabcbb")
        3
        >>> solve("bbbbb")
        1
        >>> solve("pwwkew")
        3
    """
    # last_seen maps a character to its most recent index in the string
    last_seen: dict[str, int] = {}
    max_length: int = 0
    # window_start marks the beginning of the current valid substring
    window_start: int = 0

    for window_end, char in enumerate(s):
        # If the character is already in our map and its index is within 
        # the current window, move the window start to the right of the 
        # previous occurrence to ensure all characters in window are unique.
        if char in last_seen and last_seen[char] >= window_start:
            window_start = last_seen[char] + 1

        # Update the last seen index of the current character
        last_seen[char] = window_end
        
        # Calculate the current window size and update max_length
        current_window_size = window_end - window_start + 1
        if current_window_size > max_length:
            max_length = current_window_size

    return max_length
