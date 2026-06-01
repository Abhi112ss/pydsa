METADATA = {
    "id": 3297,
    "name": "Count Substrings That Can Be Rearranged to Contain a String I",
    "slug": "count-substrings-that-can-be-rearranged-to-contain-a-string-i",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "two_pointers"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings that can be rearranged to contain all characters of a target string.",
}

def solve(s: str, target: str) -> int:
    """
    Counts the number of substrings in 's' that can be rearranged to contain 
    all characters of 'target'.

    A substring can be rearranged to contain 'target' if and only if the 
    substring contains at least as many occurrences of each character as 
    the 'target' string does.

    Args:
        s: The source string.
        target: The target string whose characters must be present in the substring.

    Returns:
        The total count of valid substrings.

    Examples:
        >>> solve("abcde", "abc")
        3
        >>> solve("aaabbb", "ab")
        9
    """
    target_counts = {}
    for char in target:
        target_counts[char] = target_counts.get(char, 0) + 1
    
    required_unique_chars = len(target_counts)
    window_counts = {}
    formed_unique_chars = 0
    
    total_substrings = 0
    left = 0
    n = len(s)

    # Use a sliding window approach with two pointers
    for right in range(n):
        char_right = s[right]
        
        # Update the frequency map for the current window
        if char_right in target_counts:
            window_counts[char_right] = window_counts.get(char_right, 0) + 1
            # If the current character's count matches the target's requirement
            if window_counts[char_right] == target_counts[char_right]:
                formed_unique_chars += 1
        
        # While the current window is valid (contains all characters of target)
        while formed_unique_chars == required_unique_chars:
            # If the window [left, right] is valid, then all substrings 
            # starting at 'left' and ending at any index from 'right' to 'n-1' are valid.
            total_substrings += (n - right)
            
            # Shrink the window from the left to find the next smallest valid window
            char_left = s[left]
            if char_left in target_counts:
                if window_counts[char_left] == target_counts[char_left]:
                    formed_unique_chars -= 1
                window_counts[char_left] -= 1
            
            left += 1
            
    return total_substrings
