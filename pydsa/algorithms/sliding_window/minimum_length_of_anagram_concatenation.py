METADATA = {
    "id": 3138,
    "name": "Minimum Length of Anagram Concatenation",
    "slug": "minimum-length-of-anagram-concatenation",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "strings"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum length of a substring that contains all characters of the given words with their required frequencies.",
}

def solve(words: list[str], k: int) -> int:
    """
    Finds the minimum length of a substring that contains all characters 
    of the concatenated words, where each word is repeated k times.

    Args:
        words: A list of strings to be concatenated k times.
        k: The number of times each word is repeated.

    Returns:
        The minimum length of the substring, or -1 if no such substring exists.

    Examples:
        >>> solve(["un", "iq", "ue"], 1)
        4
        >>> solve(["un", "iq", "ue"], 2)
        8
        >>> solve(["a", "b", "c"], 1)
        3
    """
    # Calculate the target frequency map for all characters
    target_counts: dict[str, int] = {}
    total_required_chars: int = 0
    
    for word in words:
        for char in word:
            target_counts[char] = target_counts.get(char, 0) + k
            total_required_chars += 1
            
    # If the total length of words * k is greater than the string length, impossible
    # However, the problem implies we are looking for a substring within 's'
    # Wait, the problem description for 3138 actually provides a string 's' 
    # and a list of words. Let's adjust the signature to match the standard LeetCode format.
    # Re-reading: The problem is actually: Given a string 's' and an array of strings 'words',
    # find the minimum length of a substring of 's' that contains all characters 
    # of the concatenation of 'words' repeated 'k' times.
    return -1 # Placeholder for signature correction

def solve_actual(s: str, words: list[str], k: int) -> int:
    """
    Finds the minimum length of a substring of 's' that contains all characters 
    of the concatenation of 'words' repeated 'k' times.

    Args:
        s: The source string to search within.
        words: A list of strings.
        k: The repetition factor.

    Returns:
        The minimum length of the substring, or -1 if no such substring exists.
    """
    target_counts: dict[str, int] = {}
    total_needed: int = 0
    
    # Build the frequency map of the required characters
    for word in words:
        for char in word:
            target_counts[char] = target_counts.get(char, 0) + k
            total_needed += 1
            
    window_counts: dict[str, int] = {}
    formed_chars_count: int = 0
    min_len: float = float('inf')
    left: int = 0
    
    # Sliding window approach
    for right in range(len(s)):
        char_right = s[right]
        
        # Only track characters that are actually in our target set
        if char_right in target_counts:
            window_counts[char_right] = window_counts.get(char_right, 0) + 1
            # If this character reaches the required frequency, increment formed count
            if window_counts[char_right] == target_counts[char_right]:
                formed_chars_count += 1
        
        # While the current window satisfies the requirement
        while formed_chars_count == len(target_counts):
            # Update the minimum length found so far
            current_window_size = right - left + 1
            if current_window_size < min_len:
                min_len = current_window_size
            
            # Try to shrink the window from the left
            char_left = s[left]
            if char_left in target_counts:
                if window_counts[char_left] == target_counts[char_left]:
                    formed_chars_count -= 1
                window_counts[char_left] -= 1
            
            left += 1
            
    return int(min_len) if min_len != float('inf') else -1

# The problem 3138 signature is actually: minSubstringLength(s: str, words: List[str], k: int)
def minSubstringLength(s: str, words: list[str], k: int) -> int:
    """
    Implementation of LeetCode 3138.
    """
    return solve_actual(s, words, k)

# For the sake of the prompt's specific structure requirements, 
# we provide the solve function as the entry point.
def solve(s: str, words: list[str], k: int) -> int:
    """
    Finds the minimum length of a substring of 's' that contains all characters 
    of the concatenation of 'words' repeated 'k' times.

    Args:
        s: The source string to search within.
        words: A list of strings.
        k: The repetition factor.

    Returns:
        The minimum length of the substring, or -1 if no such substring exists.

    Examples:
        >>> solve("abcde", ["a", "b"], 1)
        2
        >>> solve("aaabbb", ["a", "b"], 2)
        4
    """
    target_counts: dict[str, int] = {}
    for word in words:
        for char in word:
            target_counts[char] = target_counts.get(char, 0) + k
            
    # Number of unique characters that must meet the frequency requirement
    required_unique_chars = len(target_counts)
    
    window_counts: dict[str, int] = {}
    satisfied_unique_chars = 0
    min_len = float('inf')
    left = 0
    
    for right in range(len(s)):
        char_right = s[right]
        if char_right in target_counts:
            window_counts[char_right] = window_counts.get(char_right, 0) + 1
            if window_counts[char_right] == target_counts[char_right]:
                satisfied_unique_chars += 1
        
        # Shrink window as long as it's valid
        while satisfied_unique_chars == required_unique_chars:
            min_len = min(min_len, right - left + 1)
            
            char_left = s[left]
            if char_left in target_counts:
                if window_counts[char_left] == target_counts[char_left]:
                    satisfied_unique_chars -= 1
                window_counts[char_left] -= 1
            left += 1
            
    return int(min_len) if min_len != float('inf') else -1