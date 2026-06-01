METADATA = {
    "id": 2953,
    "name": "Count Complete Substrings",
    "slug": "count-complete-substrings",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings that contain each character at least as many times as it appears in the entire string.",
}

def solve(s: str) -> int:
    """
    Counts the number of substrings that contain each character at least 
    as many times as it appears in the entire string.

    Args:
        s: The input string.

    Returns:
        The total count of complete substrings.

    Examples:
        >>> solve("aab")
        1
        >>> solve("abcabc")
        9
    """
    # Step 1: Calculate the frequency of each character in the entire string
    target_counts = {}
    for char in s:
        target_counts[char] = target_counts.get(char, 0) + 1
    
    total_unique_chars = len(target_counts)
    n = len(s)
    
    # Step 2: Use a sliding window to find valid substrings
    # A substring is 'complete' if it contains all characters with at least 
    # the required frequency.
    ans = 0
    left = 0
    current_window_counts = {}
    # 'satisfied_chars' tracks how many unique characters meet the target frequency
    satisfied_chars = 0
    
    for right in range(n):
        char_right = s[right]
        current_window_counts[char_right] = current_window_counts.get(char_right, 0) + 1
        
        # If this character just reached the required frequency, increment satisfied_chars
        if char_right in target_counts and current_window_counts[char_right] == target_counts[char_right]:
            satisfied_chars += 1
            
        # Step 3: Shrink the window from the left as long as it remains 'complete'
        while satisfied_chars == total_unique_chars:
            # If the current window [left, right] is complete, then all substrings 
            # starting at 'left' and ending at any index from 'right' to 'n-1' 
            # are also complete.
            ans += (n - right)
            
            char_left = s[left]
            # If removing this character makes the window incomplete, decrement satisfied_chars
            if char_left in target_counts and current_window_counts[char_left] == target_counts[char_left]:
                satisfied_chars -= 1
            
            current_window_counts[char_left] -= 1
            left += 1
            
    return ans
