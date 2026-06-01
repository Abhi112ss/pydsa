METADATA = {
    "id": 1358,
    "name": "Number of Substrings Containing All Three Characters",
    "slug": "number-of-substrings-containing-all-three-characters",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings containing at least one occurrence of 'a', 'b', and 'c'.",
}

def solve(s: str) -> int:
    """
    Calculates the total number of substrings that contain at least one 'a', 'b', and 'c'.

    The algorithm uses a sliding window approach (or tracking last seen indices).
    For every index `i` acting as the end of a substring, if we know the last 
    seen positions of 'a', 'b', and 'c', the smallest of these positions 
    represents the rightmost starting point that completes a valid substring.
    Any starting point from index 0 to that minimum position will also form 
    a valid substring ending at `i`.

    Args:
        s: The input string consisting of characters 'a', 'b', and 'c'.

    Returns:
        The total count of substrings containing all three characters.

    Examples:
        >>> solve("abcabc")
        10
        >>> solve("aaabc")
        3
    """
    # Track the most recent index encountered for each required character
    last_seen = {"a": -1, "b": -1, "c": -1}
    total_substrings = 0
    
    for current_index, char in enumerate(s):
        # Update the last seen position of the current character
        last_seen[char] = current_index
        
        # The minimum of the last seen indices tells us the end of the 
        # prefix that contains all three characters.
        # For example, if last_seen is {'a': 2, 'b': 5, 'c': 4}, 
        # then any substring starting at index 0, 1, or 2 and ending 
        # at index 5 is valid.
        min_last_seen_index = min(last_seen.values())
        
        # If min_last_seen_index is -1, it means we haven't seen all 
        # three characters yet. Otherwise, there are (min_last_seen_index + 1)
        # valid substrings ending at the current index.
        if min_last_seen_index != -1:
            total_substrings += (min_last_seen_index + 1)
            
    return total_substrings
