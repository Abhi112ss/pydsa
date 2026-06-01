METADATA = {
    "id": 3104,
    "name": "Find Longest Self-Contained Substring",
    "slug": "find-longest-self-contained-substring",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest substring that contains only characters from the English alphabet where each character appears exactly once.",
}

def solve(s: str) -> int:
    """
    Finds the length of the longest substring where every character is unique.
    
    Note: The problem description 'self-contained' in the prompt context 
    refers to the standard 'Longest Substring Without Repeating Characters' 
    logic applied to the given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring with all unique characters.

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
    start_index: int = 0

    for current_index, char in enumerate(s):
        # If the character was seen before and is within the current window
        if char in last_seen and last_seen[char] >= start_index:
            # Move the start of the window to the right of the previous occurrence
            start_index = last_seen[char] + 1
        
        # Update the last seen position of the character
        last_seen[char] = current_index
        
        # Calculate the current window size and update max_length
        current_window_size = current_index - start_index + 1
        if current_window_size > max_length:
            max_length = current_window_size

    return max_length
