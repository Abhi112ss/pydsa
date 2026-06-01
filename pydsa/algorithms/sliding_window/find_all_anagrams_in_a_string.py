METADATA = {
    "id": 438,
    "name": "Find All Anagrams in a String",
    "slug": "find-all-anagrams-in-a-string",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find all starting indices of p's anagrams in s using a sliding window approach.",
}

def solve(s: str, p: str) -> list[int]:
    """
    Finds all starting indices of p's anagrams in s.

    Args:
        s: The input string to search within.
        p: The pattern string to find anagrams of.

    Returns:
        A list of starting indices where an anagram of p begins in s.

    Examples:
        >>> solve("cbaebabacd", "abc")
        [0, 6]
        >>> solve("abab", "ab")
        [0, 1, 2]
    """
    s_len, p_len = len(s), len(p)
    if p_len > s_len:
        return []

    # Frequency maps for the pattern and the current window
    # Since we only deal with lowercase English letters, 
    # an array of size 26 is sufficient and provides O(1) space.
    p_counts = [0] * 26
    window_counts = [0] * 26
    results = []

    # Helper to map char to index 0-25
    def char_idx(char: str) -> int:
        return ord(char) - ord('a')

    # Initialize the pattern counts and the first window
    for i in range(p_len):
        p_counts[char_idx(p[i])] += 1
        window_counts[char_idx(s[i])] += 1

    # If the first window is an anagram
    if p_counts == window_counts:
        results.append(0)

    # Slide the window across the string s
    for i in range(p_len, s_len):
        # Add the new character entering the window from the right
        window_counts[char_idx(s[i])] += 1
        
        # Remove the character leaving the window from the left
        # The character to remove is at index (i - p_len)
        window_counts[char_idx(s[i - p_len])] -= 1

        # Compare the frequency arrays
        # Comparing two arrays of fixed size 26 is O(1)
        if window_counts == p_counts:
            results.append(i - p_len + 1)

    return results
