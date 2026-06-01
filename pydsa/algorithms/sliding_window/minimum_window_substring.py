METADATA = {
    "id": 76,
    "name": "Minimum Window Substring",
    "slug": "minimum-window-substring",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "string"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Find the minimum window in string s which contains all characters of string t.",
}

def solve(s: str, t: str) -> str:
    """
    Finds the minimum window substring in 's' that contains all characters of 't'.

    Args:
        s: The source string to search within.
        t: The target string containing required characters.

    Returns:
        The smallest substring of 's' containing all characters of 't', 
        or an empty string if no such window exists.

    Examples:
        >>> solve("ADOBECODEBANC", "ABC")
        'BANC'
        >>> solve("a", "a")
        'a'
        >>> solve("a", "aa")
        ''
    """
    if not t or not s:
        return ""

    # Dictionary to keep a count of all the unique characters in t.
    target_counts = {}
    for char in t:
        target_counts[char] = target_counts.get(char, 0) + 1

    # Number of unique characters in t that must be present in the window.
    required_unique_chars = len(target_counts)

    # Left and Right pointers for the sliding window.
    left = 0
    right = 0

    # formed tracks how many unique characters in t are present in the current window 
    # with the required frequency.
    formed = 0
    
    # Dictionary to keep track of characters in the current window.
    window_counts = {}

    # tuple to store (window length, left index, right index)
    ans = float("inf"), None, None

    while right < len(s):
        # Add character from the right to the window.
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        # If the frequency of the current character matches the required frequency in t.
        if char in target_counts and window_counts[char] == target_counts[char]:
            formed += 1

        # Try and contract the window till the point where it ceases to be 'desirable'.
        while left <= right and formed == required_unique_chars:
            char = s[left]

            # Save the smallest window found so far.
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)

            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[char] -= 1
            if char in target_counts and window_counts[char] < target_counts[char]:
                formed -= 1

            # Move the left pointer ahead, this helps in looking for a new window.
            left += 1    

        # Keep expanding the window by moving the right pointer.
        right += 1

    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
