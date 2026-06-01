METADATA = {
    "id": 3399,
    "name": "Smallest Substring With Identical Characters II",
    "slug": "smallest-substring-with-identical-characters-ii",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the smallest substring that contains at least k occurrences of at least one character.",
}

def solve(s: str, k: int) -> int:
    """
    Finds the length of the smallest substring that contains at least k 
    occurrences of at least one character.

    Args:
        s: The input string.
        k: The minimum required frequency of a single character.

    Returns:
        The length of the smallest substring meeting the criteria, 
        or -1 if no such substring exists.

    Examples:
        >>> solve("aaabb", 3)
        3
        >>> solve("abacaba", 3)
        7
        >>> solve("abcde", 2)
        -1
    """
    n = len(s)
    if k <= 1:
        return 1 if n > 0 else -1
    
    min_length = float('inf')
    
    # We iterate through each possible character 'a'-'z' that could be the 
    # character appearing k times. This keeps the space complexity O(1).
    # For each character, we use a sliding window to find the smallest 
    # window containing k instances of that specific character.
    
    # Optimization: Instead of 26 passes, we can do one pass with a frequency map,
    # but since we need the *smallest* window for *any* character, 
    # we track the indices of each character.
    
    char_indices: dict[str, list[int]] = {}
    for index, char in enumerate(s):
        if char not in char_indices:
            char_indices[char] = []
        char_indices[char].append(index)
    
    # For each character, the smallest window containing k occurrences 
    # will always start at some index i and end at index i + k - 1 
    # in its sorted list of positions.
    for char in char_indices:
        indices = char_indices[char]
        if len(indices) >= k:
            # Check every window of size k for this specific character
            for i in range(len(indices) - k + 1):
                # The window starts at indices[i] and ends at indices[i + k - 1]
                window_size = indices[i + k - 1] - indices[i] + 1
                if window_size < min_length:
                    min_length = window_size
                    
    return int(min_length) if min_length != float('inf') else -1
