METADATA = {
    "id": 3298,
    "name": "Count Substrings That Can Be Rearranged to Contain a String II",
    "slug": "count-substrings-that-can-be-rearranged-to-contain-a-string-ii",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "frequency_array"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings that can be rearranged to contain a target string by using a sliding window to track character frequencies.",
}

def solve(s: str, target: str) -> int:
    """
    Counts the number of substrings of 's' that can be rearranged to contain 'target'.
    
    A substring can be rearranged to contain 'target' if and only if for every 
    character in 'target', the substring contains at least as many occurrences 
    of that character as 'target' does.

    Args:
        s: The source string.
        target: The target string to check against.

    Returns:
        The total count of valid substrings.

    Examples:
        >>> solve("abacaba", "aba")
        10
        >>> solve("abc", "def")
        0
    """
    n = len(s)
    m = len(target)
    
    if m > n:
        return 0

    # target_counts stores the required frequency of each character
    target_counts = {}
    for char in target:
        target_counts[char] = target_counts.get(char, 0) + 1
    
    # unique_chars_needed is the number of distinct characters in target 
    # that must meet a specific frequency threshold.
    unique_chars_needed = len(target_counts)
    
    # window_counts tracks the frequency of characters in the current window
    window_counts = {}
    # satisfied_chars tracks how many unique characters in target have 
    # met their required frequency in the current window.
    satisfied_chars = 0
    
    total_valid_substrings = 0
    left = 0

    # Iterate through the string with the 'right' pointer
    for right in range(n):
        char_right = s[right]
        
        # Only track characters that are actually in the target string
        if char_right in target_counts:
            window_counts[char_right] = window_counts.get(char_right, 0) + 1
            # If this character just reached the required frequency, increment satisfied count
            if window_counts[char_right] == target_counts[char_right]:
                satisfied_chars += 1
        
        # While the current window contains all characters of target with required frequencies
        while satisfied_chars == unique_chars_needed:
            # If the window [left, right] is valid, then all substrings 
            # starting at 'left' and ending at any index from 'right' to 'n-1' are valid.
            total_valid_substrings += (n - right)
            
            # Shrink the window from the left to find the next smallest valid window
            char_left = s[left]
            if char_left in target_counts:
                if window_counts[char_left] == target_counts[char_left]:
                    satisfied_chars -= 1
                window_counts[char_left] -= 1
            
            left += 1
            
    return total_valid_substrings
