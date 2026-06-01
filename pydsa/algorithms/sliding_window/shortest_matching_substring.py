METADATA = {
    "id": 3455,
    "name": "Shortest Matching Substring",
    "slug": "shortest_matching_substring",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Find the length of the shortest substring of s that contains all characters of t with at least the required frequencies.",
}

def solve(s: str, t: str) -> int:
    """
    Finds the length of the shortest substring of s that contains all characters 
    of t with at least the required frequencies.

    Args:
        s: The source string to search within.
        t: The target string containing required characters and frequencies.

    Returns:
        The length of the shortest matching substring, or -1 if no such substring exists.

    Examples:
        >>> solve("ADOBECODEBANC", "ABC")
        6
        >>> solve("a", "aa")
        -1
    """
    if not t:
        return 0
    if not s:
        return -1

    # Frequency map for characters required from t
    target_counts: dict[str, int] = {}
    for char in t:
        target_counts[char] = target_counts.get(char, 0) + 1

    # Number of unique characters in t that must be satisfied
    required_unique_chars = len(target_counts)
    
    # Current window state
    window_counts: dict[str, int] = {}
    # Number of unique characters in current window that meet the target frequency
    satisfied_chars = 0
    
    min_length = float('inf')
    left = 0

    # Expand the right boundary of the window
    for right in range(len(s)):
        char_right = s[right]
        window_counts[char_right] = window_counts.get(char_right, 0) + 1

        # If the current character's frequency matches the target, increment satisfied count
        if char_right in target_counts and window_counts[char_right] == target_counts[char_right]:
            satisfied_chars += 1

        # Shrink the window from the left as long as the condition is satisfied
        while satisfied_chars == required_unique_chars:
            # Update the minimum length found so far
            current_window_size = right - left + 1
            if current_window_size < min_length:
                min_length = current_window_size

            char_left = s[left]
            # If removing this character breaks the requirement, decrement satisfied count
            if char_left in target_counts and window_counts[char_left] == target_counts[char_left]:
                satisfied_chars -= 1
            
            window_counts[char_left] -= 1
            left += 1

    return int(min_length) if min_length != float('inf') else -1
